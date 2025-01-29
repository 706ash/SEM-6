add = function(n1, n2)
{
  return (n1 + n2)
}

subtract = function(n1, n2)
{
  return (n1 - n2)
}

multiply = function(n1, n2)
{
  return (n1 * n2)
}

divide = function(n1, n2)
{
  ifelse(n2==0,return ("Exception: Division By zero"),return (n1 / n2))
}

exponentiation = function(n1)
{
  return (exp(n1))
}

logarithm = function(n1)
{
  if(n1 <= 0)
  {
    return("Error: Log of negative no")
  }
  return (base::log(n1, base = 10))
}

power = function(n1, n2)
{
  return (n1 ^ n2)
}

repeat{
  cat("\n\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Divison\n5. Exponentiation\n6. Logarithm(base 10)\n7. Power\n8. Exit\n\nEnter your choice: ")
  choice = as.integer(readline())

  if(!(choice %in% 1:8))
  {
    cat("\n\nInvalid choice!")
    next
  }
  else if(choice == 8) break

  n1 = as.integer(readline(prompt = "Enter a number n1: "))
  n2 = NULL
  
  if(choice %in% c(1, 2, 3, 4, 7)){
    n2 = as.integer(readline(prompt = "Enter a second number n2: "))
  }

  
  
  result = switch(
    choice,
    add(n1, n2),
    subtract(n1, n2),
    multiply(n1, n2),
    divide(n1, n2),
    exponentiation(n1),
    logarithm(n1),
    power(n1, n2)
  )
  cat("\nResult = ",result)
  
}

