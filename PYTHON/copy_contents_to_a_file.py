import json

def write_file(file_name, contents):
    file = open(file_name,'w')
    # if file does not exists new file with the given name is created
    file.write(json.dumps(contents))
    file.close()

def read_file(file_name):
    file = open(file_name,'r')
    data = file.read()
    file.close()
    return json.loads(data) # Converts the string object to a list

contents = ['1','2','3','4','5']
write_file("contents.txt",contents)
contents = read_file("contents.txt")
print(contents) # prints ['1','2','3','4','5']
