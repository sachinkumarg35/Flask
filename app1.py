#Building url dynamically
#Variable Rules and URL Building

from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my study place"

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the marks is " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the marks is " + str(score)

#Result Checker
@app.route('/results/<int:score>')
def results(score):
    result = ""
    if score < 50:
        result = "Fail"
    else:
        result = "Success"
    return result

if __name__ == '__main__':
    app.run(debug = True) 