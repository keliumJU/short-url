from src import app
from flask import render_template, request, redirect, url_for, session
from src.models.short_path import ShortPath
from src.dto.short_path import ShortPathDTO
#para realizar el short path
import random
import string
import os

@app.route('/short_urls',methods=['GET'])
def short_urls():
    return render_template('shortpath/short_url.html')


def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=3)
        rand_letters = "".join(rand_letters)
        if "user" in session:
            short_url = ShortPath().get_path_short_by_user(rand_letters,session["id"]) 
        else:
            return rand_letters

        if not short_url:
            return rand_letters


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        url_received = request.form["short-path"]
        flag=False    
        if "user" in session:
            found_url = ShortPath().get_path_by_user(url_received,session["id"]) 
            flag=True
        else:
            pass 
        #Url encontrada, validar
        if flag and found_url:
            return redirect(url_for("display_short_url", url=found_url.pathShort))
        else:
            short_url = shorten_url()
            #print(short_url)
            #Recuperar la sesion para agregar el usuario
            if "user" in session:
                shortdto=ShortPathDTO(url_received,short_url,session["id"])
                new_url = ShortPath().add_path(shortdto)
            #para usuarios anonimos
            session["short_url_test"]=short_url
            session["long_url_test"]=url_received

            return redirect(url_for("display_short_url", url=short_url))
    else:
        return render_template('index.html')

#Display url in host
@app.route('/<short_url>')
def redirection(short_url):
    if "user" in session:
        long_url = ShortPath().get_path_short_by_user(short_url,session["id"])
        if long_url:
            return redirect(long_url.path)
    else:
        if "short_url_test" in session:
            long_url=session["long_url_test"]
            return redirect(str(long_url))
    return render_template('index.html',validation="La Url no existe, porfavor agregala") 

@app.route('/display/<url>')
def display_short_url(url):
    if "user" in session:
        return render_template('index.html', short_url_display="localhost:5000/"+url, username=session["user"],login_exits=True) 

    return render_template('index.html', short_url_display="localhost:5000/"+url) 

#after
#esto deberia pasar un redirect que lleve el nombre de usuario y con eso pasar el objeto AuthUser que 
#se mapea a todas las paginas que necesiten un usuario? la url quedaria asi: /user/juaniato/all_urls
@app.route('/user/all_urls')
def display_all():
    host="localhost:5000/"
    if "user" in session:
        id_user=session["id"]
        name_user=session["user"]
        paths=ShortPath().get_all_by_user(id_user)
        return render_template('shortpath/short_url.html', vals=paths, host=host, login_exits=True, username=name_user)


#Delete register by user
@app.route('/delete/<int:id>',methods=['GET'])
def delete_path(id):
    id_user=session["id"]
    d=ShortPath().delete_path(id, id_user)
    if d:
        #eliminacion correcta
        return redirect(url_for('display_all')) 
    else:
        return render_template('index.html')

#Edit url large by user

@app.route('/edit/<int:id>',methods=['GET'])
def edit_path(id):
    large_url=ShortPath().get_path_by_id(id)
    return render_template('shortpath/edit_url.html',large_url=str(large_url.path), id_path=int(large_url.id),login_exits=True, username=session["user"])

