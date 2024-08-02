from flask import Flask, render_template, make_response, jsonify, Response, redirect, url_for
from markupsafe import Markup

app = Flask(__name__, template_folder="templates", static_folder="static") # to create an instance of flask application(i.e. web application)

# When a module is run directly, __name__ is set to '__main__'. When it is imported, __name__ is set to the module's name.
# by passing  __name__ to Flask class, we are telling flask to use current module as directory of current application

# string in Body tag
@app.route("/")
def helloabcd():
    return "Hello World"

@app.route("/response_hello")
def response_hello():
    return Response("hello world response")

#rendering HTML    
@app.route("/markup_hello")
def markup_hello():
    return Markup("<h1>hello world</h1>")

@app.route("/render_hello")
def render_hello():
    return render_template("render_hello.html")

#json response
@app.route("/makeresponse_hello")
def makeresponse_hello():
    headers= {"Content-Type": "application/json"}
    return make_response({"msg":"hello world makeresponse!"}, 200, headers)

@app.route("/return_hello")
def return_hello():
    return {"msg":"hello world return!"}

@app.route("/jsonify_hello")
def jsonify_hello():
    return jsonify(msg = "hello world jsonify")

#to redirect
@app.route("/redirect_hello")
def redirect_hello():
    return redirect(url_for('helloabcd'))


'''
@app.route("string_hello")
def string_hello():
    return "Hellow"
'''


if __name__ == "__main__":
    app.run()
# to ensure that flask application only runs when this script is run directly, not when its imported. Keeps behaviour of script modular
