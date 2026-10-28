# Copyright (C) 2026  Mark Scharonow

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# This is the main file that will get called

# What we need: query per part type
# parter -p r -v 

from parter_tools import sql
from parter_tools import add_part
from parter_tools import extractor
from parter_tools import printout
from parter_tools import add_parttype
from parter_tools import sql_reader

import argparse

parser = argparse.ArgumentParser(description="Parter CLI v0.1")
parser.add_argument('-a', '--add', action="store_true", help="Start the new part dialogue.")
parser.add_argument('-c', '--change', help="Change a parts attibute by it's ID. Add the ID of any part and the attribute flag with the new value. (e.g.: 1, 5, ... -x ...)")
parser.add_argument('-f', '--find', action="store_true", help="Find a part by its parameters added after this flag.")
parser.add_argument('-ap', '--add_parttype', action="store_true", help="Start the new parttype dialogue.")


parser.add_argument('-i', '--id', help="Argument flag for the part ID in the DB.")
parser.add_argument('-p', '--part', help="Argument flag for the part abbreviation as found in -pa.")
parser.add_argument('-v', '--value', help="Argument flag for the value field.")
parser.add_argument('-d', '--des', default=None, help="Argument flag for the additional designator.")
parser.add_argument('-mV', '--max_V', default=None, help="Argument flag for maximal voltage. You can write it with k, M, u etc. flags. (e.g.:15k, 5u, ...)")
parser.add_argument('-mA', '--max_A', default=None, help="Argument flag for maximal amperage. You can write it with k, M, u etc. flags. (e.g.:15k, 5u, ...)")
parser.add_argument('-mfr', '--manufacturer', default=None, help="Argument flag for the manufacturer.")
parser.add_argument('-foot', '--footprint', default=None, help="Argument flag for the footprint of the part.")
parser.add_argument('-s', '--storage', default=None, help="Argument flag for the storage place of the part.")



parser.add_argument('-pa', '--part_abbr', action='store_true', help="Show all the part abberviations")


printout.mainprint()


args = parser.parse_args()
if args.part_abbr:
    printout.shorties()
elif args.add:
    add_part.log()
elif args.add_parttype:
    add_parttype.log()
elif args.find:
    table = extractor.rows
    query = extractor.filter(args.id, p=args.part, v=args.value, d=args.des, mV=args.max_V, mA=args.max_A, mfr=args.manufacturer, foot=args.footprint, storage=args.storage)
    # print(query)
    table.extend(sql.sxecute(query))
    print(sql_reader.table(table))
elif args.change:
    query = extractor.change(args.change, p=args.part, v=args.value, d=args.des, mV=args.max_V, mA=args.max_A, mfr=args.manufacturer, foot=args.footprint, storage=args.storage)
    # print(query)
    sql.sxecute(query)
    table = extractor.rows
    query = extractor.filter(args.change, None, None, None, None, None, None, None, None)
    table.extend(sql.sxecute(query))
    sql_reader.table(table)



    
