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

	def recommend(self, substring, node):
		current = self.root

		if self.search(substring):
			for letter in substring:
				


def main():
	myTrie = Trie()
	myTrie.insert("dog")
	print myTrie.search("dog")

if __name__ == '__main__':
	main()