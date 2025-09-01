from flask import Flask, render_template, request, redirect
from models import db, Student, Meal, HealthRecord, Lesson
from sqlalchemy import func

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///feeding.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    # Totals
    meals = Meal.query.count()
    students = Student.query.count()
    lessons = Lesson.query.count()

    # Meals chart
    meal_data = Meal.query.all()
    meal_labels = [m.date for m in meal_data]
    meal_values = [m.students_served for m in meal_data]

    # Health chart (average weight per date)
    health_data = (
        db.session.query(HealthRecord.date, func.avg(HealthRecord.weight))
        .group_by(HealthRecord.date)
        .all()
    )
    health_labels = [str(h[0]) for h in health_data]
    health_values = [round(h[1], 1) for h in health_data]

    return render_template(
        "index.html",
        meals=meals,
        students=students,
        lessons=lessons,
        meal_labels=meal_labels,
        meal_values=meal_values,
        health_labels=health_labels,
        health_values=health_values
    )

# --- Meals ---
@app.route("/meals", methods=["GET", "POST"])
def meals():
    if request.method == "POST":
        new_meal = Meal(
            date=request.form["date"],
            food_type=request.form["food_type"],
            students_served=request.form["students_served"]
        )
        db.session.add(new_meal)
        db.session.commit()
        return redirect("/meals")
    all_meals = Meal.query.all()
    return render_template("meals.html", meals=all_meals)

# --- Students ---
@app.route("/students", methods=["GET", "POST"])
def students():
    if request.method == "POST":
        new_student = Student(
            name=request.form["name"],
            age=request.form["age"],
            grade=request.form["grade"]
        )
        db.session.add(new_student)
        db.session.commit()
        return redirect("/students")
    all_students = Student.query.all()
    return render_template("students.html", students=all_students)

# --- Health Records ---
@app.route("/health", methods=["GET", "POST"])
def health():
    students = Student.query.all()
    if request.method == "POST":
        new_record = HealthRecord(
            student_id=request.form["student_id"],
            date=request.form["date"],
            weight=request.form["weight"],
            height=request.form["height"]
        )
        db.session.add(new_record)
        db.session.commit()
        return redirect("/health")
    all_records = HealthRecord.query.all()
    return render_template("health.html", records=all_records, students=students)

# --- Lessons ---
@app.route("/lessons", methods=["GET", "POST"])
def lessons():
    if request.method == "POST":
        new_lesson = Lesson(
            title=request.form["title"],
            content=request.form["content"]
        )
        db.session.add(new_lesson)
        db.session.commit()
        return redirect("/lessons")
    all_lessons = Lesson.query.all()
    return render_template("lessons.html", lessons=all_lessons)

if __name__ == "__main__":
    app.run(debug=True)
