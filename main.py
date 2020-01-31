from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


# @app.route('/hello', methods=['GET'])
# def hello_name():
#     my_name = request.args['name']
#     return 'Hello' + my_name + '.'


# @app.route('/json', methods=['GET'])
# def json():
#     dict = {'some variable': 'something'}
#     return jsonify(dict)

if __name__=='__main__':
    app.run(debug=True, host='localhost', port=8080)
