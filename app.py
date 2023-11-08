"""Module for processing requests"""

from flask import Flask, request, render_template
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)
# redis = Redis(host='127.0.0.1', port=6379)


@app.route("/", methods=['GET'])
def main_form():
    """Function for processing GET requests"""
    return render_template('index.html')


@app.route("/", methods=['POST'])
def post_form():
    """Function for processing POST requests"""
    print('form: ', request.form)
    if request.form['method'] == 'ADD':
        if not request.form['key'] or not request.form['value']:
            return render_template('index.html', add_context="You need enter key and value!")
        key = request.form['key']
        value = request.form['value']
        redis.set(key, value)
        return render_template('index.html', add_context="The pair added successfully!")

    if request.form['method'] == 'GET':
        key = request.form['key']
        response = redis.get(key)
        if not response:
            return render_template('index.html', get_context="The key is not exist!")
        response = str(response, 'utf-8')
        return render_template('index.html', get_context=f"The value is {response}")

    if request.form['method'] == 'UPDATE':
        if not request.form['key'] or not request.form['value']:
            return render_template('index.html', update_context="You need enter key and value!")
        key = request.form['key']
        value = request.form['value']
        redis.set(key, value)
        return render_template('index.html', update_context="The pair updated successfully!")

    # return print("Unknown request method!")


@app.route("/", methods=['PUT'])
def put_form():
    """Function for processing PUT requests"""
    if not request.form['key'] or not request.form['value']:
        return render_template('index.html', update_context="You need enter key and value!")
    key = request.form['key']
    value = request.form['value']
    redis.set(key, value)
    return render_template('index.html', update_context="The pair updated successfully!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
