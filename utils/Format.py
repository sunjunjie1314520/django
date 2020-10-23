import json

def to_JSON_Format(data):
    print(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False))