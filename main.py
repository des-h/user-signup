from flask import Flask, request, redirect, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

# THESE ARE FUNCTIONS FOR THE VALIDATIONS

def empty_val(x):
    if x:
        return True
    else:
        return False

def char_length(x):
    if len(x) > 2 and len(x) < 21:
        return True
    else:
        return False

def email_at_symbol(x):
    if x.count('@') >= 1:
        return True
    else:
        return False

def email_at_symbol_more_than_one(x):
    if x.count('@') <= 1:
        return True
    else:
        return False

def email_period(x):
    if x.count('.') >= 1:
        return True
    else:
        return False

def email_period_more_than_one(x):
    if x.count('.') <= 1:
        return True
    else:
        return False

# THIS CREATES ROUTE TO PROCESS AND VALIDATE THE FORM

@app.route('/signup')
def display_user_signup_form():
    return render_template('index.html')

@app.route("/signup", methods=['POST'])
def user_signup_complete():

    # THIS CREATES VARIABLES FROM THE FORM INPUTS

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    # THIS CREATES EMPTY STRINGS FOR THE ERROR MESSAGES

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    # THESE ARE THE ERROR MESSAGES THAT OCCUR MORE THAN ONCE

    err_required = "Required field"
    err_reenter_pw = "Please re-enter password"
    err_char_count = "must be between 3 and 20 characters"
    err_no_spaces = "must not contain spaces"

    # THIS IS THE PASSWORD VALIDATION

    if not empty_val(password):
        password_error = err_required
        password = ''
        verify = ''
    elif not char_length(password):
        password_error = "Password " + err_char_count
        password = ''
        verify = ''
        verify_error = err_reenter_pw
    else:
        if " " in password:
            password_error = "Password " + err_no_spaces
            password = ''
            verify = ''
            verify_error = err_reenter_pw

    # THIS IS THE SECOND PASSWORD VALIDATION

    if verify != password:
        verify_error = "Passwords must match"
        password = ''
        verify = ''
        password_error = 'Passwords must match'
            

    # THIS IS THE USERNAME VALIDATION

    if not empty_val(username):
        username_error = err_required
        password = ''
        verify = ''
        password_error = err_reenter_pw
        verify_error = err_reenter_pw
    elif not char_length(username):
        username_error = "Username " + err_char_count
        password = ''
        verify = ''
        password_error = err_reenter_pw
        verify_error = err_reenter_pw
    else:
        if " " in username:
            username_error = "Username " + err_no_spaces
            password = ''
            verify = ''
            password_error = err_reenter_pw
            verify_error = err_reenter_pw

    # THIS IS THE EMAIL VALIDATION

    # checks to see if email contains text prior to running validations
    if empty_val(email):
        # validations start here
        if not char_length(email):
            email_error = "Email " + err_char_count
            password = ''
            verify = ''
            password_error = err_reenter_pw
            verify_error = err_reenter_pw
        elif not email_at_symbol(email):
            email_error = "Email must contain the @ symbol"
            password = ''
            verify = ''
            password_error = err_reenter_pw
            verify_error = err_reenter_pw
        elif not email_at_symbol_more_than_one(email):
            email_error = "Email must contain only one @ symbol"
            password = ''
            verify = ''
            password_error = err_reenter_pw
            verify_error = err_reenter_pw
        elif not email_period(email):
            email_error = "Email must contain ."
            password = ''
            verify = ''
            password_error = err_reenter_pw
            verify_error = err_reenter_pw
        elif not email_period_more_than_one(email):
            email_error = "Email must contain only one ."
            password = ''
            verify = ''
            password_error = err_reenter_pw
            verify_error = err_reenter_pw
        else:
            if " " in email:
                email_error = "Email " + err_no_spaces
                password = ''
                verify = ''
                password_error = err_reenter_pw
                verify_error = err_reenter_pw

    # IF THERE ARE NO ERRORS, THIS WILL REDIRECT TO WELCOME.HTML
    # IF THERE ARE ERRORS, THIS WILL STAY ON THE MAIN.HTML (FORM) AND DISPLAY THE ERROR MSGS

    if not username_error and not password_error and not verify_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('index.html', username_error=username_error, username=username, password_error=password_error, password=password, verify_error=verify_error, verify=verify, email_error=email_error, email=email)

# THIS REDIRECTS TO A WELCOME PAGE

@app.route('/welcome')
def valid_signup():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)


app.run()