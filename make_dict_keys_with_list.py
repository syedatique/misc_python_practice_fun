import json, pdb

f = { "['columns','tranid', 0,  'id', 'test']": '111' }
f = {"[u'items', u'0', u'base_amount_refunded']": '2016-08-01T10:14:35.000Z', "[u'items', u'0', u'qty_refunded']": 'US', "['columns','tranid', 'id', 'test']": '111' }
# ff = { "['columns','tranid', 0,  'id', 'test', 0, 'tt', 'pp']": '111' }

# key_list = []
# for key in f.iterkeys():
# 	key = eval(key) # ['columns', 0, 'tranid', 'id', 0, 'test']
# 	key_list = []
# 	for i,v in enumerate(key):
# 		if v==0:
# 			index=i
# 			new_key_next = key[index+1:]
# 			new_key_previous = key[:index]


# def nested_set(dic, keys, value):
# 	key = keys[:-1]
# 	# for key in keys[:-1]:
# 		# pdb.set_trace()

# 	for i,v in enumerate(key):
# 		while v !='0':
			
# 			index=i
# 			new_key_next = key[index+1:]
# 			new_key_previous = key[:index]
# 			dic = dic.setdefault(new_key_previous, "[new_key_next]")

# 	dic[keys[-1]] = value

# def nested_set(dic, keys, value):
	
# 	key = keys[:-1]
# 	pdb.set_trace()

# 	for i,v in enumerate(key):
# 		while v !=0:
# 			dic = dic.setdefault(v, {})
# 		index=i
# 		new_key_next = key[index+1:]
# 		# nested_set(dic, new_key_next, )
# 		new_key_previous = key[:index]
# 		dic.update(new_key_previous=new_key_next)
		
# 		dic = dic.setdefault(new_key_previous, "[new_key_next]")

# 	dic[keys[-1]] = value

f = {"'store_id'": 'USD', "'grand_total'": 'USD', "'status'": 'USD'}

def nested_set(dic, keys, value):
  for key in keys[:-1]:
    # pdb.set_trace()
    dic = dic.setdefault(key, {})

  dic[keys[-1]] = value


new = {}
new_f=[]
for k,v in f.iteritems():
  	k_list = eval(k)
  	if isinstance(k_list, list):
	  	if "0" in k_list:
		  	for i,value in enumerate(k_list):
		  		if value == '0':
		  			new_key_next = k_list[i+1:]
		  			new_key_previous = k_list[:i]

					d={}
					nested_set(d, new_key_next, v)

					p={}
					nested_set(p, new_key_previous, [d])

					new_f.append(p)

					print json.dumps(p, indent=4)

		else: 
			p={}
			nested_set(p, k_list, v)
			new_f.append(p)

	else:
		new_f.append({k_list:v})



print json.dumps(new_f, indent=4)





