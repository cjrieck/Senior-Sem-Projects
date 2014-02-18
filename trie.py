class Node:
	def __init__(self, cargo):
		self.cargo = cargo
		self.next = {}

class Trie:
	def __init__(self):
		self.root = Node('.')

	def insert(self, word):
		current = self.root

		for letter in word:
			if current.next.has_key(letter):
				current = current.next[letter]
			else:
				current.next[letter] = Node(letter)
				current = current.next[letter]

	def search(self, word):
		current = self.root

		for letter in word:
			if current.next.has_key(letter):
				current = current.next[letter]
			else:
				return False
		return True

	def traverse(self, word):
		

	def recommend(self, word, words, node):
		
		if node.next.keys() == []:
			words.append(word)

		for letter in node.next.keys():
			if current.next.has_key(letter):
				self.recommend(word + letter, words, node.next[letter])

		return words

def main():
	myTrie = Trie()
	myTrie.insert("dog")
	myTrie.insert("dad")
	myTrie.insert("cat")
	# print myTrie.search("dog")
	# print myTrie.search("da")
	print myTrie.recommend("d", [], myTrie.root)

if __name__ == '__main__':
	main()