import psycopg
with psycopg.connect("dbname='postgres' user='postgres' host='localhost' password='mercury1960'") as conn:
    with conn.cursor() as cur:
#          # cur.execute("INSERT INTO study_group VALUES (%s, %s)", [1, "1510"])
#         cur.execute("SELECT * FROM study_group")
#         lst = cur.fetchone()
# print(lst)
# print(type(lst[0]))
# print(type(lst[1]))
        j = 800
        k = 201
        while True:
            cur.execute("INSERT INTO answer VALUES (%s, %s, %s, %s);", [j, f"Theme3_Question{k-200}_FalseAnswer_1", False, k-1])
            cur.execute("INSERT INTO answer VALUES (%s, %s, %s, %s);", [j+1, f"Theme3_Question{k-200}_FalseAnswer_2", False, k-1])
            cur.execute("INSERT INTO answer VALUES (%s, %s, %s, %s);", [j+2, f"Theme3_Question{k-200}_FalseAnswer_3", False,k-1])
            cur.execute("INSERT INTO answer VALUES (%s, %s, %s, %s);", [j+3, f"Theme3_Question{k-200}_TrueAnswer", True, k-1])
            j += 4
            k += 1
            if j > 1199:
                break
            print(j)
