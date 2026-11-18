```
    ___           __         
    / _ \___ _____/ /____ ____
    / ___/ _ `/ __/ __/ -_) __/
    /_/   \_,_/_/  \__/\__/_/   
    
    Parter v0.1
    Developed by Mark Scharonow
    https://mrk-fox.github.io
```

Specific components database manager.

> [!IMPORTANT]
> This project is under development. Suggestings and testing feedbacks are welcome!

# What is this?

This is a solution to a problem I have. Currently, I have thousands of electronic components lying around in a few boxes. They are separate and are easy to find, but hard to remember, therefore I do not know what I currenty have in stock. This is where Parter jumps in. It is a simple CLI SQLite DB wrapper managing all the necessarry commands for a variety of operations. 

# How does it work?

First, I connects to an existing DB and creates all the releations necessarry. Each component is assigend a component type (Cap, Resistor, Diode, etc.). Then all it's attributes get entered and saved as a tupel in the table. Now, by entering certain commands into the CLI we can search for parts easily. 

# How to deploy?

1. Create an empty SQLite database
2. Enter the DB location into the parter_tools/sql.py file.
3. Run the main file via `py main.py <flags>`

# Thanks...
to Hack Club - motivating me to work on my projects.
