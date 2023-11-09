from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
#the secret key (line below) is part of the debugtoolbar
app.config['SECRET_KEY'] = 'not-so=secret-for-now'
#also need to add this line below (app) if we use app.py
# if we use myapp ... 
#  1. above app = Flask(__name__) need to change to myapp = ...
#  2. @app.route() ... all need to change to @myapp.route()
#  3. DebugToolbarExtension(app) ... need to be Deb...(myapp)

debug = DebugToolbarExtension(app)

@app.route("/")
def get_answer():
    """form to get words"""
    prompts = story.prompts
    return render_template("home.html",prompts = prompts)

@app.route("/story")
def show_story():
    """show story"""
    text = story.generate(request.args)
    return render_template("show_story.html", text=text)