def CreateStringArray(pattern):

	n = len(pattern)
	pattern_ind_array = [None] * n
	pattern_ind_array[0] = 0
	i = 0
	j = i + 1
	while j < n:
		if pattern[j] == pattern[i]:
			pattern_ind_array[j] = i+1
			i += 1
			j += 1
		elif i == 0:
			pattern_ind_array[j] = 0
			j += 1
		else:
			i = pattern_ind_array[i - 1]

	return pattern_ind_array

def StringSearch(search_string, pattern, pattern_ind_array):

	i = j = 0
	while (i < len(search_string)) and (j < len(pattern_ind_array)):
		if search_string[i] == pattern[j]:
			if j == len(pattern_ind_array) - 1:
				return True
			i += 1
			j += 1
		elif (search_string[i] != pattern_ind_array[j]) and (j == 0):
			i += 1
		elif (search_string[i] != pattern_ind_array[j]) and (j != 0):
			j = pattern_ind_array[j - 1]

	return False

def KMP(search_string, pattern):

	pattern_ind_array = CreateStringArray(pattern)
	return StringSearch(search_string, pattern, pattern_ind_array)



if __name__ == "__main__":

	pattern = "abcaby"
	s = "abxabcabcaby"
	print(KMP(s, pattern))
