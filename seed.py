from app.database import SessionLocal, engine
from app import models

models.Base.metadata.create_all(bind = engine)



def seed_data():

    with SessionLocal() as db:


        if db.query(models.User).first():
            print("Database already contains data.")
            return


        faculty1 = models.User(name = "Prof. Surendra",email="surendra@college.edu",role = models.RoleEnum.faculty)
        faculty2 = models.User(name = "Prof. Swathi",email="swathi @college.edu",role = models.RoleEnum.faculty)

        db.add_all([faculty1,faculty2])
        db.commit()

        students = [
            models.User(name="Rahul", email="rahul@college.edu", role=models.RoleEnum.student, section="BCA-A"),
            models.User(name="Priya", email="priya@college.edu", role=models.RoleEnum.student, section="BCA-A"),
            models.User(name="Amit", email="amit@college.edu", role=models.RoleEnum.student, section="BCA-A"),
            models.User(name="Neha", email="neha@college.edu", role=models.RoleEnum.student, section="BCA-A"),
            models.User(name="Vikram", email="vikram@college.edu", role=models.RoleEnum.student, section="BCA-B"),
        ]

        db.add_all(students)
        db.commit()

        sub1 = models.Subject(name="Python Web Development", faculty_id=faculty1.id)
        sub2 = models.Subject(name="Database Management", faculty_id=faculty2.id)

        db.add_all(([sub1,sub2]))
        db.commit()

        print("Dummy data seeded successfully!")


if __name__ == "__main__":
    seed_data()

