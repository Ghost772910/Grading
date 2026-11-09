students = []

while True:
    print("\n--- Student Grading System ---")
    print("1. Add student")
    print("2. Display all")
    print("3. Class summary")
    print("4. Exit")
    
    option = input("Choose 1-4: ").strip()
    
    if option == "1":
        while True:
            student_number = input("Enter student number: ").strip()
            if student_number != "":
                break
            print("Error: Student number cannot be blank.")
            
        while True:
            name = input("Enter student name: ").strip()
            if name != "":
                break
            print("Error: Student name cannot be blank.")
        
        while True:
            mark_str = input("Enter student mark (0-100): ").strip()
            try:
                mark = float(mark_str)
                if 0 <= mark <= 100:
                    break
                else:
                    print("Error: Mark must be between 0 and 100.")
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")
                
        if mark >= 80:
            grade = "A"
            decision = "Excellent"
        elif mark >= 70:
            grade = "B"
            decision = "Very good"
        elif mark >= 60:
            grade = "C"
            decision = "Good"
        elif mark >= 50:
            grade = "D"
            decision = "Pass"
        else:
            grade = "F"
            decision = "Fail"
            
        student_record = {
            "student_number": student_number,
            "name": name,
            "mark": mark,
            "grade": grade,
            "decision": decision
        }
        students.append(student_record)
        print(f"Success! {name} has been added with a grade of {grade} ({decision}).")
        
    elif option == "2":
        if not students:
            print("\nNo student records available to display.")
        else:
            print("\nstudent records")
            for s in students:
                print(f"{s['student_number']} | Name: {s['name']} | Mark: {s['mark']} | Grade: {s['grade']} | Decision: {s['decision']}")
                
    elif option == "3":
        if not students:
            print("\nCannot generate a summary because there are no student records.")
        else:
            total_students = len(students)
            
            total_marks = 0
            highest_mark = students[0]["mark"]
            lowest_mark = students[0]["mark"]
            passes = 0
            fails = 0
            
            for s in students:
                mark = s["mark"]
                total_marks += mark
                
                if mark > highest_mark:
                    highest_mark = mark
                if mark < lowest_mark:
                    lowest_mark = mark
                    
                if mark >= 50:
                    passes += 1
                else:
                    fails += 1
                    
            average = total_marks / total_students
            
            print("\n--- Class Summary ---")
            print(f"Total Students: {total_students}")
            print(f"Class Average:  {average:.2f}")
            print(f"Highest Mark:   {highest_mark}")
            print(f"Lowest Mark:    {lowest_mark}")
            print(f"Total Passes:   {passes}")
            print(f"Total Fails:    {fails}")
            
    elif option == "4":
        print("Exiting system.")
        break
        
    else:
        print("Please choose a number between 1 and 4.")