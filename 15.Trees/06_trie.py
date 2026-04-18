"""
Trees in DSA — 6. Trie (Prefix Tree)
Stores strings character-by-character along branches.
Shared prefixes share the same path.
Search and insert are O(L) where L = word length.

Use cases: autocomplete, spell checker, word search,
           IP routing (longest prefix match).
"""


class TrieNode:
    def __init__(self):
        self.children = {}   # char → TrieNode
        self.is_end = False  # marks end of a complete word
        self.count = 0       # how many words pass through this node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the trie — O(L)."""
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1
        node.is_end = True

    def search(self, word):
        """Returns True if exact word exists — O(L)."""
        node = self._find(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        """Returns True if any word starts with prefix — O(L)."""
        return self._find(prefix) is not None

    def count_prefix(self, prefix):
        """Count how many words start with this prefix."""
        node = self._find(prefix)
        return node.count if node else 0

    def _find(self, prefix):
        """Navigate trie to end of prefix, return node or None."""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def delete(self, word):
        """Delete a word from the trie."""
        self._delete(self.root, word, 0)

    def _delete(self, node, word, depth):
        if depth == len(word):
            if node.is_end:
                node.is_end = False
            return len(node.children) == 0

        ch = word[depth]
        if ch not in node.children:
            return False

        child = node.children[ch]
        child.count -= 1
        should_delete = self._delete(child, word, depth + 1)

        if should_delete:
            del node.children[ch]
            return not node.is_end and len(node.children) == 0

        return False

    def autocomplete(self, prefix, limit=10):
        """Return all words starting with prefix (up to limit)."""
        node = self._find(prefix)
        if not node:
            return []

        results = []

        def dfs(node, path):
            if len(results) >= limit:
                return
            if node.is_end:
                results.append(prefix + "".join(path))
            for ch in sorted(node.children):
                path.append(ch)
                dfs(node.children[ch], path)
                path.pop()

        dfs(node, [])
        return results

    def all_words(self):
        """Return all words in the trie."""
        return self.autocomplete("")


# --- Demo ---
if __name__ == "__main__":
    t = Trie()
    words = ["cat", "car", "card", "care", "careful",
             "dog", "dot", "does"]

    for w in words:
        t.insert(w)

    print(f"All words:          {t.all_words()}")
    print(f"search('car'):      {t.search('car')}")
    print(f"search('ca'):       {t.search('ca')}")
    print(f"starts_with('ca'):  {t.starts_with('ca')}")
    print(f"count_prefix('ca'): {t.count_prefix('ca')}")
    print(f"autocomplete('ca'): {t.autocomplete('ca')}")
    print(f"autocomplete('do'): {t.autocomplete('do')}")

    t.delete("car")
    print(f"\nAfter deleting 'car':")
    print(f"search('car'):      {t.search('car')}")
    print(f"search('card'):     {t.search('card')}")
    print(f"autocomplete('ca'): {t.autocomplete('ca')}")
