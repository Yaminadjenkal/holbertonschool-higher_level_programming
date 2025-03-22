#!/usr/bin/activate
from flask import Flask, render_template, request
import json
import csv
import sqlite3

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

def read_sqlite():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        products = cursor.fetchall()
        conn.close()

        return [{"id": product[0], "name": product[1], "category": product[2], "price": product[3]} for product in products]
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return None
    
def create_database():
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        cursor.execute('SELECT id FROM Products')
        existing_ids = [row[0] for row in cursor.fetchall()]

        products_to_insert = [
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ]
    
        for product in products_to_insert:
            if product[0] not in existing_ids:
                cursor.execute('''
                    INSERT INTO Products (id, name, category, price)
                    VALUES (?, ?, ?, ?)
                ''', product)

        conn.commit()
        conn.close()

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    elif source == 'sql':
        products = read_sqlite()

    if product_id:
        products = [product for product in products if str(product['id']) == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
       create_database()
       app.run(debug=True, port=5000)