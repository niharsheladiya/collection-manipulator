

---

# 📚 Collection Manipulator — Student Data Organizer

A beginner-friendly Python console application designed to manage student records using fundamental Python collection types (**Lists** and **Dictionaries**). This interactive menu-driven program supports full **CRUD** (Create, Read, Update, Delete) operations in memory.

---

## 🎥 Live Demo Video Link

[Watch the live demo here](https://drive.google.com/file/d/1F1fbPnFdeJwXe0O-rTmbRza5Q6hrTnjr/view?usp=sharing) 
---

## 📌 Objective

Develop an interactive **Student Data Organizer** application in Python that processes and manages student records using primary collection data structures. This project demonstrates practical knowledge of:

* **Python Collections**: Nested structures using `lists` and `dictionaries`
* **Control Flow**: Infinite `while` loops and `if-elif-else` conditional statements
* **CRUD Operations**: Adding, retrieving, updating, and removing entries
* **User Interaction**: Dynamic CLI input prompts and formatted output displays

---

## ✅ Features & Functionality

### 1. ➕ Add Student

* Prompts for details: `Student ID`, `Name`, `Age`, `Grade`, `Date of Birth (YYYY-MM-DD)`, and `Subjects`.
* Bundles inputs into a structured Python `dict` and appends it to the global `students` list.

### 2. 📋 Display All Students

* Iterates through the stored list of dictionaries.
* Formats and prints comprehensive profiles for all currently registered students.

### 3. ✏️ Update Student Information

* Searches for a student by their unique `Student ID`.
* Overwrites and updates record fields (`Name`, `Age`, `Grade`, `DOB`, `Subjects`) directly in memory.

### 4. 🗑️ Delete Student Record

* Locates student entries by `Student ID`.
* Safely removes the matching record from the `students` collection list.

### 5. 📚 Display Offered Subjects

* Extracts and displays subject allocations stored across student records.

### 6. 🚪 Exit Program

* Displays a thank-you message and gracefully terminates the continuous menu loop.

---

## 🔄 Program Flow

1. **Welcome & Main Menu** — Displays available menu choices (1 through 6).
2. **User Input** — Captures user choice and routes to the corresponding CRUD action.
3. **Data Manipulation** — Performs list/dictionary mutations (append, read, modify keys, or remove elements).
4. **Console Output** — Displays clean status messages confirming operations (e.g., *"Student Added successfully!"*).
5. **Looping Execution** — Repeats until the user chooses option `6` to exit.

---

## 💻 Example Console Interaction

> welcom to the student data organizer!
> 
> select an option:
> 
>1.Add Student
> 
>2.Display All students
> 
> 3.Update Student Information
> 
> 4.Delete Student
> 
> 5.Display offered subjects
> 
> 6.exit
> 
> Enter Your Choice: 1
> 
> Enter student details:
> 
> Enter Student ID: 11
> 
> Enter Name: nihar
> 
> Enter Age: 18
> 
> Enter Grade: a
> 
> Date of Birth (YYYY-MM-DD): 2008-06-15
> 
> Enter Subjects(comma-separated): maths
> 
> Student Added succesfully!
> 
> select an option:
> 
> 1.Add Student
> 
> 2.Display All students
> 
> 3.Update Student Information
> 
> 4.Delete Student
> 
> 5.Display offered subjects
> 
> 6.exit
> 
> Enter Your Choice: 2
> 
> ---Display All students---
> 
> Student_id: 11
> 
> name: nihar
> 
> age: 18
> 
> grade: a
> 
> subjects: maths
> 
> select an option:
> 
> 1.Add Student
> 
> 2.Display All students
> 
> 3.Update Student Information
> 
> 4.Delete Student
> 
> 5.Display offered subjects
> 
> 6.exit
> 
> Enter Your Choice: 3
> 
> Enter Student Id: 11
> 
> Enter New Name: jal
> 
> Enter New Age: 19
> 
> Enter New Grade: b
> 
> Enter New Dob: 2009-06-16
> 
> Enter New Subjects: english
> 
> Student Details Update Successfully!

💡 **Note:** All student records are stored in volatile memory (`RAM`). Rerunning the script resets stored collections back to default.

---

## 🚀 How to Run

1. **Prerequisites**: Ensure you have **Python 3.x** installed on your system.
2. **Execute the script**:
> python collection_manipulator.py


*(No external third-party packages required — runs purely on Python standard libraries!)*

---

## 📂 Project Structure

> Collection-Manipulator/
> ├── collection_manipulator.py
>  # Main Python CLI application source code
> └── README.md
> # Project documentation and details

---

## 🧠 Assumptions Made

* **Unique Identification**: Each student is assumed to have a unique `Student ID` string for updates and deletions.
* **In-Memory Storage**: Data persists only for the duration of the execution session (no database or file persistence required for this assignment scope).
* **Input Format**: Users are assumed to input valid menu numbers and appropriate string values.

---

## 📝 Academic Integrity

This project was completed independently as part of the **Collection Manipulator** project module. All code written reflects original work adhering to assignment specifications.

---

*Collection Manipulator — Python - Data Science*

**"Bring on your coding attitude — skills for scaling higher!"**

**Program by Nihar Sheladiya**
