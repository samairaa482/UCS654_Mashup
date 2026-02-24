from flask import Flask,render_template,request
import subprocess
import yagmail
import zipfile
import os
from email_validator import validate_email


app=Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")



@app.route("/submit",
methods=["POST"])

def submit():

    singer=request.form["singer"]

    videos=request.form["videos"]

    duration=request.form["duration"]

    email=request.form["email"]

    try:

        validate_email(email)

    except:

        return "Invalid Email"

    output="output.mp3"

    subprocess.run([

"python",
"101556.py",
singer,
videos,
duration,
output

])

    zipname="result.zip"

    with zipfile.ZipFile(
    zipname,"w") as z:

        z.write(output)

    yag=yagmail.SMTP(

"user@gmail.com",
"APP_PASSWORD")

    yag.send(

    email,

"Your Mashup",

"Attached",

attachments=zipname)

    return "Email Sent!"


app.run(debug=True)