def sortedString(listString):
	listString.sort(key = len)
	print listString

listS = raw_input()
sortedString([string for string in listS.split(' ')])