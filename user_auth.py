users = {"admin": "password123"}

def login(username, password):
    if users[username] == password:
        return "Login successful"

def register(username, password):
    if username in users:
        return "User exists"
    users[username] == password

result = login("admin", "password123")
print(result)

result2 = login("unknown_user", "pass")
print(result2)
