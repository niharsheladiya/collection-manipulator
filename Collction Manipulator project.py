print("welcom to the student data organizer!")

students=[]

while True:
    print("\nselect an option:")
    print("1.Add Student")
    print("2.Display All students")
    print("3.Update Student Information")
    print("4.Delete Student")
    print("5.Display offered subjects")
    print("6.exit")
    choice=int(input("Enter Your Choice:"))

    if choice == 1:
        print("\nEnter student details:")
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        grade=input("Enter Grade:")
        dob=input("Date of Birth (YYYY-MM-DD):")
        subjects = input("Enter Subjects(comma-separated):")

        student = {
                           "id": student_id,
                           "name": name,
                           "age": age,
                           "grade":grade,
                           "date of birth":dob,
                           "subjects": subjects
                                                                 }

        students.append(student)

        print("\nStudent Added succesfully!")
              

    elif choice  == 2:

        for student in students:
            
            print("\n---Display All students---")
            print("Student_id:",student["id"])
            print("name:",student["name"])
            print("age:",student["age"])
            print("grade:",student["grade"])
      
            print("subjects:",student["subjects"])

    elif choice == 3:

        update_id=input("Enter Student Id:")

        for student in students:
            if student["id"]==update_id:
                student["name"] = input("Enter New Name: ")
                student["age"] = input("Enter New Age: ")
                student["grade"] = input("Enter New Grade: ")
                student["dob"] = input("Enter New Dob: ")
                student["subjects"] = input("Enter New Subjects: ")

                print("\nStudent Details Update Successfully!")

    elif choice==4:
        delete_id=input("Enter student id:")
        for student in students:
            if student["id"]==delete_id:
                       students.remove(student)
                       print("\nStudent Deleted Successfully.")

    elif choice==5:
        print("\nStored Subjects:")
        for student in students:
            print(student["subjects"])

    elif choice==6:
        print("\n Exiting Program. thank you!")
        break
    else:
        print("invalid choice.")
