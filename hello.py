def fibonacci_series(n):
	fib_sequence = [ ]
	a, b = 0,1
	step_count = 0
	
	for _ in range(n):
		fib_sequence.append(a)
		a, b = b, a+b
		step_count +=1
		
	return fib_sequence, step_count
num_terms = int(input("Enter no of terms in the fibonacci series: "))

fib_series, steps = fibonacci_series(num_terms)

print(f"fibonacci series up to {num_terms} terms: {fib_series}")
print(f"Total steps taken: {steps}")
