import reflex as rx
from typing import Literal, Union
from sqlmodel import select, asc, desc, or_, func, cast, String
from datetime import datetime, timedelta
from .vectordb import create_chroma_db, add_to_chroma_db
from .const import NOTE_1_CONTENT, NOTE_2_CONTENT, NOTE_3_CONTENT

#LiteralStatus = Literal["Delivered", "Pending", "Cancelled"]

def _get_percentage_change(value: Union[int, float], prev_value: Union[int, float]) -> float:
    percentage_change = (
        round(((value - prev_value) / prev_value) * 100, 2)
        if prev_value != 0
        else 0
        if value == 0
        else
        float("inf")
    )
    return percentage_change

class Customer(rx.Model, table=True):
    """The customer model."""

    name: str
    email: str
    phone: str
    address: str
    date: str
    payments: float
    status: str


class User(rx.Model, table=True):
    """The user model."""

    name: str
    email: str
    phone: str


class Note(rx.Model, table=True):
    """The note model."""

    name: str
    content: str # is there a way to represent like latex here or smth
    date: str
    course_id: str


class MonthValues(rx.Base):
    """Values for a month."""

    num_customers: int = 0
    total_payments: float = 0.0
    num_delivers: int = 0



class State(rx.State):
    """The app state."""

    users: list[Customer] = []
    sort_value: str = ""
    sort_reverse: bool = False
    search_value: str = ""
    current_user: Customer = Customer()
    # Values for current and previous month
    current_month_values: MonthValues = MonthValues()
    previous_month_values: MonthValues = MonthValues()
    # vector_db: any = None
    document_content: str = """# Links and Switches \n Links and switches have limited capacity → 
    how do we share space? We typically **dynamically allocate based on demand**. This is based on 
    the idea that the **peak of aggregate demand is often lower than the aggregate of peak demands**. 
    This approach is much more efficient. Peaks still happen, causing delays or drops, but we tolerate 
    it. Some firms like financial exchanges build their own statically-allocated networks to prevent 
    any delays, and are less sensitive of the cost of doing so. \n ## How do we actually do this dynamic allocation, though? \n - Best effort: everyone sends and see what happens. \n - **Packet 
    switching** does this by forwarding each packet it receives individually, without coordination \n - 
    Reservations: users request bandwidth at start of flow, and release it at end. \n - **Circuit 
    switching** does this by routing at the start and coordinating all routers along a path \n\n Notice 
    both are still statistical multiplexing, just at different granularities. We can define burstiness 
    ($\\frac{\\text{peak usage}}{\\text{{average usage}}}$) as one way to compare the two.
    """
    is_streaming: bool = False

    # def __init__(self):
    #     super().__init__()
        # self.vector_db = create_chroma_db("Notes")

    def start_streaming(self, _ev=None):
        self.is_streaming = True
        # In a real implementation, you would set up an async task to stream content
        # For demonstration, we'll just update the content after a delay
        yield rx.set_timeout(1, self.update_content("Initial content\n"))
        yield rx.set_timeout(2, self.update_content("More content\n"))
        yield rx.set_timeout(3, self.update_content("Final content"))
        yield rx.set_timeout(4, self.stop_streaming())

    def update_content(self, new_content: str):
        self.document_content += new_content

    def stop_streaming(self):
        self.is_streaming = False

    def load_entries(self) -> list[Customer]:
        """Get all users from the database."""
        with rx.session() as session:
            query = select(Customer)
            if self.search_value:
                search_value = f"%{str(self.search_value).lower()}%"
                query = query.where(
                    or_(
                        *[
                            getattr(Customer, field).ilike(search_value)
                            for field in Customer.get_fields()
                            if field not in ["id", "payments"]
                        ],
                        # ensures that payments is cast to a string before applying the ilike operator
                        cast(Customer.payments, String).ilike(search_value)
                    )
                )

            if self.sort_value:
                sort_column = getattr(Customer, self.sort_value)
                if self.sort_value == "payments":
                    order = desc(sort_column) if self.sort_reverse else asc(sort_column)
                else:
                    order = desc(func.lower(sort_column)) if self.sort_reverse else asc(func.lower(sort_column))
                query = query.order_by(order)
            
            self.users = session.exec(query).all()

        self.get_current_month_values()
        self.get_previous_month_values()


    def get_current_month_values(self):
        """Calculate current month's values."""
        now = datetime.now()
        start_of_month = datetime(now.year, now.month, 1)
        
        current_month_users = [
            user for user in self.users if datetime.strptime(user.date, '%Y-%m-%d %H:%M:%S') >= start_of_month
        ]
        num_customers = len(current_month_users)
        total_payments = sum(user.payments for user in current_month_users)
        num_delivers = len([user for user in current_month_users if user.status == "Delivered"])
        self.current_month_values = MonthValues(num_customers=num_customers, total_payments=total_payments, num_delivers=num_delivers)


    def get_previous_month_values(self):
        """Calculate previous month's values."""
        now = datetime.now()
        first_day_of_current_month = datetime(now.year, now.month, 1)
        last_day_of_last_month = first_day_of_current_month - timedelta(days=1)
        start_of_last_month = datetime(last_day_of_last_month.year, last_day_of_last_month.month, 1)
        
        previous_month_users = [
            user for user in self.users
            if start_of_last_month <= datetime.strptime(user.date, '%Y-%m-%d %H:%M:%S') <= last_day_of_last_month
        ]
        # We add some dummy values to simulate growth/decline. Remove them in production.
        num_customers = len(previous_month_users) + 3
        total_payments = sum(user.payments for user in previous_month_users) + 240
        num_delivers = len([user for user in previous_month_users if user.status == "Delivered"]) + 5
        
        self.previous_month_values = MonthValues(num_customers=num_customers, total_payments=total_payments, num_delivers=num_delivers)


    def sort_values(self, sort_value: str):
        self.sort_value = sort_value
        self.load_entries()


    def toggle_sort(self):
        self.sort_reverse = not self.sort_reverse
        self.load_entries()

    def filter_values(self, search_value):
        self.search_value = search_value
        self.load_entries()

    def get_user(self, user: Customer):
        self.current_user = user

    
    def add_notes(self, form_data: dict):
        self.current_note = form_data
        self.current_note["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with rx.session() as session: # TODO: change below to be based on users
            if session.exec(
                select(User).where(User.email == self.current_user["email"])
            ).first():
                return rx.window_alert("User with this email already exists")
            session.add(User(**self.current_user))
            session.commit()
        self.load_entries()

        # add_to_chroma_db(vector_db, self.current_note["content"])

        return rx.toast.info(f"Note page {self.current_note['name']} has been added.", position="bottom-right")


    def add_customer_to_db(self, form_data: dict):
        self.current_user = form_data
        self.current_user["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with rx.session() as session:
            if session.exec(
                select(Customer).where(Customer.email == self.current_user["email"])
            ).first():
                return rx.window_alert("User with this email already exists")
            session.add(Customer(**self.current_user))
            session.commit()
        self.load_entries()
        return rx.toast.info(f"User {self.current_user['name']} has been added.", position="bottom-right")
    

    def update_customer_to_db(self, form_data: dict):
        self.current_user.update(form_data)
        with rx.session() as session:
            customer = session.exec(
                select(Customer).where(Customer.id == self.current_user["id"])
            ).first()
            for field in Customer.get_fields():
                if field != "id":
                    setattr(customer, field, self.current_user[field])
            session.add(customer)
            session.commit()
        self.load_entries()
        return rx.toast.info(f"User {self.current_user['name']} has been modified.", position="bottom-right")


    def delete_customer(self, id: int):
        """Delete a customer from the database."""
        with rx.session() as session:
            customer = session.exec(select(Customer).where(Customer.id == id)).first()
            session.delete(customer)
            session.commit()
        self.load_entries()
        return rx.toast.info(f"User {customer.name} has been deleted.", position="bottom-right")
    
    
    @rx.var
    def payments_change(self) -> float:
        return _get_percentage_change(self.current_month_values.total_payments, self.previous_month_values.total_payments)

    @rx.var
    def customers_change(self) -> float:
        return _get_percentage_change(self.current_month_values.num_customers, self.previous_month_values.num_customers)

    @rx.var
    def delivers_change(self) -> float:
        return _get_percentage_change(self.current_month_values.num_delivers, self.previous_month_values.num_delivers)
    

    def create_sample_notes(self):
        now = datetime.now()

        note_1 = {"name": "Introduction to the Internet", 
                  "content": NOTE_1_CONTENT, 
                  "date": datetime(now.year, now.month, 1), 
                  "course_id": "Networking 101"}
        note_2 = {"name": "Router Hardware", 
                  "content": NOTE_2_CONTENT, 
                  "date": datetime(now.year, now.month, 5), 
                  "course_id": "Networking 101"}
        note_3 = {"name": "Cellular Technologies", 
                  "content": NOTE_3_CONTENT, 
                  "date": datetime(now.year, now.month, 11), 
                  "course_id": "Networking 101"}
        
        self.add_notes(note_1)
        self.add_notes(note_2)
        self.add_notes(note_3)

        add_to_chroma_db(self.vector_db, "Introduction to the Internet" + NOTE_1_CONTENT)
        add_to_chroma_db(self.vector_db, "Router Hardware" + NOTE_2_CONTENT)
        add_to_chroma_db(self.vector_db, "Cellular Technologies" + NOTE_3_CONTENT)
