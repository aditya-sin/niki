import string

def cipher(m,n):
	letters = string.ascii_uppercase

	mLowerLim = m/26
	mUpperLim = m%26
	nLowerLim = n/26
	nUpperLim = n%26

	for i in range(mLowerLim-1, nLowerLim):
		if mLowerLim == nLowerLim:
			if mLowerLim == 0:
				for j in range(mUpperLim-1, nUpperLim):
					print letters[j]
				break
			for j in range(mUpperLim-1, nUpperLim):
				print letters[i]+letters[j]
			break
		for j in range(26):
			if i == mLowerLim-1:
				if mLowerLim== 0 and j >= mUpperLim-1:
					print letters[j]
				elif j >= mUpperLim-1:
					print letters[i]+letters[j]
			elif i == nLowerLim-1:
				if j <= nUpperLim-1:
					print letters[i]+letters[j]
			else:
				print letters[i]+letters[j]

nums = raw_input().split(' ')
cipher(int(nums[0]),int(nums[1]))