from db import db
import users
from flask import request, session
from sqlalchemy.sql import text, func

def new_workout(date):
    user_id = users.user_id()
    if user_id == 0:
        return False
    #try:
    sql = text("INSERT INTO workouts (user_id, done_at, sent_at) VALUES (:user_id, :done_at, NOW()) RETURNING id")
    workout_id = db.session.execute(sql,{"user_id":user_id, "done_at": date})
    session["workout_id"] = workout_id.fetchone()[0]
    db.session.commit()
    #except:
        #return False
    return True
    
def save_set(movement_name, repetitions, weight, rpe):
    w_id = workout_id()
    m_id = movement_id(movement_name)

    sql = text("SELECT id FROM movement_in_workout WHERE movement_id=:movement_id AND workout_id=:workout_id")
    result = db.session.execute(sql, {"movement_id":m_id, "workout_id":w_id})
    movement_in_workout_id = result.fetchone()[0]
    try:
        sql = text("INSERT INTO sets (movement_in_workout_id,repetitions, weight, rpe) VALUES (:movement_in_workout_id,:repetitions, :weight, :rpe)")
        db.session.execute(sql, {"movement_in_workout_id":movement_in_workout_id, "repetitions":repetitions, "weight":weight, "rpe":rpe})
        db.session.commit()
    except:
        return False
    return True

def add_set():
    pass

def add_movement(movement_name):
    w_id = workout_id()
    m_id = movement_id(movement_name)

    sql = text("INSERT INTO movement_in_workout (movement_id, workout_id) VALUES (:movement_id, :workout_id)")
    db.session.execute(sql, {"movement_id":m_id, "workout_id":w_id})
    db.session.commit()

def workout_id():
    return session.get("workout_id", 0)

def movement_id(name):
    sql = text("SELECT id FROM movements WHERE name=:name")
    result = db.session.execute(sql, {"name":name})
    return result.fetchone()[0]

def get_sets(workout_id):
    sql = text("""SELECT M.name, S.repetitions, S.weight
                    FROM sets S, movement_in_workout MW, workouts W, movements M
                    WHERE W.id=:workout_id  
                    AND MW.workout_id=W.id
                    AND MW.movement_id=M.id
                    AND S.movement_in_workout_id=MW.id
                    GROUP BY S.id, M.name
                    ORDER BY M.name""")
    result = db.session.execute(sql, {"workout_id":workout_id})
    return result.fetchall()
    
def count_workouts(user_id):
    if user_id == 0:
        return 0
    sql = text("""SELECT COUNT(W.id)
                    FROM users U LEFT JOIN workouts W
                    ON W.user_id=U.id
                    AND U.id=:user_id""")
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchone()[0]

def get_workouts(user_id):
    sql = text("""SELECT W.id, W.done_at
                    FROM users U LEFT JOIN workouts W
                    ON W.user_id=U.id
                    AND U.id=:user_id
                    GROUP BY W.id, W.done_at
                    ORDER BY W.done_at""")
    result = db.session.execute(sql, {"user_id":user_id})
    workouts = []
    for workout in result:
        sets = get_sets(workout[0])
        workouts.append(f"Suoritettu:{workout[1]} {sets}")
    return workouts

def get_movements():
    sql = text("""SELECT M.name
                    FROM movements M
                    ORDER BY M.name""")
    result = db.session.execute(sql)
    return result.fetchall()