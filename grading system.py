subject1=int(input("Enter marks of subject 1: "))
subject2=int(input("Enter marks of subject 2: "))                   
subject3=int(input("Enter marks of subject 3: "))
subject4=int(input("Enter marks of subject 4: "))
subject5=int(input("Enter marks of subject 5: "))
total_marks=subject1+subject2+subject3+subject4+subject5
print("Total marks obtained: ",total_marks) 
percentage=float((total_marks/500)*100)
print("Percentage: ",percentage)
if percentage>=90:
    print("Grade: A+")          
elif percentage>=80 and percentage<90:              
    print("Grade: A")
elif percentage>=70 and percentage<80:
    print("Grade: B")
elif percentage>=60 and percentage<70:
    print("Grade: C")
elif percentage>=50 and percentage<60:
    print("Grade: D")
elif percentage>=40 and percentage<50:
    print("Grade: E")
else:
    print("Grade: F")
# The code takes marks of 5 subjects as input, calculates total marks and percentage, and assigns a grade based on the percentage.


