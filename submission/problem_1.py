def checkAnagram(string1, string2):
	# for testcases in range(int(input())):
		# string1 = input()
		# string2 = input()
		string1 = string1.replace(' ', '')
		string2 = string2.replace(' ', '')
		returnChar = 'N'
		length1 = len(string1)
		length2 = len(string2)
		if length1 == length2:
			dictionary1 = {}	
			dictionary2 = {}
			for n in string1:
			    dictionary1[n] = dictionary1.get(n, 0) + 1
			for n in string2:
			    dictionary2[n] = dictionary2.get(n, 0) + 1

		if dictionary1 == dictionary2:
			returnChar = 'Y'
		print(dictionary1)
		print(dictionary2)
		print(returnChar)
checkAnagram('xaa','aax')
