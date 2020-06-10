from flask import Flask, render_template
from datetime import datetime 


app = Flask(__name__)
 
@app.route("/")
def hello():
    return render_template("index.html")
 
@app.route("/time_date", methods=['POST'])
def time_date():
    Time=str(datetime.now())
    return "Date and Time is" + Time
 
 
if __name__ == "__main__":
    app.run()