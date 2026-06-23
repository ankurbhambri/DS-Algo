
'''
design BookShelfManager class
that has following methods

addBooks(toIndex, books)
removeBooks(fromIndex, toIndex)
moveBooks(fromIndex, toIndex, size)
getBooks()
setBookmarkIndex(index)
getBookmarkIndex()
'''

class BookShelfManager:
    def __init__(self):
        self.books = []
        self.bookmark = -1  # -1 means no bookmark set


    # Insert `new_books` so that the first one lands at `to_index`.
    # TC: O(n + k)   SC: O(k)   (k = len(new_books))
    def addBooks(self, to_index, new_books):

        # add at end if to_index is gt to books array size
        if to_index > len(self.books):
            self.books += new_books

        if 0 <= to_index <= len(self.books):
            self.books[to_index:to_index] = new_books

        # shift bookmark if the insertion happened at or before it
        if self.bookmark >= to_index:
            self.bookmark += len(new_books)


    # Remove the half-open range [from_index, to_index).
    # TC: O(n)   SC: O(1)
    def removeBooks(self, from_index, to_index):

        # agar from_index 0 se chota nikal
        from_index = max(0, from_index)

        # agar to_index books array se greater nikala
        to_index = min(to_index, len(self.books))

        # out of bound
        if from_index > len(self.books) or from_index >= to_index:
            return

        # delete kardo        
        self.books = self.books[:from_index] + self.books[to_index:]

        # ab humko bookmark bhi update karna h toh
        gap = to_index - from_index

        # agar bookmark range ke beech mein hota
        if from_index <= self.bookmark <= to_index:
            self.bookmark = from_index

        # agar to_index se bada hota toh range minus kardo
        elif self.bookmark > to_index:
            self.bookmark -= gap


    # yha humme books ko mover karna h, from_index + size books ko to_index par move karna h, 
    # aur bookmark ko bhi update karna h taki wo same book ko point karta rahe

    # TC: O(n), SC: O(size)
    def moveBooks(self, from_index, to_index, size):

        n = len(self.books)

        if size <= 0 or from_index < 0 or from_index + size > n:
            return

        # pehle chunk nikalo aur usko old position se delete kardo
        chunk = self.books[from_index:from_index + size]
        del self.books[from_index:from_index + size]

        # remove karne ke baad usse new position pe daal do
        to_index = max(0, min(to_index, len(self.books)))
        self.books[to_index:to_index] = chunk

        # the bookmarked book was part of the moved chunk
        if from_index <= self.bookmark < from_index + size:
            self.bookmark = to_index + (self.bookmark - from_index)

        elif self.bookmark >= from_index + size:
            self.bookmark = from_index

        elif self.bookmark >= to_index:
            self.bookmark += size


    def getBooks(self):
        return self.books

    def setBookmarkIndex(self, index):
        if 0 <= index < len(self.books):
            self.bookmark = index
        else:
            self.bookmark = -1

    def getBookmarkIndex(self):
        return self.bookmark


shelf = BookShelfManager()
shelf.addBooks(0, ["A", "B", "C"])      # [A, B, C]
shelf.addBooks(1, ["X", "Y"])           # [A, X, Y, B, C]
shelf.setBookmarkIndex(3)               # bookmark -> "B"
print(shelf.getBooks())                 # ['A', 'X', 'Y', 'B', 'C']
print(shelf.getBookmarkIndex())         # 3

shelf.removeBooks(1, 3)                 # remove X, Y -> [A, B, C]
print(shelf.getBooks())                 # ['A', 'B', 'C']
print(shelf.getBookmarkIndex())         # 1  (still "B")

shelf.moveBooks(1, 2, 1)               # move "B" to end -> [A, C, B]
print(shelf.getBooks())                 # ['A', 'C', 'B']
print(shelf.getBookmarkIndex())         # 2  (still "B")