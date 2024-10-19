import reflex as rx
from ..backend.backend import State


# def navbar():
#     return rx.flex(
#         rx.badge(
#             rx.icon(tag="table-2", size=28),
#             rx.heading("Virtual Teaching Assistant", size="6"),
#             color_scheme="green",
#             radius="large",
#             align="center",
#             variant="surface",
#             padding="0.65rem",
#         ),
#         rx.spacer(),
#         rx.hstack(
#             rx.logo(),
#             rx.color_mode.button(),
#             align="center",
#             spacing="3",
#         ),
#         spacing="2",
#         flex_direction=["column", "column", "row"],
#         align="center",
#         width="100%",
#         top="0px",
#         padding_top="2em",
#     )
def navbar():
    """Create the header content with title, navigation, and search."""
    return rx.flex(
        # rx.heading(
        #     heading_type="h1",
        #     text_color="#4F46E5",
        #     heading_text="Class Notes",
        # ),
        rx.badge(
            rx.icon(tag="table-2", size=28),
            rx.heading("Virtual Teaching Assistant", size="6"),
            color_scheme="indigo",
            radius="large",
            align="center",
            variant="surface",
            padding="0.65rem",
        ),
        rx.box(
            rx.link(
                hover_styles={"color": "#4F46E5"},
                text_color="#4B5563",
                link_text="Home",
            ),
            rx.link(
                hover_styles={"color": "#4F46E5"},
                text_color="#4B5563",
                link_text="Subjects",
            ),
            rx.link(
                hover_styles={"color": "#4F46E5"},
                text_color="#4B5563",
                link_text="About",
            ),
            display=rx.breakpoints(
                {"0px": "none", "768px": "flex"}
            ),
            column_gap="1.5rem",
        ),
        rx.flex(
            create_search_box(),
            create_new_note_button(),
            display="flex",
            align_items="center",
            column_gap="1rem",
        ),
        display="flex",
        align_items="center",
        justify_content="space-between",
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
        rx.input(placeholder="Search here..."),
        rx.icon(
            tag="search",
            position="absolute",
            height="1rem",
            left="0.75rem",
            color="#9CA3AF",
            top="0.625rem",
            width="1rem",
        ),
        position="relative",
    )

def create_search_input():
    """Create a search input field with custom styling."""
    return rx.input(
        placeholder="Search notes...",
        type="text",
        on_change=lambda value: State.filter_values(value),
        background_color="#F3F4F6",
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "#818CF8",
        },
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="9999px",
        font_size="0.875rem",
        line_height="1.25rem",
    )
