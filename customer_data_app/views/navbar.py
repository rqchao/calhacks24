import reflex as rx
from ..backend.backend import State

def navbar():
    """Create the header content with title, navigation, and search."""
    return rx.flex(
        rx.badge(
            rx.icon(tag="paw-print", size=16),
            rx.heading("Ghostwriter", size="4"),
            color_scheme="indigo",
            radius="large",
            align="center",
            variant="surface",
            padding="0.65rem",
        ),
        rx.flex(
            create_search_box(),
            record_button(),
            display="flex",
            align_items="center",
            column_gap="5rem",
            width="80%",
            padding_left="0.5rem",
        ),
        display="flex",
        align_items="center",
        justify_content="space-between",
        width="100%", 
    )


def create_search_box():
    """Create a search box with input field and search icon."""
    return rx.box(
        rx.input(
        placeholder="Search metadata...",
        type="text",
        on_change=lambda value: State.filter_values(value),
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
        position="relative",
        width="100%",
    )

def record_button():
    return rx.button(
        rx.hstack(
            rx.icon(
                tag="circle",
                color=rx.cond(State.recording, "red", "white"),
                fill=rx.cond(State.recording, "red", "white"),
                display=rx.cond(~State.recording, "block", "none"),
                height="1rem",
                width="1rem",
                align_self="center",
            ),
            rx.icon(
                tag="square",
                color=rx.cond(State.recording, "red", "white"),
                fill=rx.cond(State.recording, "red", "white"),
                display=rx.cond(State.recording, "block", "none"),
                height="1rem",
                width="1rem",
                align_self="center",
            ),
            "Toggle Session Recording",
            align_items="center",
        ),
        on_click=State.toggle_recording,
        color_scheme=rx.cond(State.recording, "white", "red"),
        variant="solid",
        color=rx.cond(State.recording, "red", "white"),
        bg=rx.cond(State.recording, "white", "red"),
    )