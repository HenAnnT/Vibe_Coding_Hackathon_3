from app import app, db, Student, Meal, HealthRecord, Lesson

with app.app_context():
    # Clear old data
    db.drop_all()
    db.create_all()

    # --- Students ---
    s1 = Student(name="Alice Johnson", age=10, grade="Grade 4")
    s2 = Student(name="Brian Kim", age=12, grade="Grade 6")
    s3 = Student(name="Cynthia Lee", age=9, grade="Grade 3")

    # --- Meals ---
    m1 = Meal(date="2025-08-28", food_type="Rice & Beans", students_served=30)
    m2 = Meal(date="2025-08-29", food_type="Maize Porridge", students_served=28)
    m3 = Meal(date="2025-08-30", food_type="Vegetable Stew & Chapati", students_served=32)

    # --- Health Records ---
    h1 = HealthRecord(student_id=1, date="2025-08-28", weight=32.5, height=138.0)
    h2 = HealthRecord(student_id=2, date="2025-08-28", weight=40.0, height=145.0)
    h3 = HealthRecord(student_id=3, date="2025-08-28", weight=28.0, height=130.0)

    # --- Lessons ---
    l1 = Lesson(title="Why Vegetables Matter", content="Vegetables provide vitamins and help you stay healthy.")
    l2 = Lesson(title="Drink Clean Water", content="Clean water prevents diseases and keeps you strong.")
    l3 = Lesson(title="Balanced Diet", content="A healthy diet includes proteins, carbohydrates, and fruits.")

    # Add to session
    db.session.add_all([s1, s2, s3, m1, m2, m3, h1, h2, h3, l1, l2, l3])
    db.session.commit()

    print("✅ Database seeded with demo data!")
