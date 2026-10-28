import sqlite3


def sxecute(script, params=()):
    con = sqlite3.connect("C:/Users/schar/Desktop_data/Documentation/Componets_Stock.db")
    try:
        cur = con.cursor()    
        cur.execute(script, params)
        rows = cur.fetchall()
        con.commit()
        return rows
    finally:
        con.close()



def resetTable(table):
    sxecute(f"DELETE FROM {table}")
    sxecute("DELETE FROM sqlite_sequence WHERE name = ?", (table,))