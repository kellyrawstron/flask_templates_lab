from flask import render_template
from app import app
from models.event_list import events
from models.event import Event


@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events')