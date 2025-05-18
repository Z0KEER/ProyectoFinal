import reflex as rx 
from ..models import Product

class ConsultarState(rx.State):

    form_data: dict = {}
    actual_product: Product = None

    @rx.var
    def get_codi(self) -> str:
        return self.router.page.params.get("codi")
    
    @rx.event
    def update_codi(self, value):
        self.actual_product.codi = value
    @rx.event
    def update_marca(self, value):
        self.actual_product.marca = value  
    @rx.event
    def update_nom(self, value):
        self.actual_product.nom = value

    @rx.event
    def update_preu(self, value):
        self.actual_product.preu = value
    @rx.event
    def update_quantitat(self, value):
        self.actual_product.quantitat = value
    
    
    @rx.event
    def get_product(self):
        with rx.session() as session:
            self.actual_product = session.exec(
                Product.select().where(
                    Product.id == int(self.get_codi)
                )
            ).one_or_none()

    @rx.event
    def handle_delete(self):
        with rx.session() as session:
            actual_product = session.exec(
                Product.select().where(
                    Product.id == int(self.get_codi)
                )
            ).one_or_none()
            session.delete(actual_product)
            session.commit()
        return rx.redirect("/3")

    @rx.event
    def handle_submit(self):
        """Handle the form submit."""
        with rx.session() as session:
            actual_product = session.exec(
                Product.select().where(
                    Product.id == int(self.get_codi)
                )
            ).one_or_none()

            actual_product.codi= self.actual_product.codi
            actual_product.marca= self.actual_product.marca
            actual_product.nom= self.actual_product.nom
            actual_product.preu= self.actual_product.preu
            actual_product.quantitat= self.actual_product.quantitat
            session.add(actual_product)
            session.commit()
  
        return rx.redirect("/3")
    