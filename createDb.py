from app import app, db ,FilterDetails
from flask import Flask, render_template, request, redirect, url_for
import app as APP

import xlrd

def test_connection(self):
    with app.app_context():
        db.create_all() 
        print("Database created")

def create_admin(self):
    with app.app_context():
        name = "admin"
        password = "admin123"
        userDetails = APP.UserDetails(name=name,password=password,email="admin123@admin.com" ,profileId="admin1",userRole="admin",gender="none",
                                                dob="none",phoneNumber="0000000000",
                                                religion="none",caste="none")
    
    
        db.session.add(userDetails)
        db.session.commit()
        print("Admin created")

def load_details(self):
    loc = ("dbDetails.xlsx")  #BD -471
 
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(2)
    sheet.cell_value(0, 0)


    for i in range(1,471):
        addDetails =   FilterDetails(gender=sheet.cell_value(i, 0),height=sheet.cell_value(i, 1),
                                    weight=sheet.cell_value(i, 2),bloodtype=sheet.cell_value(i, 3),bodytype=sheet.cell_value(i, 4),
                                     complexion=sheet.cell_value(i, 5),
                                    physcialstatus=sheet.cell_value(i, 6), maritalstatus= sheet.cell_value(i, 7), profileCreatedfor=sheet.cell_value(i, 8),
                                    countryCode=sheet.cell_value(i, 9),prefTimeToCall=sheet.cell_value(i, 10),religion=sheet.cell_value(i, 11),
                                    christianCaste=sheet.cell_value(i, 12),hinduCaste=sheet.cell_value(i, 13),muslimCaste=sheet.cell_value(i, 14),
                                    higestEducation=sheet.cell_value(i, 15),doc=sheet.cell_value(i, 16),master=sheet.cell_value(i, 17),
                                    bachelors=sheet.cell_value(i, 18),diploma=sheet.cell_value(i, 19),tradeSchool=sheet.cell_value(i, 20),
                                    higerSecondary=sheet.cell_value(i, 21),highSchool=sheet.cell_value(i, 22),jobCategory=sheet.cell_value(i, 23),
                                    jobType=sheet.cell_value(i, 24),monthlyIncome=sheet.cell_value(i, 25),eatingHabits=sheet.cell_value(i, 26),
                                    drinkingHabits=sheet.cell_value(i, 27),smokingHabits=sheet.cell_value(i, 28),languagesKnown=sheet.cell_value(i, 29),
                                    hobbies=sheet.cell_value(i, 30),intrests=sheet.cell_value(i, 31),star=sheet.cell_value(i, 32),raasi=sheet.cell_value(i, 33),
                                    typeofJaathakam=sheet.cell_value(i, 34),country=sheet.cell_value(i, 35),youHaveOwn=sheet.cell_value(i, 36),landinfo=sheet.cell_value(i, 37),
                                    ernakulam=sheet.cell_value(i, 38),thiruvananthapuram=sheet.cell_value(i, 39),kollam=sheet.cell_value(i, 40),
                                    pathanamthitta=sheet.cell_value(i, 41), alappuzha=sheet.cell_value(i, 42),kottayam=sheet.cell_value(i, 43),
                                    idukki=sheet.cell_value(i, 44),thrissur=sheet.cell_value(i, 45),palakkad=sheet.cell_value(i, 46),  
                                    malappuram=sheet.cell_value(i, 47),kozhikode=sheet.cell_value(i, 48),wayanad=sheet.cell_value(i, 49),
                                    kannur=sheet.cell_value(i, 50),kasaragod=sheet.cell_value(i, 51))

        with app.app_context():
            db.session.add(addDetails)
            db.session.commit()
    print("Data added")
                
       

test_connection(self=None)
create_admin(self=None)
load_details(self=None)




