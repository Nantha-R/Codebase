import json

json_content = '{"name":"Codebase"}'
contents = json.loads(json_content)
# contents is a dict containing the json records
print(contents['name'])
