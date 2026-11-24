# User authentication module

users = {}

def login(username, password):
    if username in users and users[username] == password:
        return "Login successful"
    else:
        return "Login failed"

def register(username, password):
    if username in users:
        return "User exists"
    users[username] = password
    return "User registered"

result = login("admin", "password123")
print(result)

result2 = login("unknown_user", "pass")
print(result2)