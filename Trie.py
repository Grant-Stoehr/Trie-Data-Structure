from typing import Tuple

# This is a simple structure for a Node on the Trie
class TrieNode(object):
    def __init__(self, char: str):
        # This is the character at the existing node
        self.char = char
        # This is an array of all the children that this node is housing
        self.children = []
        # This is a boolean representation of whether or not the char being examined is at the end of a word
        self.word_finished = False
        # This is a counter that tracks the number of times this char has come up
        self.counter = 1

# This method will be used to insert a word into a Trie
def Insert(root, word: str):
    node = root
    for char in word:
        # This is a boolean variable that keeps track of whether or not the char already exists in the Trie
        alreadyExists = False
        # Searches for the character in the children array of the present node
        for child in node.children:
            "If the char already exists in the spot we would be" \
            "adding it, then add one to the counter of that node and" \
            "point the node to that char to continue to build off of"
            if child.char == char:
                child.counter += 1
                node = child
                alreadyExists = True
                break
        "Getting to this point implies that the new char does not" \
        "exist in the parent node, so we have to create a new" \
        "node for that child and add that to the self.child array"
        if not alreadyExists:
            newChildNode = TrieNode(char)
            node.children.append(newChildNode)
            node = newChildNode
    # Signals the end of the word
    node.word_finished = True


# This method will be used to search for a word in the Trie
def Search(root, prefix: str) -> Tuple[bool, str]:
    "Check to see if the prefix exists in any of the" \
    "words that we have already added and if so how" \
    "many words actually have that specific prefix"

    node = root
    "If the root has no children, return false, this implies" \
    "you are searching without any words inside of the Trie"
    if not root.children:
        return False, "String does not exist in the Trie"
    for char in prefix:
        charDoesNotExist = True
        # Seach to see if any of the children chars exist in that node
        for child in node.children:
            if child.char == char:
                charDoesNotExist = False
                node = child
                break
        if charDoesNotExist:
            return False, "String does not exist in the Trie"

    return True, "String exists in the Trie"


if __name__ == "__main__":
    root = TrieNode('*')
    Insert(root, "test")
    Insert(root, "testing")
    Insert(root, "hello")
    Insert(root, "world")

    print(Search(root, "boomer"))
    print(Search(root, "wo"))
    print(Search(root, "hello"))
