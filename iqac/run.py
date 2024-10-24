from flask import Flask,render_template,request, redirect,send_from_directory, url_for
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/'

db = SQLAlchemy(app)
app.app_context().push()

class Feedback(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    rating = db.Column(db.Integer(), nullable=True)
    category = db.Column(db.String(length=30), nullable=False)  
    feedbacks = db.Column(db.String(length=200), nullable=False )
     
class Contact_Us(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False )
    email = db.Column(db.String(length=20), nullable=False)  
    messages = db.Column(db.String(length=200), nullable=False )
   

"""""  

class Shops(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Shop_name = db.Column(db.String(length=50), nullable=False )
    F_tag = db.Column(db.String(length=50), nullable=False )  #for food name
    P_tag = db.Column(db.String(length=50), nullable=False )  #for location name
    D_tag = db.Column(db.String(length=50), nullable=False )
    price = db.Column(db.Integer(), nullable=False ) 
    contact_Info = db.Column(db.String(length=50), nullable=False )
    Quality = db.Column(db.String(10), nullable=False )
    location_text = db.Column(db.String(100), nullable=False )
    location_link = db.Column(db.String(200), nullable=False )
    filename = db.Column(db.String(100), nullable=False )


class Ratings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    details = db.Column(db.String(length=50), nullable=False )
    rating = db.Column(db.Float(), nullable=False)

@app.route('/shop_adding_page')
def shop_adding_page():
    return render_template('shop_adding_page.html')
   
    
 

    
"""""

with app.app_context():
    db.create_all()


@app.route('/contact-data')
def contact_data():
    # Querying all the messages from the database
    messages = Contact_Us.query.all()

    # Pass the messages to the template
    return render_template('contact_data.html', messages=messages)
# rendering pages for filling the form

@app.route('/feedback-data')
def feedback_data():
    # Querying all the messages from the database
    feedbacks = Feedback.query.all()

    # Pass the messages to the template
    return render_template('feedback_data.html', feedbacks=feedbacks)
# rendering pages for filling the form

@app.route('/feedback')
def Feedbacks():
    return render_template('feedback.html')

@app.route('/contact_us')
def Contact():
    return render_template('contact.html')




# rendering landing pages

@app.route('/')
@app.route('/about')
def About():
    return render_template('about.html')



 
@app.route('/composition')
def Composition():
    return render_template('composition.html')


@app.route('/functions')
def Functions():
    return render_template('functions.html')

 
@app.route('/reports')
def Reports():
    return render_template('reports.html')
 

@app.route('/contact_data_page',methods=['POST'])
def contact_data_page():
    if request.method == 'POST':
        name = request.form['name']  # Retrieve the name from the form
        email = request.form['email']
        messages = request.form['messages']
         

        if  name and email and messages:
            
            # Create a new record in the database with both name and filename
            new_file = Contact_Us(name=name,email=email,messages=messages)
            db.session.add(new_file)
            db.session.commit()
            
            return render_template('contact.html')
    
    return 'Something went wrong. Please try again.'


 
 
@app.route('/feedback_data_page',methods=['POST'])
def Feedback_data_page():
    if request.method == 'POST':
        rating = request.form['ratingValue']  # Retrieve the name from the form
        fcategory = request.form['fcategory']
        fdetails = request.form['feedback']
         

        if   fcategory and fdetails:
            
            # Create a new record in the database with both name and filename
            new_file = Feedback(rating=rating,  category = fcategory , feedbacks = fdetails)
            db.session.add(new_file)
            db.session.commit()
            
            return render_template('feedback.html')
    
    return 'Something went wrong. Please try again.'



if __name__ == "__main__":
    app.run(debug=True)

