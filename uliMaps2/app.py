from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_DB'] = 'ulimaps'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql.init_app(app)

@app.route('/')
def index():
    return render_template('user/index.html')

@app.route('/admin')
def indexAdmin():
    return render_template('admin/login.html')

@app.route('/crud')
def crudAdmin():
    return render_template('admin/crud.html')

@app.route('/crudExterior')
def crudExterior():
    sql = "SELECT * FROM puntointeresexterior"
    cursor= mysql.connection.cursor()
    cursor.execute(sql)
    puntosExterior=cursor.fetchall()
    return render_template('admin/crud/crudExterior.html', puntosExterior = puntosExterior)

@app.route('/crudEstructura')
def crudEstructura():
    return render_template('admin/crud/crudEstructura.html')

@app.route('/crudPiso')
def crudPiso():
    return render_template('admin/crud/crudPiso.html')

@app.route('/crudInterior')
def crudInterior():
    return render_template('admin/crud/crudInterior.html')

@app.route('/crudParqueadero')
def crudParqueadero():
    return render_template('admin/crud/crudParqueadero.html')

if __name__ == '__main__':
    app.run(debug=True)
