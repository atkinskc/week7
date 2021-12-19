Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def sed(string, string, "C:\Python27\words.txt", "C:\Python27\output.txt"):
	fin = open("C:\Python27\words.txt", 'r')
	fout = open("C:\Python27\output.txt", 'w')
	
SyntaxError: invalid syntax
>>> def sed(string, string, "C:\Python27\words.txt", "C:\Python27\output.txt"):
	fin = open("C:\Python27\words.txt", 'r')
	fout = open("C:\Python27\output.txt", 'w')
	
SyntaxError: invalid syntax
>>> def sed(string, string, C:\Python27\words.txt, C:\Python27\output.txt):
	fin = open("C:\Python27\words.txt", 'r')
	fout = open("C:\Python27\output.txt", 'w')
	
SyntaxError: unexpected character after line continuation character
>>> def sed(string, string, C:\Python27\words.txt, C:\Python27\output.txt)
	fin = open("C:\Python27\words.txt", 'r')
	fout = open("C:\Python27\output.txt", 'w')
	
SyntaxError: unexpected character after line continuation character
>>> def sed(string, string, fin, fout):
	fin = open("C:\Python27\words.txt", 'r')
	fout = open("C:\Python27\output.txt", 'w')
	
SyntaxError: duplicate argument 'string' in function definition
>>> def sed(string, string, C:\Python27\words.txt, C:\Python27\output.txt):
	fin = open("C:\Python27\words.txt", 'r')
	fout = open("C:\Python27\output.txt", 'w')
	
SyntaxError: unexpected character after line continuation character
>>> def sed(string, string, filename, filename):
	fin = open("C:\Python27\words.txt", 'r')
	fout = open("C:\Python27\output.txt", 'w')
	
SyntaxError: duplicate argument 'string' in function definition
>>> def sed(string, string, C:\Python27\words.txt, C:\Python27\output.txt):
	fin = open("C:\Python27\words.txt", 'r')
	fout = open("C:\Python27\output.txt", 'w')
	
SyntaxError: unexpected character after line continuation character
>>> def sed(abase, goldfish, fin, fout):
	fin = open("C:\Python27\words.txt", 'r')
	fout = open("C:\Python27\output.txt", 'w')
	for string in fin:
		string = string.replace('abase','goldfish')

		
>>> def sed(abase, goldfish, fin, fout):
	fin = open("C:\Python27\words.txt", 'r')
	fout = open("C:\Python27\output.txt", 'w')
	for string in fin:
		string = string.replace('abase','goldfish')
		fin.close()
		fout.close()
	return ':)'

>>> 
