



from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_admin import Admin ,AdminIndexView, BaseView, expose
from flask_admin.model.base import BaseModelView
from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import validators
from wtforms.validators import InputRequired, Email, Length
import os

import xlrd






app = Flask(__name__)


app.secret_key = 'asdaasdasdsdasdasasdasddasadswdasdsdasdasdaveasdaqvq34c'

UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER_IMPORT'] = UPLOAD_FOLDER


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


class MyModelView(ModelView):
    BaseModelView.can_export = True
    BaseModelView.export_types = ['csv', 'xls']
    def is_accessible(self):
        if current_user.userRole == 'admin':
            return current_user.is_authenticated
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('register'))

    def not_auth(self):
        return redirect(url_for('register'))

    #image 
   


    






class ImportData(BaseView):
    @expose('/', methods=['GET', 'POST'])
    def index(self):
        #post to get file
        def xlsx_to_database(filename):
            wb = xlrd.open_workbook(filename)
            sheet = wb.sheet_by_index(3)
            sheet.cell_value(0, 0)
            for i in range(1, sheet.nrows):
                addUsers = UserDetails(name=sheet.cell_value(i, 0), password="defpass123", email=str(sheet.cell_value(i, 1))+"@email.com", userRole="user",
                                        premiumPackage="free", contactsLeft=0, profileId=sheet.cell_value(i, 1), gender=sheet.cell_value(i, 2),
                                        dob=sheet.cell_value(i, 3), hight=str(sheet.cell_value(i, 4)), weight=str(sheet.cell_value(i, 5)),
                                        complexion=sheet.cell_value(i, 6), bodyType=sheet.cell_value(i, 7), maritalStatus=sheet.cell_value(i, 8),
                                        noOfChildren=sheet.cell_value(i, 9), physicalStatus=sheet.cell_value(i, 10), motherTongue=sheet.cell_value(i, 11),
                                        nativePlace=sheet.cell_value(i, 12), bloodGroup=sheet.cell_value(i, 13), profileCreatedfor=sheet.cell_value(i, 14),
                                        religion=sheet.cell_value(i, 15), caste=sheet.cell_value(i, 16), star=sheet.cell_value(i, 17),
                                        jathakam=sheet.cell_value(i, 18), educationCategory=sheet.cell_value(i, 19), educationType=sheet.cell_value(i, 20),
                                        occupation=sheet.cell_value(i, 21), occupationType=sheet.cell_value(i, 22), jobcountry=sheet.cell_value(i, 23),
                                        jobstate=sheet.cell_value(i, 24), jobdistrict=sheet.cell_value(i, 25), jobcity=sheet.cell_value(i, 26),
                                        anualIncome=sheet.cell_value(i, 27), residenceAddr=sheet.cell_value(i, 28), userLocation=sheet.cell_value(i, 29),
                                        phoneNumber=sheet.cell_value(i, 30), whatsapp=sheet.cell_value(i, 31), prefferedContact=sheet.cell_value(i, 32),
                                        prefferedContactPersonName=sheet.cell_value(i, 33), prefferedContactRelaion=sheet.cell_value(i, 34), fatherName=sheet.cell_value(i, 35),
                                        fatherEducation=sheet.cell_value(i, 36), fatherOccupation=sheet.cell_value(i, 37), fatherOccupationDetail=sheet.cell_value(i, 38),
                                        motherName=sheet.cell_value(i, 39), motherEducation=sheet.cell_value(i, 40), motherOccupation=sheet.cell_value(i, 41),
                                        motherOccupationDetail=sheet.cell_value(i, 42), noOfMarriedBrothers=sheet.cell_value(i, 43), noOfMarriedSisters=int(sheet.cell_value(i, 44)),
                                        noOfUnmarriedBrothers=sheet.cell_value(i, 45), noOfUnmarriedSisters=sheet.cell_value(i, 46), familyType=sheet.cell_value(i, 47),
                                        familyValue=sheet.cell_value(i, 48),
                                        financialStatus=sheet.cell_value(i, 49), userOwnerOF=sheet.cell_value(i, 50), eatingHabbits=sheet.cell_value(i, 51),
                                        drinkingHabbits=sheet.cell_value(i, 52), somkingHabbits=sheet.cell_value(i, 53), languegesKnow=sheet.cell_value(i, 54),
                                        hobbies=sheet.cell_value(i, 55), intrests=sheet.cell_value(i, 56), minAge=sheet.cell_value(i, 57),
                                        maxAge=sheet.cell_value(i, 58), minHeight=sheet.cell_value(i, 59), maxHeight=sheet.cell_value(i, 60),
                                        pComplexion=sheet.cell_value(i, 61), pBodyType=sheet.cell_value(i, 62), pMaritalStatus=sheet.cell_value(i, 63),
                                        pPhysicalStatus=sheet.cell_value(i, 64), pFamilyStatus=sheet.cell_value(i, 65), pReligion=sheet.cell_value(i, 66),
                                        pCaste=sheet.cell_value(i, 67), pStar=sheet.cell_value(i, 68), pJaathakam=sheet.cell_value(i, 69),
                                        pEducationCategory=sheet.cell_value(i, 70), pOccupation=sheet.cell_value(i, 71), pAnualIncome=sheet.cell_value(i, 72),
                                        pCountry=sheet.cell_value(i, 73), pState=sheet.cell_value(i, 74), pDistrict=sheet.cell_value(i, 75),
                                        lookingFor=sheet.cell_value(i, 76), about=sheet.cell_value(i, 77))
                db.session.add(addUsers)
                db.session.commit()
                               

           

        if request.method == 'POST':
            file = request.files['file']
            if not file:
                return "No file"
            file.save(os.path.join(app.config['UPLOAD_FOLDER_IMPORT'], file.filename))
            addImage = UserDetails.query.filter_by(id=current_user.id).first()
            addImage.userimage = file.filename
            db.session.commit()
            xlsx_to_database(os.path.join(app.config['UPLOAD_FOLDER_IMPORT'], file.filename))
            return redirect(url_for('admin.index'))
        return self.render('admin/import.html')



class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        if current_user.userRole == 'admin':
            return current_user.is_authenticated
        else:
            return False
        
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('register'))

    def not_auth(self):
        return redirect(url_for('register'))
    


admin = Admin(app,index_view=MyAdminIndexView(),template_mode='bootstrap3')



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
    premiumPackage = db.Column(db.String(200), nullable=True)#
    contactsLeft = db.Column(db.Integer, nullable=True)# 
    userimage = db.Column(db.String(200), nullable=True)
    profileId = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(200), nullable=False)
    dob = db.Column(db.String(300), nullable=False) 
    hight = db.Column(db.String(200), nullable=True) 
    weight = db.Column(db.String(200), nullable=True) 
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
    fatherEducation = db.Column(db.String(200), nullable=True)####
    fatherOccupation = db.Column(db.String(200), nullable=True)
    fatherOccupationDetail = db.Column(db.String(200), nullable=True)
    motherName = db.Column(db.String(200), nullable=True)#@##
    motherEducation = db.Column(db.String(200), nullable=True)####
    motherOccupation = db.Column(db.String(200), nullable=True)
    motherOccupationDetail = db.Column(db.String(200), nullable=True)
    noOfMarriedBrothers = db.Column(db.String(200), nullable=True)
    noOfMarriedSisters = db.Column(db.String(200), nullable=True)#
    noOfUnmarriedBrothers = db.Column(db.String(200), nullable=True)#@
    noOfUnmarriedSisters = db.Column(db.String(200), nullable=True)
    familyType = db.Column(db.String(200), nullable=True)
    familyValue = db.Column(db.String(200), nullable=True)
    financialStatus = db.Column(db.String(200), nullable=True)
    userOwnerOF = db.Column(db.String(200), nullable=True)
    eatingHabbits = db.Column(db.String(200), nullable=True)
    drinkingHabbits = db.Column(db.String(200), nullable=True)
    somkingHabbits = db.Column(db.String(200), nullable=True)##
    languegesKnow = db.Column(db.String(200), nullable=True)
    hobbies = db.Column(db.String(200), nullable=True)
    intrests = db.Column(db.String(200), nullable=True)
    minAge = db.Column(db.String(200), nullable=True)
    maxAge = db.Column(db.String(200), nullable=True)
    minHeight = db.Column(db.String(200), nullable=True)
    maxHeight = db.Column(db.String(200), nullable=True)
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
    lookingFor = db.Column(db.String(200), nullable=True)
    about = db.Column(db.Text, nullable=True)

    # image = db.relationship('Image', backref='Iamges')


    def __repr__(self):
        return '<UserDetails %r>' % self.name



# class Images(db.Model):
#     __tablename__ = 'images'
#     img_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))
#     path = db.Column(db.String, unique=True)
#     fId = db.Column(db.Integer, db.ForeignKey('userdetails.id'))

#     def __repr__(self):
#         return self.name








class FilterDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(200), nullable=True)
    height = db.Column(db.String(200), nullable=True)
    weight = db.Column(db.String(200), nullable=True)
    bloodtype = db.Column(db.String(200), nullable=True)
    bodytype = db.Column(db.String(200), nullable=True) ######
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



admin.add_view(MyModelView(UserDetails, db.session))
admin.add_view(MyModelView(FilterDetails, db.session))
admin.add_view(ImportData())


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired('username is required'),Length(min=3,max=20), ])
    password = PasswordField('password', validators= [InputRequired(), Length(min=6, max=81, message=('8 letters!')) ])
    submit = SubmitField("Login")










@app.route('/')
@app.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    else:
        if request.method == 'POST':
            userDetails = UserDetails(name=request.form['name'],password=request.form['password'], email=request.form['email'] , profileId="TestONLY", userRole="user", premiumPackage="None",
                                                        contactsLeft=0,gender=request.form['gender'], dob=request.form['dob'], phoneNumber=request.form['phoneNumber'],
                                                        religion=request.form['religion'], caste=request.form['caste'])
            try:
                db.session.add(userDetails)
                db.session.commit()
                return redirect('login')
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
    return render_template('registerDone_search.html',name=current_user.name,role=current_user.userRole)







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
        






















