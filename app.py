from flask import Flask, render_template, request, redirect, url_for
from models import db, Product
from controllers import ProductController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    products = ProductController.get_all_products()
    return render_template('index.html', products=products)

@app.route('/add', methods=['POST'])
def add_product():
    name = request.form.get('name')
    price = float(request.form.get('price'))
    ProductController.add_product(name, price)
    return redirect(url_for('index'))

@app.route('/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    ProductController.delete_product(product_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
