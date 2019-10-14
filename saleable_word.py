# A word could be made "saleable" if it doesn't contain any two adjacent letters same.

class WordSale:
	def saleable_word(words):
		output = []
		for word in words:
			count, last_index = 0, -1
			len_word = len(word)
			for index in range(len_word):
				if word[index] == word[index - 1] and (index - 1) in range(len_word) and (index - 1) != last_index:
					last_index = index
					count += 1
			output.append(count)
		return output

if __name__ == '__main__':
	input_words = ["ab", "aab", "abb", "abab", "abaaaba"]
	saleable_word(input_words)
