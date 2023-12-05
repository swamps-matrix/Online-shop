from flask import render_template, request, redirect, url_for
from app import app, db
from models import Product, Order

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get(product_id)
    return render_template('product_detail.html', product=product)

# Add more routes and controllers as needed
