from flask import Blueprint, render_template, request, flash             
#this line makes this specific file the blueprint of our website, meaning that it contains bunch of routes, URLs

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", text = "Testing")

@auth.route('/logout')
def logout():
    return "<p>Logout<p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email)<4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName)<2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1!=password2:
            flash('Password don\'t match.', category='error')
        elif len(password1)<7:
            flash('Password must be atleast 7 characters', category='error')
        else:
            #add user to the database
            flash('Account created!', category='success')


    return render_template("sign_up.html")