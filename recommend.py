import json

def load_data(filename):
    with open("massive_data.json","r") as f:
        return json.load(f)

        #people you may know
def find_people(user_id,data):
    user_friends = {} 
    for user in data['users']:
        user_friends[user['id']]=set(user['friends'])
    if user_id not in user_friends:
            return[]

    direct_friends =user_friends[user_id]   
    suggestion={}
    for friend in direct_friends:
        for mutual in user_friends[friend]:
            if mutual != user_id and mutual not in direct_friends:
                # count mutual friends
                suggestion[mutual]= suggestion.get(mutual,0)+1    
    sorted_suggestion =sorted(suggestion.items(),key=lambda x:x[1],reverse=True)
    return[user_id for user_id, count in sorted_suggestion]
#Load the data

data=load_data("massive_data.json")    
user_id= int(input("Of which user's mutual friend you want to know?\n"))
print("mutual friends of user_id.",user_id)
#user_id=1
recc =find_people(user_id,data)
print(recc)