a = data.frame(
    name = c("Anna", "Dina", "Katty", "Johnny", "James", "Lotty", "Polly"),
    score = c(12.5, 9, 16.5, 12, 20, 14.5, 19),
    attempts = c(1, 3, 2, 1, 3, 2, 1),
    qualify = c("yes", "no", "yes", "no", "yes", "no", "yes")
)

#Structure of the data frame
print(str(a))

summary(a)

print(a["score"])

print(a[c(3, 5), c(1, 3)])

Address = c("Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore", "Hyderbad", "Panaji")  
a = cbind(a, Address)
print(a)

new_row = data.frame(name = "Rahul", score="13.2", attempts="2", qualify="yes", Address="Vasco")
a = rbind(a, new_row)
print(a)
