from parter_tools import printout
from parter_tools import sql
from parter_tools import extractor
from parter_tools import sql_writer

def log():
    
    print("This is the part input form for a fresh pack of new components/parts. Enter everything here. The abbreviations are below this line.")
    print("")
    printout.shorties()
    print("")
    type_short = input("Enter the part type shortcut: ")
    rows = sql.sxecute("SELECT ValueE FROM Types WHERE short = ?", (type_short,))
    while not rows:
        type_short = input("Unknown type, try again: ")
        rows = sql.sxecute("SELECT ValueE FROM Types WHERE short = ?", (type_short,))
    value_e = rows[0][0]
    print("Input the main value describing the components (e.g.: Resistor -> Ohm, Condesator -> Farad)")
    value = input(f"The unit for the part type chosen is [{value_e}]: ")
    qty = input("Enter the quanity of components currently in stock: ")
    des = input("Enter any additional desegnatior like 'X7R': ")
    maxV = input("Enter the maximal voltage viable for the component: ")
    maxA = input("Enter the maximal amperage viable for the component: ")
    mfr = input("Enter the component manufacturers name: ")
    foot = input("Enter the footprint standart of the component: ")
    storage = input("Enter the storage place of the component: ")

    type_id = sql.sxecute("SELECT ID FROM Types WHERE short = ?", (type_short,))[0][0]
    ivalue = extractor.num_tr(value)
    iqty = int(qty)
    ides = des
    imaxV = extractor.num_tr(maxV)
    imaxA = extractor.num_tr(maxA)
    imfr = mfr
    ifoot = foot
    istorage = storage

    sql_writer.addComponent(type_id, ivalue, ides, iqty, imaxV, imaxA, imfr, ifoot, istorage)

