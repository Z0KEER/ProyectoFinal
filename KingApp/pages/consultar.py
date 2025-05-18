import reflex as rx
from rxconfig import config
from ..controllers.consultar_state import ConsultarState

def consultar_product():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.heading("Consultar Producto",color="gray"),
                rx.input(
                    value=ConsultarState.actual_product.codi,
                    placeholder="Codigo",
                    name="codi_product",
                    style={"padding": "8px", "border": "1px solid #ccc", "border-radius": "5px", "margin-bottom": "10px"},
                    on_change=ConsultarState.update_codi
                ),
                rx.input(
                    value=ConsultarState.actual_product.marca,
                    placeholder="Marca",
                    name="nom_product",
                    style={"padding": "8px", "border": "1px solid #ccc", "border-radius": "5px", "margin-bottom": "10px"},
                    on_change=ConsultarState.update_marca
                ),
                rx.input(
                    value=ConsultarState.actual_product.nom,
                    placeholder="Modelo",
                    name="nom_product",
                    style={"padding": "8px", "border": "1px solid #ccc", "border-radius": "5px", "margin-bottom": "10px"},
                    on_change=ConsultarState.update_nom

                ),
                rx.input(
                    value=ConsultarState.actual_product.preu,
                    placeholder="Precio",
                    name="preu_product",
                    style={"padding": "8px", "border": "1px solid #ccc", "border-radius": "5px", "margin-bottom": "10px"},
                    on_change=ConsultarState.update_preu
                ),
                rx.input(
                    value=ConsultarState.actual_product.quantitat,
                    placeholder="Cantidad",
                    name="quantitat_product",
                    style={"padding": "8px", "border": "1px solid #ccc", "border-radius": "5px", "margin-bottom": "10px"},
                    on_change=ConsultarState.update_quantitat
                ),
        
                rx.button(
                    "Actualizar",
                    type="button",
                    style={
                        "background-color": "teal",
                        "color": "white",
                        "padding": "10px 15px",
                        "border": "none",
                        "border-radius": "5px",
                        "cursor": "pointer",
                        "transition": "background-color 0.3s",
                    },
                    _hover={"background-color": "darkcyan"},
                     on_click=[
                        ConsultarState.handle_submit,  # Acción principal
                        rx.toast("Producto Actualizado!"),  # Mensaje de confirmación
                    ],
                    
                ),
                rx.button(
                    "Eliminar",
                    type="button",  
                    style={
                        "background-color": "red",
                        "color": "white",
                        "padding": "10px 15px",
                        "border": "none",
                        "border-radius": "5px",
                        "cursor": "pointer",
                        "transition": "background-color 0.3s",
                    },
                    _hover={"background-color": "darkred"},
                    on_click=[
                        ConsultarState.handle_delete,  # Acción principal
                        rx.toast("Producto Borrado!"),  # Mensaje de confirmación
                    ],
                    
                    
                ),
            ),
            on_submit=ConsultarState.handle_submit,
            reset_on_submit=True,
            style={
                "background-color": "#f9f9f9",
                "padding": "20px",
                "border-radius": "10px",
                "box-shadow": "0 2px 10px rgba(0,0,0,0.1)"
            },
        )
    )

def consultar_item()  -> rx.Component:
    return rx.container( 
        rx.vstack(
            consultar_product(),
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