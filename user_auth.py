users = {"admin": "password123"}

def login(username, password):
    if users.get(username) == password:
        return "Login successful"
    return "Invalid credentials"

def register(username, password):
    if username in users:
        return "User exists"
    users[username] = password
    return "Registration successful"

result = login("admin", "password123")
print(result)

result2 = login("unknown_user", "pass")
print(result2)
