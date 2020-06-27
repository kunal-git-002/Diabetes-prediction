#jay mataji
#diabetes flask app
from flask import Flask,render_template,url_for,redirect,flash,request
from sklearn.externals import joblib

###
model=joblib.load("diabetes_model_joblib")

def model_op(preg,glu,bp,th,ins,bmi,deg,age):  
    x=model.predict([[preg,glu,bp,th,ins,bmi,deg,age]])
    for i in x:
        a=i         
    if a==0:
        output=a               
    elif a==1:
        output=a       
    return output



app=Flask( __name__)

@app.route("/")

def Home():
    return render_template("home.html")

@app.route("/diabetes_prediction",methods=["GET","POST"])
def Dib_pred():
    
    global result
    
    if request.method=="POST":
        if not request.form['age'] or not request.form['preg'] or not request.form['glu'] or not request.form['bp'] or not request.form['th'] or not request.form['ins'] or not request.form['bmi'] or not request.form['degree']:
            return "plzz fill all the data !!!"
        
        else:
            
            preg=int((request.form["preg"]))
            glucose=int((request.form["glu"]))
            bp=int((request.form["bp"]))
            thickness=int((request.form["th"]))
            insulin=int((request.form["ins"]) )           
            bmi=float((request.form["bmi"]))
            degree=float((request.form["degree"]))
            age=int((request.form["age"]))

            
            result=(model_op(preg,glucose,bp,thickness,insulin,bmi,degree,age))
            
            
            return redirect(url_for("output"))
            
            
    return render_template("diabetes_pred.html")

@app.route("/output")
def output():
    if result==1:
        a="Oh no !!! you have Diabetes"
    elif result==0:
        a="you don't have Diabetes "
        
    return render_template("show_result.html",data=a)

@app.route("/project_details")
def Proj_details():
    return render_template("project_details.html")




if __name__=="__main__":
    app.run()
