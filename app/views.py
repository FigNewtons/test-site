from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'FigNewtons'}

    items = [
        {
            'product': {'name': 'Hat 1'},
            'description': 'Baby blue hat'
        },
        {
            'product': {'name': 'Hat 2'},
            'description': 'Pink hat'
        }
    ]

    return render_template('index.html',
                            title = 'My Store',
                            user = user,
                            items = items)
