#HTTP verbs
# one of the most popular protocol
#
# what is the web server?
#     piece of computer, piece of software, a piece software designed to accept incoming web requests

# what we send to the web server when we connect with web page, the server receives below request for google
#     Get / HTTP /1.1  --- / is a path GET is the verb HTTP is a protocol
#     Host: www.google.com  , this is A GET REQUEST

# What it sends back?
#
# *** it may give you an error, if / is not found
# *** it may give an error, it HTTP is not supported
# *** it may give an error, if the server is unavailabel
# *** it may give HTML code back (which is what it normally does)
# *** it may give you some text back
# *** it may give you nothing back

# What else?
# >>> going to any page in your browser will do the same
#     for example for twitter page
#         GET/login HTTP/1.1
#         Host: https://twitter.com
# >>>> going to the web page always do a GET
# >>>> but there are many other things we can do , such as POST, DELETE, PUT, OPTIONS, HEAD and much more
# >>>> Each server responds differently to each, but they normally have the same meaning in each

# HTTP Verbs
# VERB    Meaning                     Examples
# GET     Retrieve something          GET/item/1
# POST    Receive data, and use it    POST/item
# PUT     Make something is there     PUT/item
# DELETE  Remove something            DELETE/item/1