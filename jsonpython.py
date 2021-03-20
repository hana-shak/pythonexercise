import json
# Sample JSON
userJSON = '{"fname":"John", "lname":"Doe", "age":30}'

# Parse to dict
user = json.loads(userJSON)

print(user['fname'])
# print(user)

# dict to json
car = {'make':'ford', 'model':'Mustang', 'year':1970}

carJSON = json.dumps(car)
print(carJSON)