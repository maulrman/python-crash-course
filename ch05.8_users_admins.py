users = [ 
    "admin", 
    "chorizong",
    "honkaihokky",
    "anon69",
    "patthematt",
    "yweh1"
]

empty_users = []

new_users = [
    "anon69",
    "alextheproducer",
    "yweh2",
    "grumanns"
]

current_users = [ u.lower() for u in users]

if empty_users:
    print("Not empty.")
else:
    print("We need to find some users!")

for u in users:
    if u == "admin":
        print(f"hello {u}, would you like a status report?")
    else:
        print(f"hello {u}, thank you for logging in.")

for u in new_users:
    if u.lower() in current_users:
        print(f"{u} is not available, use a different name.")
    else:
        print("username available.")
