from flask import Blueprint, render_template

admin = Blueprint("admin", __name__, static_folder="static", template_folder="templates")

@admin.route("/")
def index():
    return render_template("/admin/login.html")

@admin.route("crud")
def crud():
    return render_template("/admin/crud.html")