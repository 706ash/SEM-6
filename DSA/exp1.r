repeat {
  cat("\n\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm (base 10)\n7. Power\n8. Exit\n\nEnter your choice: ")
  choice = as.integer(readline())
 
  if (choice >= 1 && choice <= 4) {
	n1 = as.integer(readline(prompt = "Enter a number n1: "))
	n2 = as.integer(readline(prompt = "Enter a number n2: "))
  } else if (choice == 5 || choice == 6) {
	n1 = as.integer(readline(prompt = "Enter a number: "))
  } else if (choice == 7) {
	n1 = as.integer(readline(prompt = "Enter a number: "))
	n2 = as.integer(readline(prompt = "Enter its power: "))
  } else if (choice == 8) {
	break
  } else {
	cat("\nInvalid choice")
	next
  }
 
  result = switch(
	choice,
	n1 + n2,
	n1 - n2,
	n1 * n2,
	ifelse(n2 == 0, "Exception: Division By zero", n1 / n2),
	exp(n1),
	log(n1, base = 10),
	n1 ^ n2
  )
 
  cat("\nResult = ", result)
}

