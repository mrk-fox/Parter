from parter_tools import sql as s

def mainprint():
    print(r"""
    ___           __         
    / _ \___ _____/ /____ ____
    / ___/ _ `/ __/ __/ -_) __/
    /_/   \_,_/_/  \__/\__/_/   
    
    Parter v0.1
    Developed by Mark Scharonow
    https://mrk-fox.github.io
    """)


def shorties():
    rows = s.sxecute("SELECT short, Type FROM Types")

    for short, name in rows:
        print(short + ": " + name)
