import json

with open("SearchShowAction.json", encoding='utf-8-sig') as f:
    data = json.load(f)
    print(json.dumps(data, indent=4))