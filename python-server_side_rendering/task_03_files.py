#!/usr/bin/activate
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json') as f:
        data = json.load(f)
    items = data.get('items', [])
    return render_template('items.html', items=items)


def read_json(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data

def read_csv(file_path):
    products = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        products = read_json('products.json')
    else:
        products = read_csv('products.csv')

    if product_id:
        product = next((p for p in products if str(p['id']) == product_id), None)
        if product:
            products = [product]
        else:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
       app.run(debug=True, port=5000)