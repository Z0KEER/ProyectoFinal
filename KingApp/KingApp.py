"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
from rxconfig import config
from .components.sidebar import sidebar_bottom_profile
from .pages.principal import center_container
from .pages.agregar import agregar_item
from .pages.consultar import ConsultarState
from .pages.mostrar import mostrar_lista
from .pages.consultar import consultar_item
from .controllers import LlistaState
from .controllers import ConsultarState

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.hstack (
        sidebar_bottom_profile(),
        center_container()
    )

def prova()  -> rx.Component:
     return rx.hstack( 
        sidebar_bottom_profile(),
        )

def mostrar()  -> rx.Component:
     return rx.hstack( 
        sidebar_bottom_profile(),
        mostrar_lista(),
        )

def agregar()  -> rx.Component:
     return rx.hstack( 
        sidebar_bottom_profile(),
        agregar_item(),
        )


def consultar() -> rx.Component:
     return rx.hstack( 
        sidebar_bottom_profile(),
        consultar_item(),
        )

app = rx.App()
app.add_page(index)
app.add_page(prova, route="/1")
app.add_page(agregar, route="/2")
app.add_page(mostrar, route="/3", on_load=LlistaState.get_products)
app.add_page(consultar, route="consultar/[codi]", on_load=ConsultarState.get_product)

