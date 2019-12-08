from flask import Flask, render_template, request
from db_helpers import get_db, query_db


DATABASE = 'food.db'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/food_status', methods=['GET'])
def food_status():
    db = get_db(DATABASE).cursor()
    fridge_contents = query_db(db, 'select * from fridge')
    return render_template('food_status.html', fridge_contents=fridge_contents)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

