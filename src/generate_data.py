import random
from faker import Faker
from datetime import datetime
from src.config import config
from src.database.database import Database


fake = Faker()
NUM_STUDENTS = 100
NUM_BOOKS = 50
NUM_STAFF = 20

# create database instance
db = Database(config)

# generate students data
for _ in range(NUM_STUDENTS):
    student_id = "00365" + "".join([str(random.randint(0, 9)) for _ in range(5)])
    name = fake.first_name()
    surname = fake.last_name()
    year = random.randint(1, 5)
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=30).isoformat()
    sex = random.choice(["M", "F", "O"])
    email = fake.email()
    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    max_books = config["MAX_BORROWED_BOOKS"]
    
    db.add_user("students", name, surname, email, password, student_id=student_id, year=year, 
                date_of_birth=date_of_birth, sex=sex, max_books=max_books)

# generate books data
for _ in range(NUM_BOOKS):
    title = fake.catch_phrase()
    author = fake.name()
    production_year = random.randint(1980, datetime.now().year)
    total_copies = random.randint(5, 50)
    available_copies = random.randint(0, total_copies)

    db.add_book(title, author, production_year, total_copies, available_copies=available_copies)

# generate staff data
for _ in range(NUM_STAFF):
    name = fake.first_name()
    surname = fake.last_name()
    email = fake.company_email()
    position = fake.job()
    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    sex = random.choice(["M", "F", "O"])
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=60).isoformat()

    db.add_user("staff", name, surname, email, password, position=position, sex=sex, date_of_birth=date_of_birth)
