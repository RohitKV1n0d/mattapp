from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#code for ecommerce website using flask




=======
#chaange to test

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Product %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        product_name = request.form['name']
        product_price = request.form['price']
        product_quantity = request.form['quantity']
        new_product = Product(name=product_name, price=product_price, quantity=product_quantity)

        try:
            db.session.add(new_product)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your product'

    else:
        products = Product.query.order_by(Product.date_created).all()
        return render_template('index.html', products=products)

@app.route('/delete/<int:id>')
def delete(id):
    product_to_delete = Product.query.get_or_404(id)

    try:
        db.session.delete(product_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'
    
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    product = Product.query.get_or_404(id)

    if request.method == 'POST':
        product.name = request.form['name']
        product.price = request.form['price']
        product.quantity = request.form['quantity']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your product'

    else:
        return render_template('update.html', product=product)
    
if __name__ == "__main__":
    app.run(debug=True)
        































# app = Flask(__name__)

# # Database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# db = SQLAlchemy(app)

# # Model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200), nullable=False)
#     email = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<User %r>' % self.id

# # Routes
# @app.route('/', methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         user_name = request.form['name']
#         user_email = request.form['email']
#         new_user = User(name=user_name, email=user_email)

#         try:
#             db.session.add(new_user)
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an issue adding your user'

#     else:
#         users = User.query.order_by(User.date_created).all()
#         return render_template('index.html', users=users)






# @app.route('/delete/<int:id>')
# def delete(id):
#     user_to_delete = User.query.get_or_404(id)

#     try:
#         db.session.delete(user_to_delete)
#         db.session.commit()
#         return redirect('/')
#     except:
#         return 'There was a problem deleting that user'

# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     user = User.query.get_or_404(id)

#     if request.method == 'POST':
#         user.name = request.form['name']
#         user.email = request.form['email']

#         try:
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an issue updating your user'

#     else:
#         return render_template('update.html', user=user)

# if __name__ == "__main__":
#     app.run(debug=True)

# # Path: templates/index.html

