from flask import Flask, request
from flask import render_template, redirect
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
    cursor.close()

    return render_template('usuarios/index.html', usuarios=db_usuarios)



#Registro de Usuarios
@app.route('/CrearRegistro')
def create():
    return render_template('usuarios/CrearRegistro.html')


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
        cursor.execute("SELECT * FROM usuarios")
        usuario = cursor.fetchall()  # Usar fetchone para obtener solo un usuario
        conn.commit()
        cursor.close()
        
        return render_template('usuarios/index.html', usuarios = usuario)


#Actualizacion de registros
@app.route('/edit/<int:Id>')
def edit(Id):
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE Id = %s", (Id,))
    usuario = cursor.fetchone()  # Usar fetchone para obtener solo un usuario
    cursor.close()

    return render_template('usuarios/edit.html', usuario=usuario)

@app.route('/update', methods=['POST'])
def update():
    _Nombre = request.form['nombre']
    _Usuario = request.form['Usuario']
    _Email = request.form['email']
    _Contraseña = request.form['contraseña']
    _Id = request.form['txtId']

    sql = "UPDATE `lapythoneta`.`usuarios` SET nombre =%s, usuario=%s,email=%s, password = %s  WHERE Id = %s"
    params = [_Nombre, _Usuario,_Email, _Contraseña, _Id]

    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute(sql, params)
    conn.commit()
    cursor.close()
    return redirect('/')


#EliminarElRegistro
@app.route('/destroy/<int:Id>', methods=['GET'])
def destroy(Id):
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE Id=%s", (Id,))
    conn.commit()
    cursor.close()
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)

