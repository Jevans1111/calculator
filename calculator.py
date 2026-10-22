# SCCM4910 lab project - a four-operation calculator
def add(a, b):
	return a + b

def subtract (a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b

def main():
	while True:
		a = float(input("First number: "))
		op = input("Operator ( + - * /): ")
		b = float(input("Second number: "))
		if op == "+":
			print("result: ", add(a, b))
		elif op == "-":
			print("result: ", subtract(a, b))
		elif op == "*":
			print("result: ", multiply(a, b))
		elif op == "/":
			print("result: ", divide(a, b))
		else:
			print("Unknown operator:", op)


if __name__ == "__main__":
	main()
