from parter_tools import sql as s

def addType(type, ValueE, short):
    s.sxecute("""
    INSERT INTO Types VALUES
    (Null, '""" + type + """', '""" + ValueE + """', '""" + short + """')
    """)

def addComponent(t_id, value, des, qty, maxV, maxA, mfr, foot, storage):
        s.sxecute(f"INSERT INTO Part VALUES (Null, '{t_id}', '{value}', '{des}', '{qty}', '{maxV}', '{maxA}', '{mfr}', '{foot}', '{storage}')") #change