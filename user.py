from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


users = {
        "elliot": {
            "id": 1,
            "username": "elliot",
            "competences": "bg",
            "age": 20,
            "cv": "cv_elliot",
            "timestamp": get_timestamp()
        },
            "HHHHH": {
            "id": 2,
            "username": "elliot",
            "competences": "bg",
            "age": 10,
            "cv": "cv_elliot",
            "timestamp": get_timestamp()
        },
}

def create(user):
    username = user.get("username")
    if username in users:
        return {"error": "Person already exists"}, 400
    users[username] = {
        "id": len(users) + 1,
        "username": username,
        "competences": user.get("competences"),
        "age": user.get("age"),
        "cv": user.get("cv"),
        "created_at": get_timestamp()
    }
    return users[user], 201

def read_all():
    return users

def read_one(id):
    for user in users.values():
        if user["id"] == id:
            return user
    return {"error": "Person not found"}, 404


def update(id, user_data):
    for username, user in users.items():
        if user["id"] == id:
            users[username].update(user_data)
            return users[username]
    return {"error": "Person not found"}, 404
    
# def delete(lname):
#     if lname in users:
#         del users[lname]
#         return {"message": "Person deleted"}
#     else:
#         return {"error": "Person not deleted"}, 404
