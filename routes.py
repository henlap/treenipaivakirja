from app import app
from flask import render_template, request, redirect, session
import users, workouts

@app.route("/")
def index():
    user_id = users.user_id()
    count = workouts.count_workouts(user_id)
    return render_template("index.html",count=count)

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

@app.route("/new_workout", methods=["GET","POST"])
def new_workout():
    if request.method == "POST":
        movements = request.form.getlist("movement")
        session["movements"] = movements
        date = request.form["date"]
        if not workouts.new_workout(date):
            return render_template("error.html", message="Kirjaaminen epäonnistui")
        for movement in movements:
            workouts.add_movement(movement)
    if request.method == "GET":
        movements = session.get("movements")
    
    workout_id = workouts.workout_id()
    sets = workouts.get_sets(workout_id)
    count = len(sets)
    return render_template("new_workout.html", movements=movements, count=count, sets=sets)
        
@app.route("/add_set", methods=["POST"])
def add_set():
    movement = request.form["movement"]
    return render_template("add_set.html", movement=movement)

@app.route("/save_set", methods=["POST"])
def save_set():
    movement = request.form["movement"]
    repetitions = request.form["repetitions"]
    weight = request.form["weight"]
    rpe = request.form["rpe"]
    workouts.save_set(movement, repetitions, weight, rpe)
    return redirect("/new_workout")

@app.route("/save_workout")
def save_workout():
    del session["movements"]
    del session["workout_id"]
    return redirect("/")

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
        
@app.route("/show_workouts")
def show_workouts():
    user_id = users.user_id()
    all_workouts = workouts.get_workouts(user_id)
    return render_template("show_workouts.html", all_workouts=all_workouts)