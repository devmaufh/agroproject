from flask import Flask
from flask import render_template
from flask import request
from degreedays import DegreeDays
from request_station import ReqTemperature
 
app=Flask(__name__)

@app.route('/')
def index():
    temps=ReqTemperature()
    tmin=temps.get_tmin()
    tmax=temps.get_tmax()
    return render_template('index.html',tmin=tmin,tmax=tmax)

#Redirect to result
@app.route('/result', methods=['GET','POST'])
def result(result=None):
    if request.method=='POST' or request.method=='GET':
        result=DegreeDays(float(request.form['tu']),float(request.form['tl']),float( request.form['tmax']),float(request.form['tmin'])).define_case()
        return render_template('result.html',result=result)
    return render_template('result.html')

#Main      
if __name__ == "__main__":
    app.run()
