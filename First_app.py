from flask import Flask

# create an app for the flask
app = Flask(__name__) # __name__ is a special name variable . Flask object with unique name

# what request it is going to understand, like hello.html, or user3
@app.route('/') # '/'  means this is the home page of the site ex : 'https://www.google.com/'
def home():
    return "helloe, World!"

app.run(port=5000) # to run the app. port is just a area of the computer that recciving your requests

# server's perspective
    # POST to receive data
    # GET  used to send data back only

# Browser's perspective
    # POST to send us (server)data
    # GET to receive data from us(server)

# POST/ store data  ----- creates new store with the given name

# GET/store/<string:name> ---- gets the store name and returns some data baout it
# GET/ store ----- to return list of all the stores
# POST/ store/<string:name>/item ---- to create an item inside a specific store with the given name(name; price)
# GET/store/<string:name>/item ---- to get all the items from a given specific store

