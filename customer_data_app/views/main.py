import reflex as rx
from ..backend.backend import State, Note
from ..components.form_field import form_field, form_field_textarea

def show_notes(note: Note):
    """Show a customer in a table row."""

    return rx.table.row(
        rx.table.cell(note.name),
        rx.table.cell(note.course_id),
        # rx.table.cell(DateFormatter(date=note.date)),
        rx.table.cell(note.date),
        # rx.table.cell(rx.match(
        #     user.status,
        #     ("Delivered", status_badge("Delivered")),
        #     ("Pending", status_badge("Pending")),
        #     ("Cancelled", status_badge("Cancelled")),
        #     status_badge("Pending")
        # )),
        rx.table.cell(
            rx.hstack(
                rx.icon_button(
                    rx.icon("trash-2", size=22),
                    on_click=lambda: State.delete_note(getattr(note, "name")),
                    size="2",
                    variant="solid",
                    color_scheme="red",
                ),
            )
        ),
        style={"_hover": {"bg": rx.color("gray", 3)}},
        on_click=State.set_content(note.content),
        cursor="pointer",
        align="center",
    )


def push_test_data():
    return rx.el.button(
        "Push Data",
        background_color="#4F46E5",
        transition_duration="300ms",
        font_weight="500",
        _hover={"background-color": "#4338CA"},
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="9999px",
        font_size="0.875rem",
        line_height="1.25rem",
        color="#ffffff",
        on_click=State.create_sample_notes,
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def add_document_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Add Note", size="4", display=[
                        "none", "none", "block"]),
                size="3",
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="users", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Add New Note",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Fill out the form with the note details and content",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(
                    rx.flex(
                        # Name
                        form_field(
                            "Title",
                            "Note Title",
                            "text",
                            "name",
                            "a-large-small",
                        ),
                        # Course ID
                        form_field(
                            "Course ID",
                            "CS 61A",
                            "text",
                            "course_id",
                            "scan-barcode",
                        ),
                        # Note Content
                        form_field_textarea(
                            label="Note Content",
                            placeholder="Content",
                            name="content",
                            icon="notepad-text",
                        ),
                        # Status
                        # rx.vstack(
                        #     rx.hstack(
                        #         rx.icon("truck", size=16, stroke_width=1.5),
                        #         rx.text("Status"),
                        #         align="center",
                        #         spacing="2",
                        #     ),
                        #     rx.radio(
                        #         ["Delivered", "Pending", "Cancelled"],
                        #         name="status",
                        #         direction="row",
                        #         as_child=True,
                        #         required=True,
                        #     ),
                        # ),
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Add notes"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=State.add_note_to_db,
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            style={"max_width": 450},
            box_shadow="lg",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )


def document_display_box():
    return rx.box(
        rx.scroll_area(
            rx.vstack(
                rx.hstack(
                    rx.icon("square-pen", size=34),
                    rx.vstack(
                        rx.heading("Document Content", size="lg"),
                        # rx.text("Viewing and editing document"),
                        align_items="start",
                    ),
                    width="100%",
                    spacing="4",
                    padding_bottom="4",
                ),
                rx.divider(),
                rx.box(
                    rx.cond(
                        State.is_streaming,
                        rx.hstack(
                            rx.image(
                                src="llama.svg",
                                height="1.5em",
                                class_name="animate-pulse",
                            ),
                            rx.text("Streaming..."),
                            spacing="2",
                        ),
                        rx.text(""),
                    ),
                    rx.box(
                        rx.markdown(
                            State.document_content,
                            color="black",
                        ),
                        rx.box(
                            rx.button(
                                rx.icon(tag="copy", size=18),
                                on_click=[rx.set_clipboard(State.document_content), rx.toast("Copied!")],
                                title="Copy",
                                variant="ghost",
                                size="sm",
                            ),
                            position="absolute",
                            bottom="4",
                            right="4",
                            opacity="0",
                            _group_hover={"opacity": "1"},
                            transition="opacity 0.3s",
                        ),
                        background_color="#FFFBEB",
                        margin_bottom="1.5rem",
                        padding="1.5rem",
                        border_radius="0.5rem",
                    ),
                ),
                width="100%",
                align_items="stretch",
                spacing="4",
            ),
            scrollbar_size="2",
            padding_right="4",
        ),
        width="100%",
        max_width="800px",
        height="70vh",
        padding="6",
        border_radius="lg",
        box_shadow="lg",
        position="relative",
        overflow="hidden",
    )

def _header_cell(text: str, icon: str):
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
        ),
    )


def test_chroma_query():
    return rx.box(
        rx.input(
            placeholder="Semantic search...",
            type="text",
            value=State.search_query,
            on_change=State.set_search_query,
            # on_key_down=lambda key: State.perform_search() if key == "Enter" else None,
            on_blur = State.perform_search(),
            padding_left="1.5rem",
        ),
        rx.icon(
            tag="search",
            position="absolute",
            height="1rem",
            left="0.75rem",
            color="#9CA3AF",
            top="0.5rem",
            width="1rem",
        ),
        rx.dialog.root(
            rx.dialog.trigger(rx.button("Search")),
            rx.dialog.content(
                rx.dialog.title("Search Results"),
                rx.dialog.description(
                    # State.search_results,
                    rx.unordered_list(
                        rx.foreach(
                            State.search_results,
                            lambda result: rx.list_item(result)
                        )
                    )
                ),
                rx.dialog.close(
                    rx.button("Close", on_click=State.close_dialog)
                ),
                open=State.show_dialog,
            ),
        ),
        position="relative",
        width="100%",
    )

def main_table():
    return rx.fragment(
        rx.flex(
            add_document_button(),
            push_test_data(),
            test_chroma_query(),
            rx.spacer(),
            rx.hstack(
                rx.cond(
                    State.sort_reverse,
                    rx.icon("arrow-down-z-a", size=28, stroke_width=1.5, cursor="pointer", on_click=State.toggle_sort),
                    rx.icon("arrow-down-a-z", size=28, stroke_width=1.5, cursor="pointer", on_click=State.toggle_sort),
                ),
                rx.select(
                    ["name", "course_id", "date"],
                    placeholder="Sort By: Date",
                    size="3",
                    on_change=lambda sort_value: State.sort_values(sort_value),
                ),
                spacing="3",
                align="center",
            ),
            spacing="3",
            wrap="wrap",
            width="100%",
            padding_bottom="1em",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell("Title", "a-large-small"),
                    _header_cell("Course ID", "scan-barcode"),
                    _header_cell("Date", "calendar"),
                    _header_cell("Delete", "trash-2")
                ),
            ),
            rx.table.body(rx.foreach(State.notes, show_notes)),
            variant="surface",
            size="3",
            width="100%",
            on_mount=State.load_entries,
        ),
    )
