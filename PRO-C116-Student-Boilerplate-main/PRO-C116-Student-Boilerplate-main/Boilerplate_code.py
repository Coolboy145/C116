#Importing flask module in the project
from flask import Flask,render_template

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/")

#‘/’ URL is bound with first_flask function.
def first_flask():

    return "This is my first flask program"
@app.route("/index")
def student_webpage():
    name = "Daniel"
    return render_template("index.html",student_name = name)
#run the application on local server
app.run(debug = True)
