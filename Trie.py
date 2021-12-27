'''Trie Data Stucture'''

class Trie:
    head = {}

    def add(self, word):

        curr = self.head

        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]

        curr['*'] = True

    def search(self, word):

        curr = self.head

        for ch in word:
            if ch not in curr:
                return False
            curr = curr[ch]

        if '*' in curr:
            return True
        else:
            return False

    def func(self):
        return self.head



obj = Trie()
obj.add('Hi')
obj.add('Hello')
obj.add('He')
obj.add('Hel')
obj.add('V')
print(obj.func())


print(obj.search('He'))
print(obj.search('Hell'))
