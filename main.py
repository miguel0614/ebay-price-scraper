from eparser import process_data, format_url
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = str
    response = str
    return response


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)
