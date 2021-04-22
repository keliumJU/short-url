from src import app
from flask import render_template, request, redirect, url_for, session
from src.models.short_path import ShortPath
from src.dto.short_path import ShortPathDTO

@app.route('/edit_path',methods=['POST'])
def save_edit():
    if request.method=="POST":
        large_path=request.form.get('large_url')
        id_path=request.form.get('id_path')
        ShortPath().update_path(large_path, id_path)
        return redirect(url_for("display_all"))
     