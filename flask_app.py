from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://jzdrxkepnwriev:bb15ae170cf6e0c325d5b81a37869f7a8864ffbe5711642f5f125eb7355cfd74@ec2-184-72-223-163.compute-1.amazonaws.com:5432/ddhi8un5q39vjt'
db = SQLAlchemy(app)

engine = db.engine
with engine.connect() as con:

    #response = con.execute('Select * from brewerylocations')
    #print(list(response))

    #response = con.execute('SELECT * FROM brewerylocationsUSA')
    #print(list(response))

    #response = con.execute('SELECT * FROM beerstyle')
    #print(list(response))

@app.route('/')
def showLocations():
   # brewlocations = session.query(brewerylocations).all()
    return render_template("index.html")

@app.route('/brewerylocations')
def brewerylocations():
    response = con.execute('Select * from brewerylocations')
    return "hello \n\n"

if __name__ == '__main__':
    app.run()

# I need my app.route for /brewerylocations to print the response in the return function. I will need an app.route for each response since they are all different tables.