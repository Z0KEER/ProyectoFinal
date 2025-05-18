import reflex as rx
from rxconfig import config
from ..controllers.mostrar_state import LlistaState
from ..models import Product

def show_product(product: Product):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(rx.link(product.codi, href=(f"consultar/{product.id}"))),
        rx.table.cell(product.marca),
        rx.table.cell(product.nom),
        rx.table.cell(product.preu),
        rx.table.cell(product.quantitat),
    )


def foreach_table_example():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Codi"),
                rx.table.column_header_cell("Marca"),
                rx.table.column_header_cell("Modelo"),
                rx.table.column_header_cell("Preu"),
                rx.table.column_header_cell("Quantitat"),
            ),
        ),
        rx.table.body(
            rx.foreach(LlistaState.products, show_product)
        ),
        width="100%",
    )

def mostrar_lista() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Sidebar
            rx.box(
                "Sidebar content here",  # Reemplaza con el contenido del sidebar
                width="20%",  # Ajusta el ancho del sidebar
                  # Fondo blanco para el sidebar
                padding="4",
            ),
            # Main content
            rx.box(
                foreach_table_example(),
                background_color="gray",  # Fondo gris claro para el contenido principal
                padding="4",
                border_radius="md",
                width="100%",  # Ajusta el ancho del contenido principal
            ),
        ),
        width="100%",  # Asegura que ocupe todo el ancho de la página
        height="100vh",  # Asegura que ocupe toda la altura de la página
        background_color="gray",  # Fondo gris claro para toda la página
    )