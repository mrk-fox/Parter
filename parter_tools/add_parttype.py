from parter_tools import printout
from parter_tools import sql
from parter_tools import extractor
from parter_tools import sql_writer

def log():
    print("New Parttype")
    print("-----------------------")
    name = input("New parttypes name (e.g.: Resistor): ")
    ValueE = input("New parttypes value unit (e.g.: Ohm): ")
    short = input("New parttypes abbreviation (e.g.: r): ")
    sql_writer.addType(name, ValueE, short)