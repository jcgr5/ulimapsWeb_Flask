from flask import Flask, render_template, request, redirect
from admin.admin import admin
from user.user import user
from flask_mysqldb import MySQL

app = Flask(__name__)
app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(user, url_prefix="/user")

#mysql = MySQL()
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = ''
#app.config['MYSQL_PORT'] = 3306
#app.config['MYSQL_DB'] = 'proyectoweb'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#mysql.init_app(app)

@app.route('/')
def hola():
    return "<h1>Index App</h1>"


if __name__ == '__main__':
    app.run(debug=True)
