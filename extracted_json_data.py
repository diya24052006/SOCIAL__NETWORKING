import json

def load_data(filename):
  with open(filename,"r")as f:
    data=json.load(f)
    return data

data =load_data("data1.json")
"""print(data)"""

def display_users(data):
    print("user names and their connection information")
    for user in data['users']:
        print(f"user Id is {user['id']}). {user['name']} is friends with{user['friends']}liked pages are{user['liked_pages']}")
    print("\npages information\n")    
    for page in data['pages']:
        print(f"{page['id']}:{page['name']}")   

print(display_users(data))        