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
                                    weight=sheet.cell_value(i, 2),bloodtype=sheet.cell_value(i, 3),complexion=sheet.cell_value(i, 4),
                                    physcialstatus=sheet.cell_value(i, 5), maritalstatus= sheet.cell_value(i, 6), profileCreatedfor=sheet.cell_value(i, 7),
                                    countryCode=sheet.cell_value(i, 8),prefTimeToCall=sheet.cell_value(i, 8),religion=sheet.cell_value(i, 10),
                                    christianCaste=sheet.cell_value(i, 11),hinduCaste=sheet.cell_value(i, 12),muslimCaste=sheet.cell_value(i, 13),
                                    higestEducation=sheet.cell_value(i, 14),doc=sheet.cell_value(i, 15),master=sheet.cell_value(i, 16),
                                    bachelors=sheet.cell_value(i, 17),diploma=sheet.cell_value(i, 18),tradeSchool=sheet.cell_value(i, 19),
                                    higerSecondary=sheet.cell_value(i, 20),highSchool=sheet.cell_value(i, 21),jobCategory=sheet.cell_value(i, 22),
                                    jobType=sheet.cell_value(i, 23),monthlyIncome=sheet.cell_value(i, 24),eatingHabits=sheet.cell_value(i, 25),
                                    drinkingHabits=sheet.cell_value(i, 26),smokingHabits=sheet.cell_value(i, 27),languagesKnown=sheet.cell_value(i, 28),
                                    hobbies=sheet.cell_value(i, 29),intrests=sheet.cell_value(i, 30),star=sheet.cell_value(i, 31),raasi=sheet.cell_value(i, 32),
                                    typeofJaathakam=sheet.cell_value(i, 33),country=sheet.cell_value(i, 34),youHaveOwn=sheet.cell_value(i, 35),landinfo=sheet.cell_value(i, 36),
                                    ernakulam=sheet.cell_value(i, 37),thiruvananthapuram=sheet.cell_value(i, 38),kollam=sheet.cell_value(i, 39),
                                    pathanamthitta=sheet.cell_value(i, 40), alappuzha=sheet.cell_value(i, 41),kottayam=sheet.cell_value(i, 42),
                                    idukki=sheet.cell_value(i, 43),thrissur=sheet.cell_value(i, 44),palakkad=sheet.cell_value(i, 45),  
                                    malappuram=sheet.cell_value(i, 46),kozhikode=sheet.cell_value(i, 47),wayanad=sheet.cell_value(i, 48),
                                    kannur=sheet.cell_value(i, 49),kasaragod=sheet.cell_value(i, 50))

        with app.app_context():
            db.session.add(addDetails)
            db.session.commit()
    print("Data added")
                
       

test_connection(self=None)
create_admin(self=None)
load_details(self=None)




