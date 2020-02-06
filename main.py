from eparser import process_data, format_url
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    itemCondition = {'new': 2000, 'open': 7000, 'manufacturer': 3000, 'seller': 1500, 'used': 1000, 'parts': 2500}
    product = request.form["product"]
    priceLow = request.form["price-min"]
    priceHigh = request.form["price-max"]
    condition = request.form["condition"]
    status = request.form["status"]
    if status == 'Active':
        sold = 1
        comp = 1
    else:
        sold = 0
        comp = 0
    if __name__ == '__main__':
        data = process_data(format_url(product, sold, comp, priceLow, priceHigh, itemCondition.get(condition, '')))
    return render_template('search.html', data=data, name=product.title())


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)
