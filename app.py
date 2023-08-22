from flask import Flask

#create flask app
app = Flask(__name__)

#define a route and function for the home page
@app.route('/')
def hello():
  return "Hello, Flask"

#Run the file if the file is the main script
if __name__== '__main__':
    app.run(debug=True)
    