import json

def solution(records):
	result = {}
	# ids = [i['id'] for i in records]
	parent_ids = [i['parent_id'] for i in records]
	for record in records:
		if record["parent_id"] is None:
			result[f"{record['name']}"] = []
		# elif record["parent_id"] is not None and record['id'] in parent_ids:
		# 	for i in records:
		# 		if i['id'] == record['parent_id']:
		# 			q = i['name']
		# 	result[q].append({f"{record['name']}":[]})
		# elif record["parent_id"] is not None and record['id'] not in parent_ids:
		else:
			check = record['parent_id']
			lst = [record]
			while check is not None:
				for i in records:
					if i["id"] == check:
						lst.append(i)
						check = i['parent_id'] 
						break
			char = f"result['{lst[-1]['name']}']"
			# print(lst, '--------lst----------')
			for i in range(len(lst)-1, 0, -1):
				eval_char = eval(char)
				# print(i, record['name'], '-----------i--------------')
				# print(eval_char, '-----------eval_char--------------')
				if i-1 == 0:
					# print(eval_char, type(eval_char))
					eval_char.append({f"{record['name']}":[]})	
					# print(eval_char, '=eval_char')
					break
				elif i-1 != 0:
					for j in range(len(eval_char)):
						# print(lst(eval_char[j].keys()), '----------jjjjjjjjjjj-----------')
						# j_keys = lst(eval_char[j].keys())
						if lst[i-1]['name'] == list(eval_char[j].keys())[0]:
							char += f"[{j}]['{lst[i-1]['name']}']"
							# print(eval_char, '----------eval_char-------------')
				else:	
					pass
					# for j in 
					# for j in eval_char:
					# 	print(j, '=========eval_char===========')
					# 	if lst[i]['name'] == list(j.keys())[0]:
					# 		print('yes') 
					# 	else:
					# 		eval_char.append({f"{record['name']}":[]})	
					# 		print(eval_char)	
	print(json.dumps(result, indent=2))	
# [{'id': 4, 'name': 'question4', 'parent_id': 3}, {'id': 3, 'name': 'question3', 'parent_id': 1}, 
# {'id': 1, 'name': 'question1', 'parent_id': None}]

records = [
    {"id": 1, "name": "question1", "parent_id": None},
    {"id": 2, "name": "question2", "parent_id": None},
    {"id": 3, "name": "question3", "parent_id": 1},
    {"id": 4, "name": "question4", "parent_id": 3},
    {"id": 5, "name": "question5", "parent_id": 2},
    {"id": 6, "name": "question6", "parent_id": 2},
    {"id": 7, "name": "question7", "parent_id": 3},
    {"id": 8, "name": "question8", "parent_id": 4},
    {"id": 9, "name": "question9", "parent_id": 4},
]
solution(records)
    # {"id": 7, "name": "question7", "parent_id": 3},
    # {"id": 8, "name": "question8", "parent_id": 3},

# n = {'question1': 
#  			[{'question3': [{'question4': []}, {'question7': []}]}], 'question2': [{'question5': []}, {'question6': []}]}
# n = json.dumps(n)
# n = n.replace("'", '"')
# print(n)