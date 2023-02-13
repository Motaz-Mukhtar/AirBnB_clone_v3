#!/usr/bin/python3
from models import storage
from models.user import User




for key in storage.all().values():
    print(key)


print(storage.all("User").values())
