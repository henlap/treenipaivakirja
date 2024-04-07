from db import db
import users
from flask import request
from sqlalchemy.sql import text

def new_workout():
    movements = request.form.getlist("movement")
    return movements

def save_set(movement_in_workout_id,repetitions, weight, rpe=-1):
    try:
        sql = text("INSERT INTO sets (movement_in_workout_id,repetitions, weight, rpe) VALUES (:movement_in_workout_id,:repetitions, :weight, :rpe)")
        db.session.execute(sql, {"movement_in_workout_id":movement_in_workout_id, "repetitions":repetitions, "weight":weight, "rpe":rpe})
        db.session.commit()
    except:
        return False
    return True