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
    </head>
    <body>
     <h1>Signup</h1>
     <form method="post">
      <table>
       <tbody>
        <tr>
         <td>
          <label for="username">Username</label>  
         </td>
         <td>
          <input name="usenname" type="text" value="">
          <span class="error"></span>
         </td>
         </tr>
         <td>
           <input name="password" type="password">
           <span class="error"></span>
        </td>
        </tr>
        <tr>
        <td>
         <label for="verify" type="password">
         <span class="error"></span>
         </td>
         </tr>
         <tr>
          <td>
          <label for="email">Email(optional)</label>
          </td>
          <td>
            <input name="email" value="">
            <span class="error"></span>
           </td>
           </tr>
           </tbody>
           </table>
           <input type="submit">
           </form>
           </body>
           </html>"""


@app.route("/")
def index():
    return form
@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, ' + first_name +'</h1>'  
app.run()  