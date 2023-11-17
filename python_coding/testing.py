import json

n = {'question1': 
 			[{'question3': [{'question4': []}, {'question7': []}]}], 'question2': [{'question5': []}, {'question6': []}]}
n = json.dumps(n)
n = n.replace("'", '"')
n = json.loads(n)
print(json.dumps(n, indent=2))