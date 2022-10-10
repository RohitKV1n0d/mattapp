


from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_admin import Admin ,AdminIndexView
from flask_admin.model.base import BaseModelView
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import validators
from wtforms.validators import InputRequired, Email, Length
import os






app = Flask(__name__)


app.secret_key = 'asdaasdasdsdasdasasdasddasadswdasdsdasdasdaveasdaqvq34c'



ENV = 'prod'

if ENV == 'dev' :
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
    app.config['SECRET_KEY'] = 'asdasdasdasdasdasdasdaveqvq34c'

else:
    app.debug = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SECRET_KEY'] = SECRET_KEY
    
SQLALCHEMY_TRACK_MODIFICATIONS = False




db =SQLAlchemy(app)

class MyAdminIndexView(AdminIndexView):
    BaseModelView.can_export = True
    BaseModelView.export_types = ['csv', 'xls']
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))

admin = Admin(app, name='Admin', template_mode='bootstrap3')



login = LoginManager()
login.init_app(app)
login.login_view = 'login'

@login.user_loader
def load_user(id):
    return UserDetails.query.get(int(id))





class UserDetails(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    password  = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    userRole =db.Column(db.String(200), nullable=False)
    userimage = db.Column(db.String(200), nullable=True)
    profileId = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(200), nullable=False)
    dob = db.Column(db.String(300), nullable=False) 
    hight = db.Column(db.Integer, nullable=True)
    complexion = db.Column(db.String(200), nullable=True)    
    bodyType = db.Column(db.String(200), nullable=True)
    maritalStatus = db.Column(db.String(200), nullable=True)
    noOfChildren = db.Column(db.Integer, nullable=True)
    physicalStatus = db.Column(db.String(200), nullable=True)
    motherTongue = db.Column(db.String(200), nullable=True)
    nativePlace = db.Column(db.String(200), nullable=True)
    bloodGroup = db.Column(db.String(200), nullable=True)
    profileCreatedfor = db.Column(db.String(200), nullable=True)
    religion = db.Column(db.String(200), nullable=False)
    caste = db.Column(db.String(200), nullable=False)
    star = db.Column(db.String(200), nullable=True)
    jathakam = db.Column(db.String(200), nullable=True)
    educationCategory = db.Column(db.String(200), nullable=True)
    educationType = db.Column(db.String(200), nullable=True)
    occupation = db.Column(db.String(200), nullable=True)
    occupationType = db.Column(db.String(200), nullable=True)
    jobcountry = db.Column(db.String(200), nullable=True)
    jobstate = db.Column(db.String(200), nullable=True)
    jobdistrict = db.Column(db.String(200), nullable=True)
    jobcity = db.Column(db.String(200), nullable=True)
    anualIncome = db.Column(db.String(200), nullable=True)
    residenceAddr = db.Column(db.String(200), nullable=True)
    userLocation = db.Column(db.String(200), nullable=True)
    phoneNumber = db.Column(db.String(200), nullable=False)
    whatsapp = db.Column(db.String(200), nullable=True)
    prefferedContact = db.Column(db.String(200), nullable=True)
    prefferedContactPersonName = db.Column(db.String(200), nullable=True)
    prefferedContactRelaion = db.Column(db.String(200), nullable=True)
    fatherName = db.Column(db.String(200), nullable=True)
    motherName = db.Column(db.String(200), nullable=True)
    fatherOccupation = db.Column(db.String(200), nullable=True)
    fatherOccupationDetail = db.Column(db.String(200), nullable=True)
    motherOccupation = db.Column(db.String(200), nullable=True)
    motherOccupationDetail = db.Column(db.String(200), nullable=True)
    noOfMarriedBrothers = db.Column(db.Integer, nullable=True)
    noOfUnmarriedBrothers = db.Column(db.Integer, nullable=True)
    noOfMarriedSisters = db.Column(db.Integer, nullable=True)
    noOfUnmarriedSisters = db.Column(db.Integer, nullable=True)
    familyType = db.Column(db.String(200), nullable=True)
    familyValue = db.Column(db.String(200), nullable=True)
    financialStatus = db.Column(db.String(200), nullable=True)
    userOwnerOF = db.Column(db.String(200), nullable=True)
    eatingHabbits = db.Column(db.String(200), nullable=True)
    drinkingHabbits = db.Column(db.String(200), nullable=True)
    languegesKnow = db.Column(db.String(200), nullable=True)
    hobbies = db.Column(db.String(200), nullable=True)
    intrests = db.Column(db.String(200), nullable=True)
    minAge = db.Column(db.Integer, nullable=True)
    maxAge = db.Column(db.Integer, nullable=True)
    minHeight = db.Column(db.Integer, nullable=True)
    maxHeight = db.Column(db.Integer, nullable=True)
    pComplexion = db.Column(db.String(200), nullable=True)
    pBodyType = db.Column(db.String(200), nullable=True)
    pMaritalStatus = db.Column(db.String(200), nullable=True)
    pPhysicalStatus = db.Column(db.String(200), nullable=True)
    pFamilyStatus = db.Column(db.String(200), nullable=True)
    pReligion = db.Column(db.String(200), nullable=True)
    pCaste = db.Column(db.String(200), nullable=True)
    pStar = db.Column(db.String(200), nullable=True)
    pJaathakam = db.Column(db.String(200), nullable=True)
    pEducationCategory = db.Column(db.String(200), nullable=True)
    pOccupation = db.Column(db.String(200), nullable=True)
    pAnualIncome = db.Column(db.String(200), nullable=True)
    pCountry = db.Column(db.String(200), nullable=True)
    pState = db.Column(db.String(200), nullable=True)
    pDistrict = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return '<UserDetails %r>' % self.name


class FilterDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(200), nullable=True)
    height = db.Column(db.String(200), nullable=True)
    weight = db.Column(db.String(200), nullable=True)
    bloodtype = db.Column(db.String(200), nullable=True)
    complexion = db.Column(db.String(200), nullable=True)
    physcialstatus = db.Column(db.String(200), nullable=True)
    maritalstatus = db.Column(db.String(200), nullable=True)
    profileCreatedfor = db.Column(db.String(200), nullable=True)
    countryCode = db.Column(db.String(200), nullable=True)
    prefTimeToCall = db.Column(db.String(200), nullable=True)
    religion = db.Column(db.String(200), nullable=True)
    christianCaste = db.Column(db.String(200), nullable=True)
    hinduCaste = db.Column(db.String(200), nullable=True)
    muslimCaste = db.Column(db.String(200), nullable=True)
    higestEducation = db.Column(db.String(200), nullable=True)
    doc = db.Column(db.String(200), nullable=True)
    master = db.Column(db.String(200), nullable=True)
    bachelors = db.Column(db.String(200), nullable=True)
    diploma = db.Column(db.String(200), nullable=True)
    tradeSchool = db.Column(db.String(200), nullable=True)
    higerSecondary = db.Column(db.String(200), nullable=True)
    highSchool = db.Column(db.String(200), nullable=True)
    #job = db.Column(db.String(200), nullable=True)
    jobCategory = db.Column(db.String(200), nullable=True)
    jobType = db.Column(db.String(200), nullable=True)
    monthlyIncome = db.Column(db.String(200), nullable=True)
    eatingHabits = db.Column(db.String(200), nullable=True)
    drinkingHabits = db.Column(db.String(200), nullable=True)
    smokingHabits = db.Column(db.String(200), nullable=True)
    languagesKnown = db.Column(db.String(200), nullable=True)
    hobbies = db.Column(db.String(200), nullable=True)
    intrests = db.Column(db.String(200), nullable=True)
    star =  db.Column(db.String(200), nullable=True)
    raasi = db.Column(db.String(200), nullable=True)
    typeofJaathakam = db.Column(db.String(200), nullable=True)
    country = db.Column(db.String(200), nullable=True)
    youHaveOwn = db.Column(db.String(200), nullable=True)
    landinfo = db.Column(db.String(200), nullable=True) ######
    ernakulam = db.Column(db.String(200), nullable=True)
    thiruvananthapuram = db.Column(db.String(200), nullable=True)
    kollam = db.Column(db.String(200), nullable=True)
    pathanamthitta = db.Column(db.String(200), nullable=True)
    alappuzha = db.Column(db.String(200), nullable=True)
    kottayam = db.Column(db.String(200), nullable=True)
    idukki = db.Column(db.String(200), nullable=True)
    thrissur = db.Column(db.String(200), nullable=True)
    palakkad = db.Column(db.String(200), nullable=True)
    malappuram = db.Column(db.String(200), nullable=True)
    kozhikode = db.Column(db.String(200), nullable=True)
    wayanad = db.Column(db.String(200), nullable=True)
    kannur = db.Column(db.String(200), nullable=True)
    kasaragod = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return '<FilterDetails %r>' % self.name



admin.add_view(ModelView(UserDetails, db.session))
admin.add_view(ModelView(FilterDetails, db.session))


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired('username is required'),Length(min=3,max=20), ])
    password = PasswordField('password', validators= [InputRequired(), Length(min=6, max=81, message=('8 letters!')) ])
    submit = SubmitField("Login")










@app.route('/')
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        userDetails = UserDetails(name=request.form['name'],password=request.form['password'],email=request.form['email'] ,profileId="TestONLY",userRole="user",gender=request.form['gender'],
                                                    dob=request.form['dob'],phoneNumber=request.form['phoneNumber'],
                                                    religion=request.form['religion'],caste=request.form['caste'])
        try:
            db.session.add(userDetails)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:   
        userDetails = UserDetails.query.order_by(UserDetails.id).all()
        return render_template('register_search.html', userDetails=userDetails)


@app.route('/login', methods = ["GET",'POST'])
def login():
    
    if request.method == 'POST':
        user = UserDetails.query.filter_by(email=request.form['email']).first()
        if user:
            if request.form['password'] == user.password:
                login_user(user)
                return redirect(url_for('home'))

    return render_template('login.html')



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
@login_required
def home():
    return render_template('index.html')







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
        






















