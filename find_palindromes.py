import sys

def find_palindrome(orig_number):
	orig_number = int(orig_number)
	for num in range(orig_number):
		#print num 
		#print orig_number
		str_num = str(num)
		reversed_num = str_num[::-1]
		#print reversed_num
		for i in range (0, (len(str_num)+1) / 2):
			if str_num[i] != reversed_num[i]:
				print 'str_num[i] = ' +str_num[i]
				print 'reversed_num[i] = ' +reversed_num[i]
				print 'This number is not a palindrome: ' + str_num
			else:
				print 'str_num[i] = ' +str_num[i]
				print 'reversed_num[i] = ' +reversed_num[i]
				print 'This number is a palindrome: ' + str_num
	return find_palindrome

def main():
	#print 'main() function'
	orig_number = raw_input('Please enter a number: ')
	find_palindrome(orig_number)

if __name__ == '__main__':
  main()
