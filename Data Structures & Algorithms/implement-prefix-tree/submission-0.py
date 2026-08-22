class Node:
    def __init__(self):
        self.endOfWord=False 
        self.arr=[None]*26

class PrefixTree:
    def __init__(self):
        self.root=Node()

    def insert(self, word: str) -> None:
        curr=self.root
        for c in word:
            if not curr.arr[ord(c)-ord('a')]:
                curr.arr[ord(c)-ord('a')]=Node()
            curr=curr.arr[ord(c)-ord('a')]
        curr.endOfWord=True

    def search(self, word: str) -> bool:
        curr=self.root
        for c in word:
            if not curr.arr[ord(c)-ord('a')]:
                return False
            curr=curr.arr[ord(c)-ord('a')]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for c in prefix:
            if not curr.arr[ord(c)-ord('a')]:
                return False
            curr=curr.arr[ord(c)-ord('a')]
        return True