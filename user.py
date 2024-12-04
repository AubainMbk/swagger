from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


users = {
        "Farrell": {
        "username": "elliot",
        "competences": "bg",
        "age": 10,
        "cv": "cv_elliot",
        "timestamp": get_timestamp()
    },
        "HHHHH": {
        "username": "elliot",
        "competences": "bg",
        "age": 10,
        "cv": "cv_elliot",
        "timestamp": get_timestamp()
    },
}


def read():
    return [users[key] for key in sorted(users.keys())]

# def read_one(username):
#     if username in users:
#         return users[username]
#     else:
#         return {"error": "Person not found"}, 404

# def read_all():
#     return users

# def create(person):
#     lname = person.get("username")
#     if lname in users:
#         return {"error": "Person already exists"}, 400
#     users[lname] = {
#         "username": person.get("username"),
#         "competences": lname,
#         "timestamp": get_timestamp()
#     }
#     return users[lname], 201

# def update(lname, person):
#     if lname in users:
#         users[lname].update(person)
#         users[lname]["timestamp"] = get_timestamp()
#         return users[lname]
#     else:
#         return {"error": "Person not found"}, 404
    
# def delete(lname):
#     if lname in users:
#         del users[lname]
#         return {"message": "Person deleted"}
#     else:
#         return {"error": "Person not deleted"}, 404
