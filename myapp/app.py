from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def ping():
    return "server is alive"

if __name__ == "__main__" : 
    app.run()
