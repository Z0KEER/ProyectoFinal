import reflex as rx

def sidebar_item(
    text: str, icon: str, href: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, color=rx.color("gray")),
            rx.text(text, size="4", color=rx.color("gray")),  # Texto gris
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Añadir Producto", "clipboard-pen-line", "/2"),
        sidebar_item("Mostrar productos", "book-open-text", "/3"),
        spacing="1",
        width="100%",
    )


def sidebar_bottom_profile() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.hstack(
                    rx.image(
                        src="/snkrs.png",
                        width="3.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Sneakers",
                        size="6",  # Más grande
                        weight="bold",
                        color="linear-gradient(90deg, #ff0000, #ffffff, #000000)",  # Degradado rojo-blanco-negro
                        style={
                            "fontFamily": "'Montserrat', 'Arial', sans-serif",
                            "textShadow": "2px 2px 8px #00000055",
                            "background": "linear-gradient(90deg, #ff0000, #ffffff, #000000)",
                            "WebkitBackgroundClip": "text",
                            "WebkitTextFillColor": "transparent",
                            "letterSpacing": "0.08em",
                            "fontWeight": "900",
                        },
                    ),
                    align="center",
                    justify="start",
                    padding_x="0.5rem",
                    width="100%",
                ),
                sidebar_items(),
                rx.spacer(),
                rx.vstack(
                    rx.vstack(
                        
                        sidebar_item(
                            "Principal", "house", "/"
                        ),
                        spacing="1",
                        width="100%",
                    ),
                    rx.divider(),
                    rx.hstack(
                        
                            rx.image(
                                src="/llados.png",      # Cambia la ruta por la de tu imagen/avatar
                                width="2em",
                                height="2em",
                                border_radius="50%",    # Hace la imagen circular
                                margin_right="0.75em",
                            ),
                        rx.vstack(
                            rx.box(
                                rx.text(
                                    "Mi cuenta",
                                    size="3",
                                    weight="bold",
                                    color=rx.color("gray")
                                ),
                                rx.text(
                                    "llados@fitness.com",
                                    size="2",
                                    weight="medium",
                                    color=rx.color("gray")
                                ),
                                width="100%",
                            ),
                            spacing="0",
                            align="start",
                            justify="start",
                            width="100%",
                        ),
                        padding_x="0.5rem",
                        align="center",
                        justify="start",
                        width="100%",
                    ),
                    width="100%",
                    spacing="5",
                ),
                spacing="5",
                position="fixed",
                padding_x="1em",
                padding_y="1.5em",
                bg="black",  # Fondo negro del sidebar
                align="start",
                height="100%",
                width="16em",
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon("align-justify", size=30, color=rx.color("gray"))
                ),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(
                                    rx.icon("x", size=30, color=rx.color("gray"))
                                ),
                                width="100%",
                            ),
                            sidebar_items(),
                            rx.spacer(),
                            rx.vstack(
                            
                                rx.divider(margin="0"),
                                rx.hstack(
                                    rx.image(
                                        src="/llados.png",      # Cambia la ruta por la de tu imagen/avatar
                                        width="2em",
                                        height="2em",
                                        border_radius="50%",    # Hace la imagen circular
                                        margin_right="0.75em",
                                    ),
                                    rx.vstack(
                                        rx.box(
                                            rx.text(
                                                "Mi cuenta",
                                                size="3",
                                                weight="bold",
                                                color=rx.color("gray")
                                            ),
                                            rx.text(
                                                "llados@fitness.com",
                                                size="2",
                                                weight="medium",
                                                color=rx.color("gray")
                                            ),
                                            width="100%",
                                        ),
                                        spacing="0",
                                        justify="start",
                                        width="100%",
                                    ),
                                    padding_x="0.5rem",
                                    align="center",
                                    justify="start",
                                    width="100%",
                                ),
                                width="100%",
                                spacing="5",
                            ),
                            spacing="5",
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1.5em",
                        bg="black",  # Fondo negro drawer mobile
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
        ),
    )