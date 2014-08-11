#!/usr/bin/python 

def read_file():
	dictionary = {}
	i = 0
	file_object = open("analysis_file/bible.txt", "r")
	for line in file_object:
		dictionary[i] = line
		i +=1
	display_dictionary(dictionary)

def display_dictionary(dictionary):
	count = 0
	for name in dictionary:
		words = dictionary[name].split()
		for word in words: 
			if ('Lord' in word) or ('lord' in word):
 				count +=1

	print(count)	

		
def main():
	read_file()

if __name__ == "__main__":
    main()
