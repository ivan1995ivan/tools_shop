from flask import Flask, render_template
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_shop.db'
db.init_app(app)

@app.route('/')
def index():
    from models import Product  # Отложенный импорт
    products = Product.query.all()
    return render_template('index.html', products=products)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
