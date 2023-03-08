from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade
import os
from flask_security import roles_accepted, auth_required, logout_user, Security,SQLAlchemyUserDatastore
from datetime import datetime


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://bankroute:Salahf98@inlbank22.mysql.database.azure.com/bank'
# db.app = app
# db.init_app(app)
# migrate = Migrate(app,db)
app.config['SECRET_KEY'] = os.urandom(32)

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", 'pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw')
app.config['SECURITY_PASSWORD_SALT'] = os.environ.get("SECURITY_PASSWORD_SALT", '146585145368132386173505678016728509634')
app.config["REMEMBER_COOKIE_SAMESITE"] = "strict"
app.config["SESSION_COOKIE_SAMESITE"] = "strict"
app.config['SECURITY_RECOVERABLE'] = True
# app.security = Security(app, user_datastore)

@app.route('/')
def start():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact',methods=['GET','POST'])
def contact():
    return render_template('contact.html')

@app.route('/projects')
def project():
    return render_template('projects.html')


if __name__  == "__main__":
    with app.app_context():
        app.run(debug=True)