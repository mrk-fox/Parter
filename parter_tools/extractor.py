# This file gets called with the flags for ther parter command and then outputs the whole table with all the parts. 
import re
from parter_tools import sql

rows = [('ID', 'Type', 'Value', 'Value Unit', 'Des', 'maxV', 'maxA', 'Footprint', 'MFR', 'Qty', 'Storage')]

def filter(id, p, v, d, mV, mA, mfr, foot, storage):
    query = "SELECT Part.ID, Type, Value, ValueE, Des, maxV, maxA, foot, MFR, qty, storage FROM Part JOIN Types ON Types.ID = Part.TypeID"
    addition = []
    if id != None:
        addition.append(f"Part.ID =  {id}")
    if p != None:
        addition.append(f"short =  '{p}'")
    if v != None:
        addition.append(f"Value = '{v}'")
    if d != None:
        addition.append(f"Des = '{d}'")
    if mV != None:
        addition.append(f"maxV >= {mV}")
    if mA != None:
        addition.append(f"maxA >= {mA}")
    if mfr != None:
        addition.append(f"MFR = '{mfr}'")

    if addition:
        query += " WHERE " + " AND ".join(addition)
    return query

def change(id, p, v, d, mV, mA, mfr, foot, storage):
    query = "UPDATE Part"
    addition = []
    if p != None:
        addition.append(f"TypeID = '{type_tr(p)}'")
    if v != None:
        addition.append(f"Value = '{v}'")
    if d != None:
        addition.append(f"Des = '{d}'")
    if mV != None:
        addition.append(f"maxV >= {mV}")
    if mA != None:
        addition.append(f"maxA >= {mA}")
    if mfr != None:
        addition.append(f"MFR = '{mfr}'")

    if addition:
        query += " SET " + ", ".join(addition)
        query += f" WHERE Part.ID = {id}"
    
    return query
        


EXPONENTS = {
    "f": -15, 
    "p": -12, 
    "n": -9, 
    "u": -6, 
    "µ": -6, 
    "m": -3,
    "k": 3, 
    "M": 6, 
    "G": 9, 
    "T": 12,
}

_SUFFIXES = "".join(EXPONENTS)
_WITH_SUFFIX = re.compile(rf"(\d+(?:[.,]\d+)?)\s*([{_SUFFIXES}])")
_ELECTRONIC = re.compile(rf"(\d+)([{_SUFFIXES}])(\d+)")   # 4k7 -> 4.7k
_PLAIN = re.compile(r"\d+(?:[.,]\d+)?")

def _clean(x): #deciding the return in float vs integer
    return int(x) if float(x).is_integer() else float(x)

def num_tr(inp):
    inp = str(inp).strip()
    if m := _ELECTRONIC.fullmatch(inp):
        whole, suffix, frac = m.groups()
        return _clean(float(f"{whole}.{frac}e{EXPONENTS[suffix]}"))

    if m := _WITH_SUFFIX.fullmatch(inp):
        number, suffix = m.groups()
        number = number.replace(",", ".")
        return _clean(float(f"{number}e{EXPONENTS[suffix]}"))

    if _PLAIN.fullmatch(inp):
        return _clean(float(inp.replace(",", ".")))

    return inp 


def type_tr(type):
    query = f"SELECT ID FROM Types WHERE short = '{type}'"
    out = sql.sxecute(query)
    return(out[0][0])


def to_float(s): # makes a string int a float
    s = s.strip().replace(",", ".")   # 2,4 is ok
    return float(s) if s else None
