from flask import Flask, render_template, request
import cont_products

app = Flask(__name__)

@app.route('/')
def main():
    titulo = 'Inicio'
    return render_template('auth/login.html', titulo = titulo)

@app.route('/products/index.html', methods=['GET','POST'])
def index_products():
    titulo = 'Productos'
    return render_template('products/index.html', titulo = titulo)

@app.route('/add_product/', methods=['GET','POST'])
def add_product():
    titulo = 'Agregar producto'
    if request.method == 'POST':
        id = request.form['id_product']
        name = request.form['name_product']
        price = request.form['price_product']
        description = request.form['description_product']
        cont_products.add_prod(id, name, price, description)
    
    return render_template('products/add_product.html', titulo = titulo)

@app.route('/list_product/', methods=['GET', 'POST'])
def list_product():
    titulo = 'Lista productos'
    products = cont_products.list_prod()
    return render_template('products/list_product.html', titulo = titulo, products = products)