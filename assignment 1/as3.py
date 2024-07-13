# Take input from the user for
subjects = ["Math", "Science", "English", "History", "Geography"]
marks = []
for subject in subjects:
    mark = float(input(f"Enter the marks for {subject}: ")) 
    marks.append(mark)

# Calculate total, average, and grade
total = sum(marks)
average = total / len(subjects)

if average >= 90:
    grade = 'A'

elif average >= 80: 
    grade = 'B'
    
elif average >= 70:
    grade = 'C'

elif average >= 60:
    grade = 'D'

else:
    grade = 'F'

# Print the results
print(f"Total Marks: {total}")
print(f"Average Marks: {average}") 
print(f"Grade: {grade}")