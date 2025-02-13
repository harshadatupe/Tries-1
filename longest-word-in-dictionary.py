def longestWord(self, words: List[str]) -> str:
    # tc O(n * wl), sc O(n * wl).
    root = TrieNode()
    root.end = True

    # build the trie
    for word in words:
        curr = root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True
    
    # traverse the trie using dfs to find longest word
    longest = [""]

    def get_longest_word_using_dfs(node, path):
        if not node.end:
            return
        
        if len(path) > len(longest[0]) or (len(path) == len(longest[0]) and "".join(path) < longest[0]):
            longest[0] = "".join(path)
        
        for key in node.children:
            path.append(key)
            get_longest_word_using_dfs(node.children[key], path)
            path.pop()
    get_longest_word_using_dfs(root, [])

    return longest[0]