from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#code for ecommerce website using flask

app = Flask(__name__)
# app.secret_key = 'asdaasdasdsdasdasasdasddasdasdasdaveasdaqvq34c'   


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
# db = SQLAlchemy(app)

# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200), nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<Product %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('register_search.html')







# @app.route('/delete/<int:id>')
# def delete(id):
#     product_to_delete = Product.query.get_or_404(id)

#     try: 
#         db.session.delete(product_to_delete)
#         db.session.commit()
#         return redirect('/')
#     except:
#         return 'There was a problem deleting that task'
    
# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     product = Product.query.get_or_404(id)

#     if request.method == 'POST':
#         product.name = request.form['name']
#         product.price = request.form['price']
#         product.quantity = request.form['quantity']

#         try:
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an issue updating your product'

#     else:
#         return render_template('update.html', product=product)
    
if __name__ == "__main__":
    app.run(debug=True)
        






















