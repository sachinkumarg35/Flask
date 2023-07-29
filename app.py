from flask import Flask
### WSGI Application

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my house. Please once you visit house"

@app.route('/members')
def house():
    return "Then you will have more opportunities"

if __name__ == '__main__':
    app.run(debug=True)