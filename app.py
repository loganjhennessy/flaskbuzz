'''Simple Flask app

To run, execute the following

    export FLASK_APP=<path to this file>
    flask run

'''

from flaskbuzz_funcs import flaskbuzz_reg
from flask import Flask, request

app = Flask(__name__) # instantiate the flask app

@app.route('/flaskbuzz_basic') # define the endpoint
def flaskbuzz_basic(): 
    '''The method name does not need to match endpoint name, but makes
    it more readable if it does.

    To access it, go to <ip>/flaskbuzz_basic

    Where <ip> is the ip that your flask app is running on
    '''
    flaskbuzz_list = flaskbuzz_reg()
    return str(flaskbuzz_list) # flask requires str as output for endpoint methods

@app.route('/flaskbuzz_pro')
def flaskbuzz_pro():
    '''To access this, go to

    <ip>/flaskbuzz_basic?start=<int>&end=<int>

    Wehre <ipp> is the ip that your flask app is running on
    '''
    start = request.args['start']
    end = request.args['end']
    return str(flaskbuzz_reg(int(start),int(end)))

if __name__ == '__main__':
    app.run()
