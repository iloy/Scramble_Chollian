
import sys

import sqlite3

def make_dic():
    total_insert_cnt = 0
    with open('british-english-insane') as f:
        conn = sqlite3.connect('dictionary.db')
        cur = conn.cursor()

        cur.execute("DROP TABLE IF EXISTS british_english_insane")
        cur.execute("CREATE TABLE british_english_insane (word text PRIMARY KEY, length integer, count_a integer default 0, count_b integer default 0, count_c integer default 0, count_d integer default 0, count_e integer default 0, count_f integer default 0, count_g integer default 0, count_h integer default 0, count_i integer default 0, count_j integer default 0, count_k integer default 0, count_l integer default 0, count_m integer default 0, count_n integer default 0, count_o integer default 0, count_p integer default 0, count_q integer default 0, count_r integer default 0, count_s integer default 0, count_t integer default 0, count_u integer default 0, count_v integer default 0, count_w integer default 0, count_x integer default 0, count_y integer default 0, count_z integer default 0)")

        for line in f:
            success = True
            word = line.rstrip().lower()
            ch_count = {}
            for ch in word:
                if ch not in 'abcdefghijklmnopqrstuvwxyz':
                    success = False
                    break
                if ch in ch_count:
                    ch_count[ch] = ch_count[ch] + 1
                else:
                    ch_count[ch] = 1
            if success:
#                print total_insert_cnt+1, word, ch_count
                column_str = ''
                value_str = ''
                for ch in ch_count:
                    column_str = column_str + ", " + "count_" + ch
                    value_str = value_str + ", " + str(ch_count[ch])
                try:
                    cur.execute("INSERT INTO british_english_insane (word, length" + column_str + ") VALUES ('" + word + "', " + str(len(word)) + value_str + ")")
                    total_insert_cnt = total_insert_cnt + 1
                except Exception as e:
#                    print e
#                    print word
#                    sys.exit()
                    pass

#        cur.execute('''CREATE INDEX alphabet_count_idx ON british_english_insane (count_a, count_b, count_c, count_d, count_e, count_f, count_g, count_h, count_i, count_j, count_k, count_l, count_m, count_n, count_o, count_p, count_q, count_r, count_s, count_t, count_u, count_v, count_w, count_x, count_y, count_z)''')

        conn.commit()
        cur.close()
        conn.close()

if __name__ == '__main__':
    make_dic()

