from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
     return render_template("home.html")

# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=8080,host='0.0.0.0')
