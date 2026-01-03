'''

Given a playlist of songs. Implement a shuffle function, such that there is no/minimal adjacent artists.

using Song = pair<string, string>; // (artist, song)

void shuffle(vector<Song>& playlist)

Input:

[
  { "artist": "A", "song": "apple" },
  { "artist": "A", "song": "banana" },
  { "artist": "B", "song": "orange" },
  { "artist": "B", "song": "guava" },
  { "artist": "C", "song": "mango" }
]

Output: ABABC

'''


import heapq
from collections import defaultdict, deque

# Song = (artist, song)
def shuffle(playlist):
    # 1. Group songs by artist
    artist_songs = defaultdict(deque)
    for artist, song in playlist:
        artist_songs[artist].append(song)

    # 2. Max heap based on remaining song count
    # Python has min heap, so we use negative counts
    max_heap = []
    for artist, songs in artist_songs.items():
        heapq.heappush(max_heap, (-len(songs), artist))

    result = []
    prev_count, prev_artist = 0, None

    # 3. Build shuffled playlist
    while max_heap:
        count, artist = heapq.heappop(max_heap)

        # Pick one song from this artist
        song = artist_songs[artist].popleft()
        result.append((artist, song))

        # Reduce count (since count is negative)
        count += 1

        # Push previous artist back if it still has songs
        if prev_artist and prev_count < 0:
            heapq.heappush(max_heap, (prev_count, prev_artist))

        prev_count, prev_artist = count, artist

    return result

print(shuffle([
  ("A", "apple"),
  ("A", "banana"),
  ("A", "grapes"),
  ("B", "orange"),
  ("B", "guava"),
  ("C", "mango")
]))