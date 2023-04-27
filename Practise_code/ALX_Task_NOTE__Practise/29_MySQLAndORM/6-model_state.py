#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
        engine = create_engine("mysql+mysqldb:// otomisinsql:passwordTpass@localhost:3306/alx")
    Base.metadata.create_all(engine)
