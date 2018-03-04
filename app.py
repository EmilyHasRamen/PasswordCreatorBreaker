import random
import sys
# directory for where our database code is
sys.path.append('/Users/cap1/hackthefog/passwordcreatorbreaker/passwordcreator')
import genorator
from genorator import makepassword
from flask import Flask, render_template, send_from_directory, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
	return render_template("main.html")

@app.route("/makepassword", methods=["GET", "POST"])
def generate():
	if request.method == "POST":
		numwords = int(request.form.get('num'))
		# digitlen = int(request.form.get('digit'))
		genpassword_ = genorator.makepassword(4, numwords)
		return render_template("main.html", genpassword=genpassword_)
	elif request.method == "GET":
		return render_template("main.html", genpassword="Something went wrong...")
if __name__ == "__main__":
	app.run()