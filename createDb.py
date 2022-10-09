from app import app, db 
from flask import Flask, render_template, request, redirect, url_for
import app as APP


def test_connection(self):
    with app.app_context():
        db.create_all() 
        print("Database created")

def create_admin(self):
    with app.app_context():
        userDetails = APP.UserDetails(name="admin",password="admin123",email="admin123@admin.com" ,profileId="admin1",userRole="admin",gender="none",
                                                dob="none",phoneNumber="0000000000",
                                                religion="none",caste="none")
        try:
            db.session.add(userDetails)
            db.session.commit()
            print("Admin created")
            
        except:
            print("There was an issue adding your task")
    








test_connection(self=None)
create_admin(self=None)

