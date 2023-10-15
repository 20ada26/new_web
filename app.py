from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengalure, India',
    'Salary':'Rs 5,00,000'
  },
 {
    'id':2,
    'title':'Data Scientest',
    'location':'Chennai, India',
    'Salary': 'Rs 7,00,000'
  },
  {
    'id':3,
    'title':'Back End Developer',
    'location':'Mumbai, India',
    'Salary': 'Rs 6,50,000'
  },
  {
    'id':4,
    'title':'Front End Developer',
    'location':'Remote',
    'Salary': 'Rs 8,50,000'
  }
]

@app.route("/")
def hello_world():
    return render_template("home.html",jobs = JOBS,company='Gravity')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  