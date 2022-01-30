from flask import Flask
from flask_caching import Cache 

from random import randint 

from time import sleep
from pickle import loads, dumps

cache = Cache()


app = Flask(__name__)

app.config['CACHE_TYPE'] = 'simple'

cache.init_app(app)

stored_object = [{1,2,3}, {'a':1,'b':2,'c':3}, ['foo', 'bar']]

# store
cache.set('obj', dumps(stored_object))


# the calculation is cached for 5 seconds
@app.route('/')
@cache.cached(timeout=5)
def index():
    # if form.method==post:
        # take the different dropdown values and create a unique object string you can put in key value in set function below like (dropdown1=hcs,dropdown2=ivs) so hcs,ivs thens store this as key 
        # then get data from database 
        # format it into json format and put it into set like below in dumps..
        # now take unique string from dropdown parameters as key and json form of data as object. 
        # this allows users to cache different views from database
        # if this key does not exist then do set.. 
    cache.set('obj', dumps(stored_object))

    # if the key does exist then get... 
    retrieved_object = loads(cache.get('obj'))

    # compare
    print(stored_object==retrieved_object, '\n', stored_object, '\n', retrieved_object)

    # Then format the json data into row format to look like dataframe (use personal github refrence for javascript apex charts, plotly js or charts.js.)
    return f'<h1>The object is: {retrieved_object}</h1>'

if __name__ == "__main__":
    app.run(debug=True)