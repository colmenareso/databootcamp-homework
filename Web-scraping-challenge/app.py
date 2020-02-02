# Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import web_scrape


# create instance of Flask app
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_find = mongo.db.collection.find_one()
    
    # Return template and data
    return render_template("index.html", mars_show=mars_find)
    

@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = web_scrape.scrape()
    
    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)
    
    
    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)