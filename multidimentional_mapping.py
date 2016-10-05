import json
# dict1 = {'key21': 
# 				{	'key31': {'key41':41},
# 					'key32': {'key42':42}
# 				}
# 		}
# list1 = ['key21', 'key32', 'key42']
# #list1 = ['key21', 'key32', 'key42', 'bad-key'] # Test bad key



# item = dict1
# try:
#     for key in list1:
#             item = item[key]
# except (KeyError, TypeError):
#     print None
# else:
#     print item

# Example two
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
        },
    "c": 8
}    

maplist = ["b", "v", "y"]

# Get a given data from a dictionary with position provided as a list
def getFromDict(dataDict, mapList):    
    for k in mapList: dataDict = dataDict[k]
    return dataDict

# Set a given data in a dictionary with position provided as a list
def setInDict(dataDict, mapList, value): 
    for k in mapList[:-1]: dataDict = dataDict[k]
    dataDict[mapList[-1]] = value



Keys = ["name", "label"]
myList = []

mykey_name = [['tt'],['pp','99','ps'],['oo']]

for i in mykey_name:
    Values = []
    Values.extend([i,i])
    Dict = dict(zip(Keys, Values))
    
    myList.append(Dict)
print("This is send data: %s" %json.dumps(myList))

 
