#this file stores all the views and the end points of the web for the functioning aspect of our website

from flask import Blueprint, render_template            

#this line makes this specific file the blueprint of our website, meaning that it contains bunch of routes, URLs

views = Blueprint('views', __name__)

@views.route('/')           #called as decorator
def home():
    return render_template("home.html")