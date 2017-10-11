'''Simple Flask app

To run, execute the following

    export FLASK_APP=<path to this file>
    flask run

'''

from fizzbuzz_funcs import fizzbuzz_reg
from flask import Flask, request

app = Flask(__name__) # instantiate the flask app

@app.route('/fizzbuzz_basic') # define the endpoint
def fizzbuzz_basic(): # does not need to match endpoint name, but makes it more readable if it does
    fizzbuzz_list = fizzbuzz_reg()
    return str(fizzbuzz_list) # flask requires str as output for endpoint methods

@app.route('/fizzbuzz_pro')
def fizzbuzz_pro():
    start = request.args['start']
    end = request.args['end']
    return str(fizzbuzz_reg(int(start),int(end)))

if __name__ == '__main__':
    app.run()
