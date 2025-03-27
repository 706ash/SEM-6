library(ggplot2)

students <- data.frame(
  Name = c("Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"),
  Age = c(22, 24, 23, 22, 25, 24, 22, 23, 24, 22),
  Gender = c("F", "M", "M", "M", "F", "M", "F", "F", "M", "F"),
  Score = c(85, 90, 78, 88, 92, 80, 95, 70, 82, 88),
  StudyHours = c(15, 20, 12, 18, 25, 14, 30, 16, 10, 22),
  Difficulty = c("Medium", "Hard", "Medium", "Medium", "Easy", "Hard", "Hard", "Easy", "Easy", "Medium")
)
print(students)

mean_scores <- aggregate(Score ~ Gender, data = students, FUN = mean)
print(mean_scores)

high_scorers <- subset(students, Score > 80)
print(high_scorers)

correlation <- cor(students$StudyHours, students$Score)
print(paste("Correlation between Study Hours and Score:", correlation))

ggplot(students, aes(x = StudyHours, y = Score, color = Difficulty)) +
  geom_point(size = 3) +
  labs(title = "Study Hours vs Score", x = "Study Hours", y = "Score") +
  theme_minimal()

ggplot(students, aes(x = Difficulty, y = Score, fill = Difficulty)) +
  geom_boxplot() +
  labs(title = "Score Distribution Across Difficulty Levels", x = "Difficulty", y = "Score") + theme_minimal()
