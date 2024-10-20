import reflex as rx


def form_field(
    label: str, placeholder: str, type: str, name: str, icon: str, default_value: str = ""
) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.hstack(
                rx.icon(icon, size=16, stroke_width=1.5),
                rx.form.label(label),
                align="center",
                spacing="2",
            ),
            rx.form.control(
                rx.input(
                    placeholder=placeholder, 
                    type=type,
                    default_value=default_value
                ),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
    )

def form_field_textarea(
    label: str, placeholder: str, name: str, icon: str, default_value: str = ""
) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(icon, size=16, stroke_width=1.5),
            rx.text(label),
            align="center",
            spacing="2",
        ),
        rx.text_area(
            placeholder=placeholder,
            default_value=default_value,
            name=name,
            width="100%",
        ),
        align_items="flex_start",
        width="100%",
        spacing="1",
    )