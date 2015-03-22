from app import app
'''
imports the app variable from our app package and invokes its run method
the app variable holds the Flask instance
'''
app.run(host = "127.0.0.1", port = 5000, debug = True)
# only use when test on your own computer
