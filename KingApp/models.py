import reflex as rx

class Product(rx.Model, table=True):
    codi: int
    marca: str
    nom: str
    preu: float
    quantitat: int
 