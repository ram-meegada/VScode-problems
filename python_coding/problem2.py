import json

def solution(records, final_result):
	for record in records:
		result = {}
		if record["parent_id"] is None:
			result[f"name"] = f"{record['name']}"
			result[f"id"] = record['id']
			result[f"children"] = []
			final_result.append(result)
		elif record["parent_id"] is not None:
			check = record['parent_id']
			lst = [record]
			while check is not None:
				for i in records:
					if i["id"] == check:
						lst.append(i)
						check = i['parent_id'] 
						break
			for k in range(len(final_result)):
				if lst[-1]['id'] == final_result[k]['id']:
					char = f"final_result[{k}]['children']"
					break
			for i in range(len(lst)-1, 0, -1):
				eval_char = eval(char)
				if i-1 == 0:
					temp = {}
					temp['name'] = record['name']
					temp['id'] = record['id']
					temp['children'] = []
					eval_char.append(temp)	
					break
				elif i-1 != 0:
					for j in range(len(eval_char)):
						if lst[i-1]['id'] == eval_char[j]['id']:
								char += f"[{j}]['children']"
				else:	
					pass
	print(json.dumps(final_result, indent=2))	

records = [
    {"id": 1, "name": "question1", "parent_id": None},
    {"id": 2, "name": "question2", "parent_id": None},
    {"id": 3, "name": "question3", "parent_id": 1},
    {"id": 4, "name": "question4", "parent_id": 3},
    {"id": 5, "name": "question5", "parent_id": 2},
    {"id": 6, "name": "question6", "parent_id": 2},
    {"id": 7, "name": "question7", "parent_id": 3},
    {"id": 8, "name": "question8", "parent_id": 4},
    {"id": 9, "name": "question9", "parent_id": None},
]
final_result = []
solution(records, final_result)

