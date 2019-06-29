import os
from flask import render_template, request

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.pop('user_id', None)
    return render_template("success.html")

@app.route("/auth", methods=["POST"])
def auth():
    # Forget any user_id

    user = request.form.get("user")
    password = request.form.get("password")
    if db.execute("SELECT * FROM accounts WHERE users = :id AND passwords = :pass" , {"id": user,"pass":password}).rowcount == 0:
        return render_template("error.html", message="No such User with that id.")
    else:
        # session["user_id"]=db.execute("SELECT id FROM accounts where users=:id",{"id":user})
        return render_template("success.html")

@app.route("/insert", methods=["POST"])
def insert():
    user = request.form.get("user")
    password = request.form.get("password")
    if db.execute("SELECT * FROM accounts WHERE users = :id" , {"id": user}).rowcount != 0:
        return render_template("error.html", message="Userid not available.")


    # Make sure valid characters.
    if len(user)<0 or len(password)<0:
        return render_template("error.html", message="please enter proper user id and password")
    db.execute("INSERT INTO accounts (users,passwords ) VALUES (:user, :password)",
            {"user": user, "password": password})
    db.commit()
    return render_template("success.html")
