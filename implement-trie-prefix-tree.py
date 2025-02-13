class Trie:
    # tc O(wordlen), sc O(26^wordlen).
    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        curr = self.trie
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        
        curr["end"] = True

    def search(self, word: str) -> bool:
        curr = self.trie
        for char in word:
            if char not in curr:
                return False
            curr = curr[char]
        
        return "end" in curr
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]
        return True