from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY']= "secret"


debug = DebugToolbarExtension(app)

@app.route("/")
def questions():
    """Creates form to ask words"""

    prompts = story.prompts

    return render_template("quest.html", prompts= prompts)

@app.route("/story")
def story_results():
    """Shows the results of story"""

    text = story.generate(request.args)

    return render_template("story.html" , text=text)
