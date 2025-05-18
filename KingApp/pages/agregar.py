import reflex as rx
from rxconfig import config
from ..controllers.afegir_state import afegirState

def form_add_product():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.heading("Añadir Producto",color="gray"),
                rx.input(
                    placeholder="Codigo",
                    name="codi_product",
                    style={"padding": "5px", "border": "1px solid #ccc", "border-radius": "5px", "margin-bottom": "10px"}
                ),
                rx.input(
                    placeholder="Marca",
                    name="marca_product",
                    style={"padding": "8px", "border": "1px solid #ccc", "border-radius": "5px", "margin-bottom": "10px"}
                ),
                rx.input(
                    placeholder="Modelo",
                    name="nom_product",
                    style={"padding": "8px", "border": "1px solid #ccc", "border-radius": "5px", "margin-bottom": "10px"}
                ),
                rx.input(
                    placeholder="Precio",
                    name="preu_product",
                    style={"padding": "8px", "border": "1px solid #ccc", "border-radius": "5px", "margin-bottom": "10px"}
                ),
                rx.input(
                    placeholder="Cantidad",
                    name="quantitat_product",
                    style={"padding": "8px", "border": "1px solid #ccc", "border-radius": "5px", "margin-bottom": "10px"}
                ),
                rx.button(
                    "Añadir",
                    type="submit",
                    style={
                        "background-color": "gray",
                        "color": "white",
                        "padding": "10px 15px",
                        "border": "none",
                        "border-radius": "5px",
                        "cursor": "pointer",
                        "transition": "background-color 0.3s"
                    },
                    _hover={"background-color": "darkcyan"},
                    on_click=rx.toast("Producto Añadido!"),
                    
                ),
            ),
            on_submit=afegirState.handle_submit,
            reset_on_submit=True,
            
            style={
                "background-color": "#f9f9f9",
                "padding": "20px",
                "border-radius": "10px",
                "box-shadow": "0 2px 10px rgba(0,0,0,0.1)"
            }
        )
    )


def agregar_item() -> rx.Component:
    return rx.container(
        rx.vstack(
            form_add_product(),
            align="center",
            style={
                "min-height": "100vh",
                "width": "100%",
                "height": "100vh",
                "padding": "40px"
            },
        ),
        align="center",
        style={
            "background-color": "gray",  # Fondo gris para toda la página
            "min-height": "100vh",
            "width": "100vw",
        }
    )