from flask import Flask, request
from app.db.database import Query

app = Flask(__name__)


@app.route('/api/health')
def health():
    return 'Ok'


@app.route('/api/')
def home():
    return 'Welcome to the Product Manager API'


@app.route('/api/products', methods=['GET'])
def get_products():
    data = Query("SELECT * FROM products").query()
    return data


if __name__ == '__main__':
    app.run(debug=True)
