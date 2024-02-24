import json

filter = {"rfc461Schema": "champion_kill"}

with open("game_example.jsonl", "r") as file:
    filtered_data = []

    for l in file:
        data = json.loads(l)
        if all(data.get(key) == value for key, value in filter.items()):
            filtered_data.append(data)

with open("filtered_data.json", "w") as outfile:
    json.dump(filtered_data, outfile, indent=4)
