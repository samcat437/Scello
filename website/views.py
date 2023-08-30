from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/weddings')
def weddings():
    return render_template("weddings.html")


@views.route('/teaching')
def teaching():
    return render_template("teaching.html")


@views.route('/contact')
def contact():
    return render_template("contact.html")