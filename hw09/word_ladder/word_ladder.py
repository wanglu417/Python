from stack import Stack
from queue import Queue
import sys
sys.setrecursionlimit(1000000)


class WordLadder:
    """A class providing functionality to create word ladders"""
    # Implement functionality necessary to generate a
    # stack representing the word ladder based on the parameters
    # passed to the constructor.

    def __init__(self, w1, w2, wordlist):
        self.wordlist = wordlist
        self.beginWord = w1
        self.endWord = w2
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.queue = Queue()
        self.stack = Stack()
        self.stack.push(self.beginWord)
        self.queue.enqueue(self.stack)
        self.wordlist.remove(self.beginWord)

    def make_ladder(self):
        """Generate a list representing the word ladder"""
        if self.queue.isEmpty():
            return None
        else:
            self.tempStack = self.queue.dequeue()
            self.tempWord = self.tempStack.peek()
            for i in range(len(self.tempWord)):
                for j in self.alphabet:
                    self.tempAlphabetList = list(self.tempWord)
                    if j != self.tempAlphabetList[i]:
                        self.tempAlphabetList[i] = j
                        self.newWord = ''.join(self.tempAlphabetList)
                        if self.newWord in self.wordlist:
                            self.newStack = self.tempStack.copy()
                            self.newStack.push(self.newWord)
                            if self.newWord == self.endWord:
                                return self.newStack.items
                            else:
                                self.queue.enqueue(self.newStack)
                                self.wordlist.remove(self.newWord)
            return self.make_ladder()
