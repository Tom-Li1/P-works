def init(data):
    data['first']={}
    data['middle']={}
    data['last']={}

def lookup(data, label, name):
    return data[label].get(name)

def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, '')
    labels = 'first', 'middle', 'last'

    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]
            
storage = {}
init(storage)
while True:
    f_n = input("Full name(q to quit):")
    if f_n == 'q':
        break
    store(storage, f_n)

a = input("Label(first middle last):")
b = input("Part of full name:")
print(lookup(storage, a, b))