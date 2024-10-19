# def create_stylesheet_link(stylesheet_url):
#     """Create a link element for a stylesheet."""
#     return rx.el.link(href=stylesheet_url, rel="stylesheet")


# def create_small_heading(
#     heading_type, text_color, heading_text
# ):
#     """Create a small heading with custom styling."""
#     return rx.heading(
#         heading_text,
#         font_weight="500",
#         color=text_color,
#         font_size="1.125rem",
#         line_height="1.75rem",
#         as_=heading_type,
#     )


# def create_medium_heading(
#     heading_type, text_color, heading_text
# ):
#     """Create a medium-sized heading with custom styling."""
#     return rx.heading(
#         heading_text,
#         font_weight="700",
#         font_size="1.5rem",
#         line_height="2rem",
#         color=text_color,
#         as_=heading_type,
#     )


# def create_hover_link(hover_styles, text_color, link_text):
#     """Create a link with hover effects and custom styling."""
#     return rx.el.a(
#         link_text,
#         href="#",
#         transition_duration="300ms",
#         _hover=hover_styles,
#         color=text_color,
#         transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
#         transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
#     )


# def create_section_heading(heading_type, heading_text):
#     """Create a section heading with predefined styling."""
#     return rx.heading(
#         heading_text,
#         font_weight="600",
#         margin_bottom="1rem",
#         color="#1F2937",
#         font_size="1.25rem",
#         line_height="1.75rem",
#         as_=heading_type,
#     )


# def create_form_label(label_text):
#     """Create a form label with predefined styling."""
#     return rx.el.label(
#         label_text,
#         display="block",
#         font_weight="500",
#         margin_bottom="0.25rem",
#         color="#374151",
#         font_size="0.875rem",
#         line_height="1.25rem",
#     )


# def create_select_option(option_text):
#     """Create an option element for a select input."""
#     return rx.el.option(option_text)


# def create_paragraph_text(paragraph_content):
#     """Create a paragraph with predefined styling."""
#     return rx.text(
#         paragraph_content,
#         color="#4B5563",
#         font_size="0.875rem",
#         line_height="1.25rem",
#     )


# def create_hoverable_note_box(note_title, note_description):
#     """Create a hoverable box for displaying a note with title and description."""
#     return rx.box(
#         create_small_heading(
#             heading_type="h3",
#             text_color="#1F2937",
#             heading_text=note_title,
#         ),
#         create_paragraph_text(
#             paragraph_content=note_description
#         ),
#         cursor="pointer",
#         transition_duration="300ms",
#         _hover={"background-color": "#EEF2FF"},
#         padding="0.75rem",
#         border_radius="0.375rem",
#         transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
#         transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
#     )


# def create_icon(
#     icon_height, margin_right, icon_tag, icon_width
# ):
#     """Create an icon with custom dimensions and margin."""
#     return rx.icon(
#         tag=icon_tag,
#         height=icon_height,
#         margin_right=margin_right,
#         width=icon_width,
#     )


# def create_icon_button(
#     icon_height, icon_tag, icon_width, button_text
# ):
#     """Create a button with an icon and text."""
#     return rx.el.button(
#         create_icon(
#             icon_height=icon_height,
#             margin_right="0.25rem",
#             icon_tag=icon_tag,
#             icon_width=icon_width,
#         ),
#         button_text,
#         transition_duration="300ms",
#         display="flex",
#         _hover={"color": "#3730A3"},
#         align_items="center",
#         color="#4F46E5",
#         transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
#         transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
#     )


# def create_list_item(item_content):
#     """Create a list item element."""
#     return rx.el.li(item_content)


# def create_custom_heading(
#     heading_type, font_size, margin_bottom, heading_text
# ):
#     """Create a heading with custom font size and margin."""
#     return rx.heading(
#         heading_text,
#         font_weight="600",
#         margin_bottom=margin_bottom,
#         font_size=font_size,
#         line_height="1.75rem",
#         as_=heading_type,
#     )


# def create_footer_link_item(link_text):
#     """Create a footer link item with hover effect."""
#     return rx.el.li(
#         create_hover_link(
#             hover_styles={"color": "#ffffff"},
#             text_color="#9CA3AF",
#             link_text=link_text,
#         )
#     )


# def create_social_icon(alt_text, icon_tag):
#     """Create a social media icon."""
#     return rx.icon(
#         alt=alt_text,
#         tag=icon_tag,
#         height="1.5rem",
#         width="1.5rem",
#     )


# def create_social_link(alt_text, icon_tag):
#     """Create a social media link with icon."""
#     return rx.el.a(
#         create_social_icon(
#             alt_text=alt_text, icon_tag=icon_tag
#         ),
#         href="#",
#         transition_duration="300ms",
#         _hover={"color": "#ffffff"},
#         color="#9CA3AF",
#         transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
#         transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
#     )


# def create_search_input():
#     """Create a search input field with custom styling."""
#     return rx.el.input(
#         placeholder="Search notes...",
#         type="text",
#         background_color="#F3F4F6",
#         _focus={
#             "outline-style": "none",
#             "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
#             "--ring-color": "#818CF8",
#         },
#         padding_left="1rem",
#         padding_right="1rem",
#         padding_top="0.5rem",
#         padding_bottom="0.5rem",
#         border_radius="9999px",
#         font_size="0.875rem",
#         line_height="1.25rem",
#     )


# def create_search_box():
#     """Create a search box with input field and search icon."""
#     return rx.box(
#         create_search_input(),
#         rx.icon(
#             tag="search",
#             position="absolute",
#             height="1rem",
#             left="0.75rem",
#             color="#9CA3AF",
#             top="0.625rem",
#             width="1rem",
#         ),
#         position="relative",
#     )


# def create_new_note_button():
#     """Create a 'New Note' button with custom styling."""
#     return rx.el.button(
#         "New Note",
#         background_color="#4F46E5",
#         transition_duration="300ms",
#         font_weight="500",
#         _hover={"background-color": "#4338CA"},
#         padding_left="1rem",
#         padding_right="1rem",
#         padding_top="0.5rem",
#         padding_bottom="0.5rem",
#         border_radius="9999px",
#         font_size="0.875rem",
#         line_height="1.25rem",
#         color="#ffffff",
#         transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
#         transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
#     )


# def create_header_content():
#     """Create the header content with title, navigation, and search."""
#     return rx.flex(
#         create_medium_heading(
#             heading_type="h1",
#             text_color="#4F46E5",
#             heading_text="Class Notes",
#         ),
#         rx.box(
#             create_hover_link(
#                 hover_styles={"color": "#4F46E5"},
#                 text_color="#4B5563",
#                 link_text="Home",
#             ),
#             create_hover_link(
#                 hover_styles={"color": "#4F46E5"},
#                 text_color="#4B5563",
#                 link_text="Subjects",
#             ),
#             create_hover_link(
#                 hover_styles={"color": "#4F46E5"},
#                 text_color="#4B5563",
#                 link_text="About",
#             ),
#             display=rx.breakpoints(
#                 {"0px": "none", "768px": "flex"}
#             ),
#             column_gap="1.5rem",
#         ),
#         rx.flex(
#             create_search_box(),
#             create_new_note_button(),
#             display="flex",
#             align_items="center",
#             column_gap="1rem",
#         ),
#         display="flex",
#         align_items="center",
#         justify_content="space-between",
#     )


# def create_sticky_header():
#     """Create a sticky header with responsive layout."""
#     return rx.box(
#         rx.box(
#             create_header_content(),
#             width="100%",
#             style=rx.breakpoints(
#                 {
#                     "640px": {"max-width": "640px"},
#                     "768px": {"max-width": "768px"},
#                     "1024px": {"max-width": "1024px"},
#                     "1280px": {"max-width": "1280px"},
#                     "1536px": {"max-width": "1536px"},
#                 }
#             ),
#             margin_left="auto",
#             margin_right="auto",
#             padding_left=rx.breakpoints(
#                 {
#                     "0px": "1rem",
#                     "640px": "1.5rem",
#                     "1024px": "2rem",
#                 }
#             ),
#             padding_right=rx.breakpoints(
#                 {
#                     "0px": "1rem",
#                     "640px": "1.5rem",
#                     "1024px": "2rem",
#                 }
#             ),
#             padding_top="1rem",
#             padding_bottom="1rem",
#         ),
#         background_color="#ffffff",
#         box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
#         position="sticky",
#         top="0",
#         z_index="10",
#     )


# def create_subject_select():
#     """Create a select input for choosing subjects."""
#     return rx.el.select(
#         create_select_option(option_text="All Subjects"),
#         create_select_option(option_text="Mathematics"),
#         create_select_option(option_text="Physics"),
#         create_select_option(
#             option_text="Computer Science"
#         ),
#         create_select_option(option_text="Chemistry"),
#         id="subject",
#         background_color="#F3F4F6",
#         border_width="1px",
#         border_color="#D1D5DB",
#         _focus={
#             "outline-style": "none",
#             "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
#             "--ring-color": "#818CF8",
#         },
#         padding_left="0.75rem",
#         padding_right="0.75rem",
#         padding_top="0.5rem",
#         padding_bottom="0.5rem",
#         border_radius="0.375rem",
#         width="100%",
#     )


# def create_date_input():
#     """Create a date input field."""
#     return rx.el.input(
#         id="date",
#         type="date",
#         background_color="#F3F4F6",
#         border_width="1px",
#         border_color="#D1D5DB",
#         _focus={
#             "outline-style": "none",
#             "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
#             "--ring-color": "#818CF8",
#         },
#         padding_left="0.75rem",
#         padding_right="0.75rem",
#         padding_top="0.5rem",
#         padding_bottom="0.5rem",
#         border_radius="0.375rem",
#         width="100%",
#     )


# def create_filter_section():
#     """Create a filter section with subject and date inputs."""
#     return rx.box(
#         create_section_heading(
#             heading_type="h2", heading_text="Filter Notes"
#         ),
#         rx.box(
#             rx.box(
#                 create_form_label(label_text="Subject"),
#                 create_subject_select(),
#             ),
#             rx.box(
#                 create_form_label(label_text="Date"),
#                 create_date_input(),
#             ),
#             display="flex",
#             flex_direction="column",
#             gap="0.875rem",
#         ),
#         background_color="#ffffff",
#         margin_bottom="1.5rem",
#         padding="1.5rem",
#         border_radius="0.5rem",
#         box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
#     )


# def create_notes_list():
#     """Create a list of notes with subject and description."""
#     return rx.box(
#         create_section_heading(
#             heading_type="h2", heading_text="Notes List"
#         ),
#         rx.box(
#             create_hoverable_note_box(
#                 note_title="Mathematics: Calculus",
#                 note_description="Limits and Continuity",
#             ),
#             create_hoverable_note_box(
#                 note_title="Physics: Thermodynamics",
#                 note_description="Laws and Applications",
#             ),
#             create_hoverable_note_box(
#                 note_title="Computer Science: Data Structures",
#                 note_description="Binary Trees",
#             ),
#             create_hoverable_note_box(
#                 note_title="Chemistry: Organic Chemistry",
#                 note_description="Alkanes and Alkenes",
#             ),
#             display="flex",
#             flex_direction="column",
#             gap="1rem",
#         ),
#         background_color="#ffffff",
#         padding="1.5rem",
#         border_radius="0.5rem",
#         box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
#     )


# def create_topics_list():
#     """Create a list of topics for a specific subject."""
#     return rx.list(
#         create_list_item(
#             item_content="Definition of a limit"
#         ),
#         create_list_item(
#             item_content="Properties of limits"
#         ),
#         create_list_item(
#             item_content="Techniques for evaluating limits"
#         ),
#         create_list_item(
#             item_content="Continuity of functions"
#         ),
#         create_list_item(
#             item_content="Types of discontinuities"
#         ),
#         display="flex",
#         flex_direction="column",
#         list_style_type="disc",
#         list_style_position="inside",
#         gap="0.5rem",
#         color="#374151",
#     )


# def create_note_content():
#     """Create the main content of a note including description and key takeaways."""
#     return rx.box(
#         rx.text(
#             "Limits and continuity are fundamental concepts in calculus that help us understand the behavior of functions as they approach certain points. These concepts form the foundation for more advanced topics in calculus, such as derivatives and integrals.",
#             margin_bottom="1rem",
#         ),
#         create_custom_heading(
#             heading_type="h4",
#             font_size="1.125rem",
#             margin_bottom="0.5rem",
#             heading_text="Key Takeaways:",
#         ),
#         rx.list(
#             create_list_item(
#                 item_content="A limit describes the value that a function approaches as the input gets closer to a specific value."
#             ),
#             create_list_item(
#                 item_content="Continuity is a property of functions where there are no breaks, jumps, or holes in their graphs."
#             ),
#             create_list_item(
#                 item_content="Understanding limits and continuity is crucial for analyzing function behavior and solving real-world problems."
#             ),
#             list_style_type="disc",
#             list_style_position="inside",
#             margin_bottom="1rem",
#         ),
#         class_name="prose",
#         max_width="none",
#     )


# def create_note_footer():
#     """Create a footer for a note with last updated date and action buttons."""
#     return rx.flex(
#         rx.flex(
#             create_icon(
#                 icon_height="1rem",
#                 margin_right="0.5rem",
#                 icon_tag="calendar",
#                 icon_width="1rem",
#             ),
#             rx.text.span("Last updated: May 15, 2023"),
#             display="flex",
#             align_items="center",
#         ),
#         rx.flex(
#             create_icon_button(
#                 icon_height="1rem",
#                 icon_tag="edit",
#                 icon_width="1rem",
#                 button_text=" Edit ",
#             ),
#             create_icon_button(
#                 icon_height="1rem",
#                 icon_tag="share-2",
#                 icon_width="1rem",
#                 button_text=" Share ",
#             ),
#             display="flex",
#             align_items="center",
#             column_gap="1rem",
#         ),
#         display="flex",
#         align_items="center",
#         justify_content="space-between",
#         margin_top="2rem",
#         color="#4B5563",
#         font_size="0.875rem",
#         line_height="1.25rem",
#     )


# def create_full_note_view():
#     """Create a full view of a note including title, topics, content, and footer."""
#     return rx.box(
#         rx.flex(
#             create_medium_heading(
#                 heading_type="h2",
#                 text_color="#1F2937",
#                 heading_text="Mathematics: Calculus",
#             ),
#             create_icon_button(
#                 icon_height="1.25rem",
#                 icon_tag="bookmark",
#                 icon_width="1.25rem",
#                 button_text=" Save Note ",
#             ),
#             display="flex",
#             align_items="center",
#             justify_content="space-between",
#             margin_bottom="1.5rem",
#         ),
#         rx.box(
#             create_section_heading(
#                 heading_type="h3",
#                 heading_text="Limits and Continuity",
#             ),
#             create_topics_list(),
#             background_color="#FFFBEB",
#             margin_bottom="1.5rem",
#             padding="1.5rem",
#             border_radius="0.5rem",
#         ),
#         create_note_content(),
#         create_note_footer(),
#         background_color="#ffffff",
#         padding="2rem",
#         border_radius="0.5rem",
#         box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
#     )


# def create_main_content():
#     """Create the main content section with filter, notes list, and full note view."""
#     return rx.flex(
#         rx.box(
#             create_filter_section(),
#             create_notes_list(),
#             width=rx.breakpoints(
#                 {"0px": "100%", "1024px": "33.333333%"}
#             ),
#         ),
#         rx.box(
#             create_full_note_view(),
#             width=rx.breakpoints(
#                 {"0px": "100%", "1024px": "66.666667%"}
#             ),
#         ),
#         display="flex",
#         flex_direction=rx.breakpoints(
#             {"0px": "column", "1024px": "row"}
#         ),
#         gap="2rem",
#     )


# def create_footer_quick_links():
#     """Create the quick links section for the footer."""
#     return rx.box(
#         create_custom_heading(
#             heading_type="h3",
#             font_size="1.25rem",
#             margin_bottom="1rem",
#             heading_text="Quick Links",
#         ),
#         rx.list(
#             create_footer_link_item(link_text="Home"),
#             create_footer_link_item(link_text="Subjects"),
#             create_footer_link_item(link_text="About"),
#             create_footer_link_item(link_text="Contact"),
#             display="flex",
#             flex_direction="column",
#             gap="0.5rem",
#         ),
#         margin_bottom=rx.breakpoints(
#             {"0px": "1.5rem", "768px": "0"}
#         ),
#         width=rx.breakpoints(
#             {"0px": "100%", "768px": "33.333333%"}
#         ),
#     )


# def create_footer_content():
#     """Create the main content for the footer including quick links and social media."""
#     return rx.flex(
#         rx.box(
#             create_custom_heading(
#                 heading_type="h3",
#                 font_size="1.25rem",
#                 margin_bottom="1rem",
#                 heading_text="Class Notes",
#             ),
#             rx.text(
#                 "Empowering students with organized and accessible study materials.",
#                 color="#9CA3AF",
#             ),
#             margin_bottom=rx.breakpoints(
#                 {"0px": "1.5rem", "768px": "0"}
#             ),
#             width=rx.breakpoints(
#                 {"0px": "100%", "768px": "33.333333%"}
#             ),
#         ),
#         create_footer_quick_links(),
#         rx.box(
#             create_custom_heading(
#                 heading_type="h3",
#                 font_size="1.25rem",
#                 margin_bottom="1rem",
#                 heading_text="Connect",
#             ),
#             rx.flex(
#                 create_social_link(
#                     alt_text="Facebook", icon_tag="facebook"
#                 ),
#                 create_social_link(
#                     alt_text="Twitter", icon_tag="twitter"
#                 ),
#                 create_social_link(
#                     alt_text="Instagram",
#                     icon_tag="instagram",
#                 ),
#                 display="flex",
#                 column_gap="1rem",
#             ),
#             width=rx.breakpoints(
#                 {"0px": "100%", "768px": "33.333333%"}
#             ),
#         ),
#         display="flex",
#         flex_wrap="wrap",
#         justify_content="space-between",
#     )


# def create_footer():
#     """Create the complete footer with content and copyright notice."""
#     return rx.box(
#         create_footer_content(),
#         rx.box(
#             rx.text(
#                 "© 2023 Class Notes. All rights reserved."
#             ),
#             border_color="#374151",
#             border_top_width="1px",
#             margin_top="2rem",
#             padding_top="2rem",
#             text_align="center",
#             color="#9CA3AF",
#         ),
#         width="100%",
#         style=rx.breakpoints(
#             {
#                 "640px": {"max-width": "640px"},
#                 "768px": {"max-width": "768px"},
#                 "1024px": {"max-width": "1024px"},
#                 "1280px": {"max-width": "1280px"},
#                 "1536px": {"max-width": "1536px"},
#             }
#         ),
#         margin_left="auto",
#         margin_right="auto",
#         padding_left=rx.breakpoints(
#             {
#                 "0px": "1rem",
#                 "640px": "1.5rem",
#                 "1024px": "2rem",
#             }
#         ),
#         padding_right=rx.breakpoints(
#             {
#                 "0px": "1rem",
#                 "640px": "1.5rem",
#                 "1024px": "2rem",
#             }
#         ),
#         padding_top="2rem",
#         padding_bottom="2rem",
#     )


# def create_main_layout():
#     """Create the main layout of the application including header, content, and footer."""
#     return rx.box(
#         create_sticky_header(),
#         rx.box(
#             create_main_content(),
#             width="100%",
#             style=rx.breakpoints(
#                 {
#                     "640px": {"max-width": "640px"},
#                     "768px": {"max-width": "768px"},
#                     "1024px": {"max-width": "1024px"},
#                     "1280px": {"max-width": "1280px"},
#                     "1536px": {"max-width": "1536px"},
#                 }
#             ),
#             margin_left="auto",
#             margin_right="auto",
#             padding_left=rx.breakpoints(
#                 {
#                     "0px": "1rem",
#                     "640px": "1.5rem",
#                     "1024px": "2rem",
#                 }
#             ),
#             padding_right=rx.breakpoints(
#                 {
#                     "0px": "1rem",
#                     "640px": "1.5rem",
#                     "1024px": "2rem",
#                 }
#             ),
#             padding_top="2rem",
#             padding_bottom="2rem",
#         ),
#         rx.box(
#             create_footer(),
#             background_color="#1F2937",
#             margin_top="3rem",
#             color="#ffffff",
#         ),
#         class_name="font-['Poppins']",
#         background_color="#F9FAFB",
#     )


# def create_app():
#     """Create the complete application with necessary stylesheets and layout."""
#     return rx.fragment(
#         create_stylesheet_link(
#             stylesheet_url="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css"
#         ),
#         create_stylesheet_link(
#             stylesheet_url="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap"
#         ),
#         rx.el.style(
#             """
#         @font-face {
#             font-family: 'LucideIcons';
#             src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
#         }
#     """
#         ),
#         create_main_layout(),
#     )