import reflex as rx
from ..backend.backend import State

def navbar():
    """Create the header content with title, navigation, and search."""
    return rx.flex(
        rx.badge(
            rx.icon(tag="paw-print", size=16),
            rx.heading("Oski's Little Helper", size="4"),
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

def create_new_note_button():
    """Create a 'New Note' button with custom styling."""
    return rx.el.button(
        "New Note",
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
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_search_box():
    """Create a search box with input field and search icon."""
    return rx.box(
        rx.input(
        placeholder="Search notes...",
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
                color="white",
                fill="white",
                display=rx.cond(State.recording, "block", "none"),
                height="1rem",
                width="1rem",
                align_self="center",
            ),
            rx.icon(
                tag="square",
                color="white",
                fill="white",
                display=rx.cond(~State.recording, "block", "none"),
                height="1rem",
                width="1rem",
                align_self="center",
            ),
            "Toggle Session Recording",
            align_items="center",
        ),
        on_click=State.toggle_recording,
        color_scheme="red",
        variant="solid",
        color="white",
    )
