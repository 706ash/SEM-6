# ADDITION OF VECTORS
print("Enter a vector: ")
vector1 = scan()
print("Enter another of the same dimensions: ")
vector2 = scan()
ifelse(length(vector1) != length(vector2),print("Dimension error"), print(vector1+vector2))

#SUM, MEAN, PRODUCT OF VECTOR
print("Enter a vector: ")
vector1 = scan()

cat("SUM: ", sum(vector1))
cat("MEAN: ", mean(vector1))
cat("PRODUCT: ", prod(vector1))

# SORTING
print("Enter a vector: ")
vector1 = scan()
bool = as.integer(readline(prompt = "Enter 1 to sort in ascending 0 for descending: "))

if(bool == 0){
  cat("SORTED VECTOR: ", sort(vector1, decreasing = TRUE))
}else{
  cat("SORTED VECTOR: ", sort(vector1))
}

#ODD OR EVEN
num <- as.numeric(readline(prompt = "Enter a number: "))
if(num %% 2 == 0)
{
  cat(num, "is even.")
} else{
  cat(num, "is odd.")
}

