def sub(a,b):
	result=a-b
	return result

def main():
	a=float(input("Enter your first number: "))
	b=float(input("Enter the second number: "))
	sub_result= sub(a,b)
	print("your answer is: ", sub_result)

main()