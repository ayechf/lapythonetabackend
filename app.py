from flask import Flask, request
from flask import render_template
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'lapythoneta'

mysql = MySQL(app)

@app.route('/') 
def index():
    conn = mysql.connection
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM usuarios") 
    db_usuarios = cursor.fetchall()
    print("-"*60)
    for usuarios in db_usuarios:
        print(usuarios)
        print("-"*60)
    cursor.close()

    return render_template('usuarios/index.html', usuarios=db_usuarios)

@app.route('/edit.html')
def edit():
    return render_template('usuarios/edit.html')

#Registro de Usuarios

@app.route('/crear-registro', methods=["POST"])
def crear_registro():
    if request.method == "POST":
        _nombre = request.form['txtNombre']
        _usuario = request.form['txtUsuario']
        _email = request.form['txtEmail']
        _password = request.form['txtPassword']

        conn = mysql.connection
        cursor = conn.cursor()
        sql = "INSERT INTO usuarios (nombre, usuario, email, password) VALUES (%s, %s, %s, %s);"
        cursor.execute(sql, (_nombre, _usuario, _email, _password))
        conn.commit()
        cursor.close()

        return render_template('usuarios/edit.html')

if __name__=='__main__':
    app.run(debug=True)

