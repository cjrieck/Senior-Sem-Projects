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
		current = self.root

		for letter in word:
			if current.next.has_key(letter):
				current = current.next[letter]
			else:
				return False
		return current

	def recommend(self, word, node, words=[]):
		
		if node.next.keys() == []:
			words.append(word)

		for letter in node.next.keys():
			if node.next.has_key(letter):
				self.recommend(word + letter, node.next[letter], words)

		return words

	def recommendations(self, word):
		startingNode = self.traverse(word)
		if not startingNode:
			return "no words found"

		words = self.recommend(word, startingNode)
		return words

def main():
	myTrie = Trie()
	myTrie.insert("dog")
	myTrie.insert("dad")
	myTrie.insert("cat")
	for word in myTrie.recommendations("d"):
		print word

if __name__ == '__main__':
	main()