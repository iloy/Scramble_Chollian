
import sys
import sqlite3

from collections import Counter

def solve(chars):

#    print chars

    ch_counter = Counter(chars)

    where_str = ' AND '.join('count_' + ch + ' <= ' + str(ch_counter[ch]) if ch in ch_counter else 'count_' + ch + ' = 0' for ch in 'abcdefghijklmnopqrstuvwxyz')
#    print where_str

    conn = sqlite3.connect('../dic/dictionary.db')
    cur = conn.cursor()

    score = 0
    for row in cur.execute("SELECT word, length FROM british_english_insane WHERE length > 1 AND " + where_str + " ORDER BY length DESC, word ASC"):
        print row[0], row[1]
        score = score + int(row[1])**2

    print "total score: " + str(score)

    cur.close()
    conn.close()

if __name__ == '__main__':
    chars = []
    while(True):
        data = sys.stdin.readline().split()
        if len(data) == 0:
            break
        chars.extend(data)

    solve(chars)

