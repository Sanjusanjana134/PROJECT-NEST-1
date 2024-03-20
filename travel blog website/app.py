from flask import Flask, render_template
from pymongo import MongoClient
app = Flask(__name__)

# Configure MongoDB connection
client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB server URI
db = client["travel"]  # Replace with your database name

@app.route('/')
def travel():
    return render_template('travel.html')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/blogpost')
def blogpost():
    return render_template('blogpost.html')

@app.route('/aboutus')
def aboutus():
    # Fetch data from MongoDB (example)
    collection = db['blog']  # Replace with your collection name
    data = collection.find()
    return render_template('aboutus.html', data=data)
@app.route('/')
def not_found():
    return '''
    <!doctype html>
    <html lang="en">
    <title>404 Not Found</title>
    <h1>Not Found</h1>
    <p>The requested URL was not found on the server. If you entered the URL manually, please check your spelling and try again.</p>
    '''

# Rest of your code for add_data and get_data routes

if __name__ == '__main__':
    app.run(debug=True)
