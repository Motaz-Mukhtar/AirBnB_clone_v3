#!/usr/bin/python3



from models import storage
from models.state import State


print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

first_state_id = list(storage.all(State).values())[0].id
print("First State: {}".format(storage.get(State, first_state_id)))
