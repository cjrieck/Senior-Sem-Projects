class Node:
	def __init__(self, cargo, end=False):
		self.cargo = cargo
		self.next = {}
		self.end = end

class Trie:
	def __init__(self):
		self.root = Node('.')

	def insert(self, word):
		current = self.root

		for letter in range(len(word)):
			if current.next.has_key(word[letter]):
				current = current.next[word[letter]]
			else:
				if letter == len(word)-1:
					current.next[word[letter]] = Node(word[letter])
					current.next[word[letter]].end = True
				else:
					current.next[word[letter]] = Node(word[letter])
					current = current.next[word[letter]]

	

def main():
	myTrie = Trie()

	myTrie.insert("dog")
	myTrie.insert("dad")
	myTrie.insert("cat")
	myTrie.insert("dogma")

	substring = raw_input("Enter string: ")

	# enter code here

if __name__ == '__main__':
	main()