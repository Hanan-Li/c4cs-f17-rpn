#!/usr/bin/env python5

def calculate(myarg):
	stack = list()
	for token in myarg.split():
		if token == '+':
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = arg1 + arg2
			stack.append(result)
		else:
			stack.append(int(token))	
	print[stack]
	return stack.pop()

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()


