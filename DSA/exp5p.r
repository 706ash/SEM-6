# Load the mtcars dataset
data(mtcars)

# 1. Obtain the structure of the mtcars dataset
str(mtcars)

# 2. Display the entries in the hp (horsepower) and mpg (miles per gallon) columns
mtcars[, c("hp", "mpg")]

# 3. Display the count of the number of entries where the number of cylinders (cyl) is 6
sum(mtcars$cyl == 6)

# 4. Display details of the mtcars dataset ordered by mpg in descending order
mtcars[order(-mtcars$mpg), ]

# 5. Create a copy of the mtcars dataset and name it df_mtcars
df_mtcars <- mtcars
print(df_mtcars)

# 6. Select the max and min values under hp (horsepower)
max(df_mtcars$hp)
min(df_mtcars$hp)

# 7. Select all observations where wt (weight) is greater than 3.5
subset(df_mtcars, wt > 3.5)

# 8. Select all entries with 6 cylinders (cyl == 6) whose horsepower (hp) is larger than the average horsepower
subset(df_mtcars, cyl == 6 & hp > mean(df_mtcars$hp))

# 9. Find the average mpg for all entries with 4 cylinders (cyl == 4) that have hp smaller than 100
mean(subset(df_mtcars, cyl == 4 & hp < 100)$mpg)

# 10. Update all entries with 8 cylinders (cyl == 8) to have wt (weight) equal to 5
df_mtcars$wt[df_mtcars$cyl == 8] <- 5
print(mtcars)
