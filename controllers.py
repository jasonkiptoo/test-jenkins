from models import db, Product

class ProductController:
    @staticmethod
    def get_all_products():
        return Product.query.all()

    @staticmethod
    def add_product(name, price):
        new_product = Product(name=name, price=price)
        db.session.add(new_product)
        db.session.commit()
        
    @staticmethod
    def delete_product(product_id):
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()