
#Write a script that reads your name from the console and prints it reversed in upper-case letters.

import sys

def reversed_name(input_name):
	upper_name = input_name.upper()
	print upper_name
	if len(upper_name) >= 1:      
		reversed_name = upper_name[::-1]
		print reversed_name
	return reversed_name

def main():
	print 'main() function'
	input_value = raw_input('Please enter your name: ')
	input_name = str(input_value)
	reversed_name(input_name)

if __name__ == '__main__':
  main()


