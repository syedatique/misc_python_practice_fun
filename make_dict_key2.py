import pdb, json

f = {"['columns', 'email']": 'david.moran.eureka@gmail.com', "['columns', 20, 'tranid']": '111', "['columns', 'item', 'name']": 'men timberland shoes'}

# Using defaultdict to create a nested dict
from collections import defaultdict
def deep_default_dict(level):
   result = {}
   while level > 1:
      result = lambda: defaultdict(result)
      level -= 1
   return result

# Set dict items in nested DICT
def getFromDict(dataDict, mapList):
  return reduce(lambda d, k: d[k], mapList, dataDict)

def setInDict(dataDict, mapList, value):
  getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value
# END

def nested_set(dic, keys, value):
  for key in keys[:-1]:
    # pdb.set_trace()
    if key != 0:
      dic = dic.setdefault(key, {})
    else:
      li = dic.setdefault(save_key, [])
      li.append(dic)
    save_key = key
  dic[keys[-1]] = value

# result = []

for k,v in f.iteritems():
  k_list = eval(k)
  d = deep_default_dict(len(k_list))()
  # d={}

  # setInDict(d, k_list, v)
  nested_set(d, k_list, v)
  # result.append(d)

  # print json.dumps(d, indent=3)

# print json.dumps(result, indent=3)


# Finally
import pdb, json
f = {"['columns', 'email']": 'david.moran.eureka@gmail.com', "['columns', 'tranid']": '111', "['columns', 'item', 'name']": 'men timberland shoes'}
f = {"[u'items', u'0', u'base_amount_refunded']": '2016-08-01T10:14:35.000Z', "[u'items', u'0', u'qty_refunded']": 'US'}
# f = {"['columns', 0, 'tranid']": '111',}

def nested_set(dic, keys, value):
  for key in keys[:-1]:
    # pdb.set_trace()
    dic = dic.setdefault(key, {})

  dic[keys[-1]] = value

new = {}
new_f=[]
for k,v in f.iteritems():
  k_list = eval(k)
  d={}
  nested_set(d, k_list, v)
  print json.dumps(d, indent=3)
  new_f.append(d)

print json.dumps(new_f, indent=3)

  # for k,v in d.iteritems():
  #   if k in new:
  #     new[k].update(v)
  #   else:
  #     new[k]=v
  # print json.dumps(new, indent=3)
  # # new = {}



