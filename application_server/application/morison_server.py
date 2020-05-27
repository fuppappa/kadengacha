from flask import request, redirect, url_for, render_template, flash
from application import app, db
from application.models import Product
import random
import time

from PIL import Image
import qrcode as qr
import base64
from io import BytesIO


@app.route('/load1')
def load():
    return render_template("loading.html")


@app.route('/test2')
def test2():
    user_budget = request.args.get('budget')
    products = []
    message = "あなたの買うべき物を探しました！" + "\n" + "\n"
    budget = 100000
    category = ""

    if user_budget:
        budget = int(user_budget)
    money = budget

    if budget < 10000 or budget > 100000:
        error = Product()
        error.name = "予算が10万円以内でありません"

        return render_template("index.html", products=[error], budget=100000)

    while not products:
        rand = random.randrange(0, db.session.query(Product.id).count())
        products = db.session.query(Product).filter(Product.id == rand, Product.price <= budget).all()

    budget -= int(products[0].price)

    while budget > 0:
        candidate = db.session.query(Product).filter(Product.price <= budget).all()

        if not candidate:
            break

        product = random.choice(candidate)

        products.append(product)

        budget -= int(product.price)

    return render_template("index.html", products=products, budget=budget)


@app.route('/test')
def test():
    products = []
    message = "あなたの買うべき物を探しました！" + "\n" + "\n"
    budget = 5000
    money = budget
    category = ""

    while not products:
        rand = random.randrange(0, db.session.query(Product.id).count())
        products = db.session.query(Product).filter(Product.id == rand, Product.price <= budget).all()

    budget -= int(products[0].price)

    while budget > 0:
        candidate = db.session.query(Product).filter(Product.price <= budget).all()

        if not candidate:
            break

        product = random.choice(candidate)

        products.append(product)

        budget -= int(product.price)

    return render_template("test.html", products=products)


@app.route('/')
def show_entries():
    return render_template("index.html")


@app.route('/take', methods=['GET'])
def add_entry():
    products = []
    message = "あなたの買うべき物を探しました！" + "\n" + "\n"
    budget = 100000
    money = budget
    category = ""

    while not products:
        rand = random.randrange(0, db.session.query(Product.id).count())
        products = db.session.query(Product).filter(Product.id == rand, Product.price <= budget).all()

    budget -= int(products[0].price)

    while budget > 0:
        candidate = db.session.query(Product).filter(Product.price <= budget).all()

        if not candidate:
            break

        product = random.choice(candidate)

        products.append(product)

        budget -= int(product.price)

    return render_template("index.html", products=products)
