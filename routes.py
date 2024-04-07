from app import app
from flask import render_template, request, redirect
import users, workouts

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/select_movements")
def select_movements():
    return render_template("select_movements.html")

@app.route("/new_workout", methods=["POST"])
def new_workout():
    movements = request.form.getlist("movement")
    return render_template("new_workout.html", movements=movements)

@app.route("/add_set")
def add_set():
    return render_template("add_set.html")

@app.route("/save_set", methods=["POST"])
def save_set():
    #repetitions = request.form["repetitions"]
    #weight = request.form["weight"]
    #rpe = request.form["rpe"]
    #workouts.save_set(movement_in_workout_id,repetitions, weight, rpe)
    return redirect("/new_workout")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eivät täsmää")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti epäonnistui")