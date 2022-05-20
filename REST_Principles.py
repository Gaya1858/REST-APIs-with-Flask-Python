# What is rest api is?
# REST APis uses the same GET< pOST and so function
# >>>> It's a way of thinking about how a web server responds to your requests
# >>>> it doesn't respond with just data'
# >>>>It responds with resources'

# Resources????
# >>>> similar to object-orinted programming
# >>>> think of the server as having resources, and each is able to interact with the pertinent request

# Stateless???
# Another key feature is that REST is supposed to be stateless
# this means one request cannit depend on any other requests
#
# The server onky knows about the current request, and not any previous requests

# Exampl: POST/ item/chair - creates an item
# The server does not know the item exists
# GET/item.chair then goes to the daatabase and checks to see if the item is here
# To get an item you do not need to ahve created an item before-- the item could be in the database from previously

# another example:
# ****A user logs in to  the twitter web application
# **** The web server does not the user is logged in (since it is stateless)
# **** What do we do?
# **** The web applcation must send enough data to identity the user in every request, or else the server won't
#     associate the request with the user.


