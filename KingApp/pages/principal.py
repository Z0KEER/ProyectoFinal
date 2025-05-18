import reflex as rx
from rxconfig import config


def center_container() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Sneaker Vault", 
                size="9",
                style={
                    "background": "linear-gradient(90deg, #ff0000, #ffffff, #000000)",
                    "WebkitBackgroundClip": "text",
                    "WebkitTextFillColor": "transparent",
                    "fontWeight": "bold",
                    "fontFamily": "'Montserrat', 'Arial', sans-serif",
                    "textShadow": "2px 2px 8px #00000055",
                },
                       
                       ),
            rx.text(
                "Your ultimate hub for sneaker enthusiasts. Organize, track, and showcase your kicks!",
                font_size="lg",
                color="gray.700",
                text_align="center",
            ),

            rx.image(
                src="/snkrs.png",
                width="15em",
                height="auto",
                border_radius="25%",
            ),
            # rx.button(
            #     "Discover Collection",
            #     color_scheme="orange",
            #     size="lg",
            #     border_radius="full",
            #     box_shadow="lg",
            #     on_click=lambda: print("Navigating to sneaker collection..."),
            # ),
            rx.text(
                "👟 Keep your sneaker game strong!",
                font_size="md",
                color="gray.500",
                text_align="center",
                margin_top="4",
            ),
            spacing="6",
            justify="center",
            align="center",
            min_height="100vh",
            
        ),
        rx.logo(),
        background_color="gray",
    )