
# Minyi Li, ml3754@drexel.edu 
# CS530: DUI, Assignment [2] 


import os

from flask import (Flask, g, json, jsonify, redirect, render_template, request,
                   session)     

from db import Database


app = Flask(__name__)


DATABASE_PATH = 'bikes.db'



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')



# create a new function that renders a template for the route “/bikes”,
# make a variable to store the bike data,
# the data contents are copied from the data/data.txt, 
# the call to render_template() that passes the data to the template.

@app.route('/bikes')
def bikes():
    data = {
        'bikes': [
            {"id": "b1",
             "name": "Sixthreezero Around The Block Women's Single Speed Cruiser Bicycle Coral w/ Black Seat/Grips",
             "wheels": 2,
             "size": 26,
             "motor": "No",
             "folding": "No",
             "image": "sixthreezero.jpg",
             "available": 2},
            {
                "id": "b2",
                "name": "Roadmaster 26 Men's Granite Peak Men's Bike",
                "wheels": 2,
                "size": 26,
                "motor": "No",
                "folding": "No",
                "image": "roadmaster.jpg",
                "available": 0
            },
            {
                "id": "b3",
                "name": "Fun 20 Inch Wheel Unicycle with Alloy Rim",
                "wheels": 1,
                "size": 20,
                "motor": "No",
                "folding": "No",
                "image": "unicycle.jpg",
                "available": 7
            },
            {
                "id": "b4",
                "name": "Mongoose Dolomite Fat Tire Mountain Bike",
                "wheels": 2,
                "size": 26,
                "motor": "No",
                "folding": "No",
                "image": "mongoose.jpg",
                "available": 3
            },
            {
                "id": "b5",
                "name": "EuroMini ZiZZO Campo 28lb Lightweight Aluminum Frame Shimano 7 - Speed Folding Bike",
                "wheels": 2,
                "size": 20,
                "motor": "No",
                "folding": "Yes",
                "image": "euromini.jpg",
                "available": 1
            },
            {
                "id": "b6",
                "name": "Huffy Mountain Bike Summit Ridge w / Shimano & Trail Tires",
                "wheels": 2,
                "size": 24,
                "motor": "No",
                "folding": "No",
                "image": "huffy.jpg",
                "available": 0
            },
            {
                "id": "b7",
                "name": "Razor RSF350 Electric Street Bike",
                "wheels": 2,
                "size": 10,
                "motor": "Yes",
                "folding": "No",
                "image": "razor.jpg",
                "available": 8
            },
            {
                "id": "b8",
                "name": "Shaofu Folding Electric Bicycle – 350W 36V Waterproof E-Bike with 15 Mile Range Collapsible Frame and APP Speed Setting",
                "wheels": 2,
                "size": 12,
                "motor": "Yes",
                "folding": "Yes",
                "image": "shaofu.jpg",
                "available": 0
            },
            {
                "id": "b9",
                "name": "Goplus Adult Tricycle Trike Cruise Bike Three-Wheeled Bicycle w/Large Size Basket for Recreation Shopping Exercise",
                "wheels": 3,
                "size": 26,
                "motor": "No",
                "folding": "No",
                "image": "tricycle.jpg",
                "available": 2
            },
            {
                "id": "b10",
                "name": "Swagtron 200W SWAGCYCLE Envy Steel Frame Folding Electric Bicycle e Bike w / Automatic Headlight",
                "wheels": 2,
                "size": 12,
                "motor": "Yes",
                "folding": "Yes",
                "image": "swagtron.jpg",
                "available": 5
            }
        ]
    
    }
    return render_template('bikes.html',data = data)



@app.route('/rent')
def rent():
    return render_template('rent.html')


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = Database(DATABASE_PATH)
    return db

@app.teardown_appcontext
def close_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def generate_response(args):
    return jsonify(get_db().get_bikes())


@app.route('/api/get_bikes', methods=['GET'])
def api_get_bikes():
    return generate_response(request.args)


@app.route('/api/update_bikes', methods=['POST'])
def api_update_bikes():
    tid = request.form.get('id')
    available = request.form.get('available')
    get_db().update_bikes(tid, available)
    return generate_response(request.form)


@app.route('/api/reset_bikes', methods=['POST'])
def api_reset_bikes():
    available = request.form.get('available')
    get_db().reset_bikes(available)
    return generate_response(request.form)



if __name__ == '__main__':
    app.run(host='localhost', port=8081, debug=True)
