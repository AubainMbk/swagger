from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


users = {
        "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp()
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp()
    }
}

def read():
    return [users[key] for key in sorted(users.keys())]

def read_one(lname):
    if lname in users:
        return users[lname]
    else:
        return {"error": "Person not found"}, 404

def read_all():
    return users

def create(person):
    lname = person.get("lname")
    if lname in users:
        return {"error": "Person already exists"}, 400
    users[lname] = {
        "fname": person.get("fname"),
        "lname": lname,
        "timestamp": get_timestamp()
    }
    return users[lname], 201

def update(lname, person):
    if lname in users:
        users[lname].update(person)
        users[lname]["timestamp"] = get_timestamp()
        return users[lname]
    else:
        return {"error": "Person not found"}, 404
    
def delete(lname):
    if lname in users:
        del users[lname]
        return {"message": "Person deleted"}
    else:
        return {"error": "Person not deleted"}, 404