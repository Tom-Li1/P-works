people = {
	'Peter':{
	'phone':'2341',
	'addr':'Foo Drive 23'
	},

	'Bill':{
	'phone':'9181',
	'addr':'Bar street 32'
	},

	'Eric':{
	'phone':'8279',
	'addr':'Baz avenue 90'
	}
}

labels = {
	'phone':'phone number',
	'addr':'address'
}

name = input("Name:")
request = input("Phone number(p) or address(a)?")

if request == 'p':
	key = 'phone'
if request == 'a':
	key = 'addr'

if name in people:
	print("{}'s {} is {}".format(name, labels[key], people[name][key]))