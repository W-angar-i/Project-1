def get_data():
    students = {}
    
    num_students = int(input("Enter the number of students: "))
    
    for _ in range(num_students):
        name = input("Enter student's name: ").capitalize()
        
        assignment_marks = []
        print(f"Enter 3 assignment marks for {name}:")
        for i in range(3):
            mark = float(input(f"Assignment {i} mark: "))
            assignment_marks.append(mark)
        
        exam_marks = []
        print(f"Enter 2 exam marks for {name}:")
        for i in range(2):
            mark = float(input(f"Exam {i} mark: "))
            exam_marks.append(mark)
        
        students[name] = {
            'assignment_marks': assignment_marks,
            'exam_marks': exam_marks
        }
    
    return students

def Display_results(students):    
    """This function takes dictionary students which have been returned by the 'get_data' function
    Printing the dictionary
    name: represents the key
    marks: represents the value in students assignments and marks
    """
    for name, marks in students.items():
        """We use f-string to allow variables to be passed using curly braces '{}' """
        print(f"Student: {name}, Assignment Marks: {marks['assignment_marks']}, Exam Marks: {marks['exam_marks']}")
        print()
        """The purpose of this print() is to separate the students information by printing empty line. Acts like a space"""

# students variable will contain the student data, in dictionary format
#Display_results is the function that is being called and the dictionary is passed to it
students = get_data()
Display_results(students)