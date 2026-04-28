class Student:
    def __init__(self,student_id,name,class_,subjects):
        self.student_id=student_id
        self.name=name
        self.class_=class_
        self.subjects=subjects
    def display(self):
        print(self.student_id,self.name)

class Teacher:
    def __init__(self,teacher_id,name,class_,subject):
        self.teacher_id=teacher_id
        self.name=name
        self.class_=class_
        self.subject=subject
    def display(self):
        print(self.teacher_id,self.name)

class Marks:
    def __init__(self,marks,student_id,subject):
        self.marks=marks
        self.student_id=student_id
        self.subject=subject

class Grade:
    def __init__(self,grade,gp,student_id,subject):
        self.grade=grade
        self.gp=gp
        self.student_id=student_id
        self.subject=subject

class StudentResultManagement:  #encap
    def __init__(self):
        self.students=[]
        self.teachers=[]
        self.marks=[]
        self.__grades=[]

    def add_student(self,student_id,name,class_,subjects): #student details are added
        student=Student(student_id,name,class_,subjects)  #abstraction
        if student in self.students:
            print("Record already exists")  #E2: Duplicate entry error
        self.students.append(student)
        print(f"student {student.name} - {student.student_id} added successfully!")

    def add_teacher(self,teacher_id,name,class_,subject): #teacher can select their class and subjects
        teacher=Teacher(teacher_id,name,class_,subject)  
        self.teachers.append(teacher)
        print(f"Teacher {teacher.name} added successfully!")

    def grade_calc(self,grade,student_id,subject):  #calculate grade points using grades
        if grade in "O":
            gp=10
        elif grade in "A+":
            gp=9
        elif grade in "A":
            gp=8
        elif grade in "B+":
            gp=7
        elif grade in "B":
            gp=6
        elif grade in "C":
            gp=5
        else:
            gp=0
        grade=Grade(grade,gp,student_id,subject)
        self.__grades.append(grade)
        print("Grades Appended successfully!")
        


    def enter_marks(self,marks,student_id,subject):  #claculate grades using marks
        marks_=Marks(marks,student_id,subject)
        if marks_.marks>=0 and marks_.marks<=100:
            self.marks.append(marks_)
            if marks_.marks<40:
                grade="F"
            elif marks_.marks>=40 and marks_.marks<=49:
                grade="C"
            elif marks_.marks>=50 and marks_.marks<=59:
                grade="B"
            elif marks_.marks>=60 and marks_.marks<=69:
                grade="B+"
            elif marks_.marks>=70 and marks_.marks<=79:
                grade="A"
            elif marks_.marks>=80 and marks_.marks<=89:
                grade="A+"
            else:
                grade="O"
            self.grade_calc(grade,student_id,subject)
            
        else:
            print("Invalid marks value")  #E1: Invalid marks value error
        
        
        
    def find_student(self,student_id): #to find the student details
        for student in self.students:
            if student.student_id==student_id:
                print(student.student_id,
                      student.name,
                      student.class_,
                      student.subjects
                )
                return "found"
            else:
                print("Student ID not found")   #E3: Student ID not found error
            
    def find_teacher(self,teacher_id):  #to find the teacher details
        for teacher in self.teachers:
            if teacher.teacher_id==teacher_id:
                print(teacher.teacher_id,
                      teacher.name,
                      teacher.class_,
                      teacher.subject
                )
                return "found"
            else:
                print("Teacher ID not found")   #E3: Teacher ID not found error
            
    def view_grades(self,student_id,subject):  #to view grades
        for gd in self.__grades:
            if gd.student_id==student_id and gd.subject==subject:
                return (gd.student_id,
                      gd.grade,
                      gd.gp,
                      gd.subject
                      )
            else:
                print("Student Id NOT found")
                
    def report(self,*args): #generate the report for given student 
        student=Student(*args) #method overloading
        print(f"The report for Student {student.name} - rollno {student.student_id} generated")
        for gd in self.__grades:
            if gd.student_id==student.student_id:
                print(gd.grade,
                      gd.subject,
                      gd.gp
                      )

sm=StudentResultManagement()

sm.add_student(94,"santhosh","CSBS",["DBMS","CN","OOPS") #Student selecting / predefined class and subject enrollment
print(sm.find_student(94)) #To view student details
sm.add_teacher(1,"jake","CSBS","OOPS") #Teacher selecting class and subject
print(sm.find_teacher(1)) #To view teacher details

sm.enter_marks(99,94,"OOPS") #Teacher enter the marks for each subject
print(sm.view_grades(94,"OOPS")) #can view the grade,gradepoints for each sstudent subject-wise
sm.report(94,"santhosh","CSBS",["DBMS","CN","OOPS"]) #REPORT generate

#print(sm.__grades)

print("\n")  #polymorphism
s=Student(94,"santhosh","CSBS",["DBMS","CN","OOPS"])
s.display()
t=Teacher(1,"jake","CSBS","OOPS")
t.display()
