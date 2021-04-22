from flask import Flask, render_template
from datetime import timedelta

app = Flask(__name__, static_url_path = "/static", static_folder = "static", template_folder='views')
app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY='dev',
)
app.permanent_session_lifetime=timedelta(minutes=30)

from src.controllers import *
from src.controllers.auth import user
from src.controllers.short import *
def create_app():
    app.run(debug=True, port=5000)
