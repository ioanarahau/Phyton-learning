#Write a script that checks if a given number is palindrome (eg. 2, 33, 13231). Do not use strings.

import sys

def check_palindrome(orig_number):
	print 'check_palindrome() function'
	reversed_number = orig_number[::-1]
	print orig_number
	print reversed_number
	for i in range (0, (len(orig_number) + 1) / 2):
		if reversed_number[i] != orig_number[i]:
			print 'This number is not a palindrome: ' + orig_number
			return False
		print 'This number is a palindrome: ' + orig_number
		return True

def main():
	print 'main() function'
	orig_number = raw_input('Please enter a number: ')
	check_palindrome(orig_number)

if __name__ == '__main__':
  main()
