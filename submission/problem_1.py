#9791563725
def checkAnagram():
	for testcases in range(int(input())):
		string1 = input()
		string2 = input()
		string1 = string1.replace(' ', '')
		string2 = string2.replace(' ', '')
		returnChar = 'N'
		length1 = len(string1)
		length2 = len(string2)
		if length1 == length2:
			dictionary1 = {}	
			dictionary2 = {}
			key1 = dictionary1.keys()
			key2 = dictionary2.keys()
			for n in string1:
			    if n in key1:
			        dictionary1[n] += 1
			    else:
			        dictionary1[n] = 1
			for n in string2:
			    if n in key2:
			        dictionary2[n] += 1
			    else:
			        dictionary2[n] = 1
			if dictionary1 == dictionary2:
				returnChar = 'Y'
		print(dictionary1)
		print(dictionary2)
		print(returnChar)
checkAnagram()