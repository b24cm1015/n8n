users = {"admin": "password123"}

def login(username, password):
    if username not in users or users[username] != password:
        return "Invalid credentials"
    return "Login successful"

def register(username, password):
    if username in users:
        return "User exists"
    users[username] = password
    return "Registration successful"

if __name__ == "__main__":
    result = login("admin", "password123")
    print(result)

    result2 = login("unknown_user", "pass")
    print(result2)
