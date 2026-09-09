while True:
    print("\n--- Basic Computer Programming Course ---")
    Student_number = input("Enter your student number: ")
    Student_name = input("Enter your name: ")

    Prelim_grade = float(input("Enter your prelim grade: "))
    Midterm_grade = float(input("Enter your midterm grade: "))
    Final_grade = float(input("Enter your final grade: "))

    Total_grade = (Prelim_grade * 0.3) + (Midterm_grade * 0.3) + (Final_grade * 0.4)
    rounded_grade = round(Total_grade)

    rating = ""
    equivalent = ""

    if rounded_grade >= 99 and rounded_grade <= 100:
        rating = "1.0"
        equivalent = "Excellent"
    elif rounded_grade >= 96 and rounded_grade <= 98:
        rating = "1.25"
        equivalent = "Excellent"
    elif rounded_grade >= 93 and rounded_grade <= 95:
        rating = "1.5"
        equivalent = "Very Satisfactory"
    elif rounded_grade >= 90 and rounded_grade <= 92:
        rating = "1.75"
        equivalent = "Very Satisfactory"
    elif rounded_grade >= 87 and rounded_grade <= 89:
        rating = "2.0"
        equivalent = "Satisfactory"
    elif rounded_grade >= 84 and rounded_grade <= 86:
        rating = "2.25"
        equivalent = "Satisfactory"
    elif rounded_grade >= 81 and rounded_grade <= 83:
        rating = "2.5"
        equivalent = "Fairly Satisfactory"
    elif rounded_grade >= 78 and rounded_grade <= 80:
        rating = "2.75"
        equivalent = "Fairly Satisfactory"
    elif rounded_grade >= 75 and rounded_grade <= 77:
        rating = "3.0"
        equivalent = "Passed"
    elif rounded_grade >= 73 and rounded_grade <= 74:
        rating = "4.0"
        equivalent = "Conditional"
    elif rounded_grade >= 0 and rounded_grade <= 72:
        rating = "5.0"
        equivalent = "Failed"

    print("\nBasic Computer Programming")
    print("Student's Grade Computation")
    print("Student Number: ", Student_number)
    print("Student Name: ", Student_name)

    if rounded_grade >= 75:
        print("\nCongratulations! You successfully PASSED the course.")
    else:
        print("\nSorry! You FAILED the course. Better luck next time.")

    print("Grade Details:")
    print("Prelim: ", Prelim_grade)
    print("Midterm: ", Midterm_grade)
    print("Final: ", Final_grade)
    print(f"Rating: {Total_grade:.2f}")
    print("Equivalent: ", rating)
    print("Remarks: ", equivalent)

    continue_prompt = input("\nDo you want to compute another student's grade? (yes/no): ").strip().lower()
    if continue_prompt != 'yes' and continue_prompt != 'y':
        print("Exiting program. Goodbye!")
        break