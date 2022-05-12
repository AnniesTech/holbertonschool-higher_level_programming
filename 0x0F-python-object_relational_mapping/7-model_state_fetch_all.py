#!/usr/bin/python3
"""
lists all State objects from a database
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)

    rows = eng.execute("SELECT * FROM states ORDER BY states.id;")
    for row in rows:
        print("{}: {}".format(row.id, row.name))
