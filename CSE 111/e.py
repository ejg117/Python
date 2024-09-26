import json

mylist = {'name': 'Ephraim G', 'age' : 20, 'hobbies': ['Gym', 'Video games','Coding']}

with open ('data.json', 'w') as f: json.dump(mylist, f)

with open('data.json', 'r') as f: print(json.load(f))