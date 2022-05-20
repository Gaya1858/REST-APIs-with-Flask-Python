from flask import Flask, jsonify, request,render_template

# create an app for the flask
app = Flask(__name__)  # __name__ is a special name variable . Flask object with unique name
stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My item',
                'price': 12.99
            }
        ]
    }
]
@app.route('/')
def home():
    return render_template('index.html')

# server's perspective
# POST to receive data
# GET  used to send data back only

# Browser's perspective
# POST to send us (server)data
# GET to receive data from us(server)

# POST/ store data  ----- creates new store with the given name
# @app.route('/store') # by default is a get request so we have to add method =[POST]
@app.route('/store', methods=['POST'])
def creat_store():
    request_data = request.get_json() # request is made to this endpoint, browser
                                      # also send us json data f store
    new_store ={'name': request_data['name'],
                'items': []}
    stores.append(new_store)
    return jsonify(new_store)



# GET/store/<string:name> ---- gets the store name and returns some data baout it
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})



# GET/ store ----- to return list of all the stores
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})  # it converts a stores in json format


# POST/ store/<string:name>/item ---- to create an item inside a specific store with the given name(name; price)
@app.route('/store/<string:name>/item', methods=['POST'])
def create_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
           new_item ={'name': request_data['name'],
                      'price': request_data['price']
                      }
           store['items'].append(new_item)
           return jsonify(new_item)
    return jsonify({'message':'store not found'})




# GET/store/<string:name>/item ---- to get all the items from a given specific store
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message':' store not found'})
    pass


app.run(port=4999)
# how to call api