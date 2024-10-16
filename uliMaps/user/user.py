from flask import Blueprint, render_template

user = Blueprint("user", __name__, static_folder="static", template_folder="templates")

@user.route("/")
def index():
    return render_template("usuario/index.html")