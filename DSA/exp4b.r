student_grades <- data.frame ( 
studentID = c(101, 102, 103, 104, 105, 106), 
name = c("Alice", "Bob", "Charlie", "David", "Eva", "Frank"), 
courseID = c("CS101", "CS101", "CS102", "CS102", "CS103", "CS101"), 
grade = c(90, 85, 78, 92, 88, 84), 
semester = c("Fall", "Fall", "Spring", "Spring", "Fall", "Fall") )

# Retrieve the data for students who took course "CS101" in the "Fall" semester and have a grade greater than or equal to 85.
print(subset(student_grades, courseID=="CS101" & semester=="Fall" & grade >=85))

# Calculate the average grade for each course (courseID) in the dataset.
print(aggregate(grade ~ courseID, data= student_grades, FUN=mean))

# Create a new column called grade_category that classifies the grades into "A" for grades ≥ 90, "B" for grades between 80 and 89, and "C" for grades below 80.
student_grades$grade_category = ifelse(student_grades$grade >= 90, "A", ifelse(student_grades$grade >= 80, "B", "C"))
print(student_grades)

# Sort the student_grades data frame by grade in descending order and display the result.
print(student_grades[order(-student_grades$grade), ])

# Find the number of students in each course (courseID) who scored an "A" grade (grade ≥ 90).
a_grade = subset(student_grades, student_grades$grade >= 90)
count_a_grade = table(a_grade$courseID)
print(count_a_grade)
