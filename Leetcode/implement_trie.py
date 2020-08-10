"""
Implement Trie (Prefix Tree)



Share
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.start={}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.start
        for ch in word:
            if ch not in  cur:
                cur[ch]={}
            cur=cur[ch]
        
        cur['*']=True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.start
        for ch in word:
            if ch not in cur:
                return False
            cur=cur[ch]

        if '*' in cur:
            return True
        else:
            return False

        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.start
        for ch in prefix:
            if ch not in cur:
                return False
            cur=cur[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("hello")
obj.insert("hey")
obj.insert("heyl")
obj.insert("apple")
obj.insert("app")
print(obj.start.keys())
print(obj.search("heyl"))
print(obj.startsWith("hi"))