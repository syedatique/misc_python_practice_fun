# def make_dict_key(K):
# 	try:
# 		hash(K)
# 		print K
# 	except TypeError:
# 		# Not hashable, so can't be used as a dictionary key.
# 		if isinstance(K, dict):
# 			print (type(K),) + tuple((key, make_dict_key(value)) for (key, value) in K.iteritems())
# 		else:
# 			try:
# 				print (type(K),) + tuple(make_dict_key(x) for x in K)
# 			except TypeError:
# 				# K is not a sequence-like object.
# 				print (type(K), repr(K))

# a = [[u'payment', u'additional_information', u'0'], [u'payment', u'base_amount_ordered']]

# make_dict_key(a)


# Set a given data in a dictionary with position provided as a list
# def setInDict(dataDict, mapList, value): 
#     for k in mapList[:-1]:
#     	dataDict = dataDict[eval(k)]
#     dataDict[mapList[-1]] = value

#     print dataDict

f = {"[u'columns', u'email']": 'david.moran.eureka@gmail.com', "[u'columns', u'tranid']": '111', "[u'columns', u'item', u'name']": 'men timberland shoes'}



# f = {"[u'columns', u'email']": 'david.moran.eureka@gmail.com'}
# d={}

# setInDict(d, eval(f.keys()[0]), f.values()[0] )

from collections import defaultdict
def deep_default_dict(level):
   result = {}
   while level > 1:
      result = lambda: defaultdict(result)
      level -= 1
   return result

# for k in f.iterkeys():
# 	k_list = eval(k)
# 	d = deep_default_dict(len(k_list))()
# 	for i in range(len(k_list)):
# 		d[i]
# 	d[]


d = deep_default_dict(4)()
# d["column"]["email"]["fff"]['fdfd']="test"
import json
# print json.dumps(d, indent=3)




# new approiach:

dataDict = {
    "a":{
        "r": 1,
        "s": 2,
        "t": 3
        },
    "b":{
        "u": 1,
        "v": {
            "x": 1,
            "y": 2,
            "z": 3
        },
        "w": 3
        }
}



def getFromDict(dataDict, mapList):
    return reduce(lambda d, k: d[k], mapList, dataDict)

def setInDict(dataDict, mapList, value):
	getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value

setInDict(d, ["b", "v", "w"], 4)

print json.dumps(d, indent=3)




