#Interview Question

You are given a Trie (a tree in which each Node contains a character
  of a word inserted into it) populated with n words. The class definitions
  of the Node and Trie classes are as follows:

Node:  
``` python  
class Node:
	def __init__(self, cargo, end=False):
		self.cargo = cargo
		self.next = {}
		self.end = end
```

Trie:  
``` python  
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
```

Create an Auto Complete system that gives word recommendations
given an inputted string. For example, if the Trie contained the words
"dog", "dad" and "dogma" and the user entered "d" the output should
yield "dog", "dogma", "dad" (order doesn't matter and you can
output the result in the form of a list or on new lines)
