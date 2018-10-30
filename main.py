from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True

form="""
<!DOCTYPE html>
<html>
   <head>
    <style>
    .error {color: red;}
    </style>   






@app.route("/")
def index():
    return form
@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, ' + first_name +'</h1>'  
app.run()  