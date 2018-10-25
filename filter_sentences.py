import json

data_list = []

with open('cleaned_big.json') as f:
	for line in f:
		data = json.loads(line)
		sentences = data["Sentences_t"]
		if sentences != "" and ("quake" in sentences.lower() or "zealand" in sentences.lower()):
			data_list.append(data)
			print(json.dumps(data))
