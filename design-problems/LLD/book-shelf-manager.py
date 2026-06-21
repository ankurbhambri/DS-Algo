
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

# The shelf is an ordered list of books. The interesting part of the design is
# the bookmark: it points at a specific book, so when books are inserted,
# removed or moved the bookmark index must shift to keep pointing at the SAME
# book. If the bookmarked book itself is removed, the bookmark is cleared (-1).
#
# Internally we track the bookmark by the position of the book it refers to and
# patch that position inside every mutating operation.

class BookShelfManager:
    def __init__(self):
        self.books = []
        self.bookmark = -1  # -1 means no bookmark set

    # Insert `new_books` so that the first one lands at `to_index`.
    # TC: O(n + k)   SC: O(k)   (k = len(new_books))
    def addBooks(self, to_index, new_books):
        to_index = max(0, min(to_index, len(self.books)))
        self.books[to_index:to_index] = new_books

        # shift bookmark if the insertion happened at or before it
        if self.bookmark >= to_index:
            self.bookmark += len(new_books)

    # Remove the half-open range [from_index, to_index).
    # TC: O(n)   SC: O(1)
    def removeBooks(self, from_index, to_index):

        from_index = max(0, from_index)
        to_index = min(to_index, len(self.books))

        if from_index >= to_index:
            return

        removed = to_index - from_index
        del self.books[from_index:to_index]

        if self.bookmark >= to_index:
            self.bookmark -= removed          # bookmark was after the cut

        elif self.bookmark >= from_index:
            self.bookmark = -1                # bookmarked book was removed
    

    # yha humme books ko mover karna h, from_index + size books ko to_index par move karna h, 
    # aur bookmark ko bhi update karna h taki wo same book ko point karta rahe

    # TC: O(n)   SC: O(size)
    def moveBooks(self, from_index, to_index, size):

        n = len(self.books)
        if size <= 0 or from_index < 0 or from_index + size > n:
            return

        has_bookmark = 0 <= self.bookmark < n   # was: bookmarked_book = ...

        chunk = self.books[from_index:from_index + size]
        del self.books[from_index:from_index + size]

        to_index = max(0, min(to_index, len(self.books)))
        self.books[to_index:to_index] = chunk

        if has_bookmark:
            if from_index <= self.bookmark < from_index + size:
                # the bookmarked book was part of the moved chunk
                self.bookmark = to_index + (self.bookmark - from_index)
            else:
                b = self.bookmark
                if b >= from_index + size:   # chunk removed from before it
                    b -= size
                if b >= to_index:            # chunk reinserted at/before it
                    b += size
                self.bookmark = b

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