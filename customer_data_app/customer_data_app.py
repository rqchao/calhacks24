"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .views.main import document_display_box
from .views.navbar import navbar
from .views.main import main_table


def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.flex(
            rx.box(main_table(), width=["100%", "100%", "100%", "60%"]),
            document_display_box(),
            spacing="6",
            width="100%",
            flex_direction=["column", "column", "column", "row"],
        ),
        height="100vh",
        bg=rx.color("accent", 1),
        width="100%",
        spacing="6",
        padding_x=["1.5em", "1.5em", "3em"],
        padding_y=["1em", "1em", "2em"],
    )


# Create app instance and add index page.
app = rx.App(
    theme=rx.theme(
        appearance="dark", has_background=True, radius="large", accent_color="indigo"
    ),
)

app.add_page(
    index,
    title="Ghostwriter",
    description="Your virtual teaching assistant.",
)
