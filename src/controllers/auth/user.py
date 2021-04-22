from src import app
from flask import render_template, request, redirect, url_for, g, session
from src.dto.user import UserDTO
from src.models.user import User
import hashlib


@app.route('/register')
def register():
    return render_template('auth/register.html')

@app.route('/sigin')
def sigin():
    if "user" in session:
        return redirect(url_for('user'))
    return render_template('auth/sigin.html')

@app.route('/register_user', methods=['POST'])
def registerUser():
    validation=""
    nombre=request.form.get('nombre')
    emailaddress=request.form.get('email_address')
    contrasenia=request.form.get('password')

    #comprobar si el usuario existe en la base de datos
    user_valid=User().user_exits_by_name(str(nombre))

    if(user_valid):
        validation="El nombre de usuario ya existe en la base de datos, elige otro porfavor"
        return render_template("auth/register.html",validacion=validation)
    else:
        validation="Usuario creado, Puedes Iniciar Sesion"
        #contrasenia encryptada
        h=hashlib.new("sha1",str(contrasenia).encode('utf-8'))
        password=h.hexdigest()
        #agregamos el nuevo usuario a la base de datos
        userdto=UserDTO(nombre,emailaddress,password)
        user=User().add_user(userdto)

    return render_template("auth/sigin.html",validacion=validation) 

@app.route('/login', methods=['POST'])
def login():
    validation=""
    if(request.method=="POST"):
        nombre=request.form.get('nombre')
        contrasenia=request.form.get('password')

        #filtrar por nombre y contrasenia en la db
        h=hashlib.new("sha1",str(contrasenia).encode('utf-8'))
        password=h.hexdigest()

        userdto=UserDTO(nombre,"",password)
        resolve_user=User().user_exits(userdto)

        if(resolve_user):
            session.permanent=True
            session["user"]=resolve_user.nombre
            session["id"]=resolve_user.id
            #return "HI"
            return redirect(url_for('user'))

        else:
            validation="Nombre de usuario o contraseña incorrectos"
            return render_template("auth/sigin.html",validation=validation) 
    else:
        if "user" in session:
            #return "HI"
            return redirect(url_for('user'))
    #colocar el nombre del usuario en el navbar si la cuenta existe
    #Si no existe, redireccionar a login con un error en el span
    return redirect('auth/sigin.html')

@app.route('/user')
def user():
    if "user" in session:
        user=session["user"]
        return render_template("index.html", username=str(user), login_exits=True)


@app.route('/logout')
def logout():
    session.pop("user",None)
    session.pop("id",None)
    #return redirect(url_for('login'))
    return redirect(url_for('index'))


