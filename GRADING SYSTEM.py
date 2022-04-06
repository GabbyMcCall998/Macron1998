#MY GRADING SYSTEM
raw_input=input

for i in range(0,1):
    print('Analytical Geometry & calculus '.upper())
    print('Enter Exam score')
    grade=int(raw_input())
    print('enter credit hour'.title())
    y=int(raw_input())
   # while  y>=1 or y<=3:
    if grade >=80:
        lettergrade = "A"
        gpa=4.0*y
    elif grade >= 75:
        lettergrade = "B+"
        gpa=3.5*y
    elif grade >= 70:
        lettergrade = "B"
        gpa=3.0*y
    elif grade >= 65:
        lettergrade = "c+"
        gpa=2.5*y
    elif grade >= 60:
        lettergrade = "C"
        gpa=2.0*y
    elif grade >= 55:
        lettergrade = "D+"
        gpa=1.5*y
    elif grade >= 50:
        lettergrade = "D"
        gpa=1.0*y
    elif grade <= 49:
        lettergrade = "E"
        gpa=0.5*y
    else:
        print('did not recognise input')
print('your letter grade is:'.upper()  +    lettergrade+'\nYOUR GPA IS ' +   str(gpa))
                
            
