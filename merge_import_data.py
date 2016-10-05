import pdb


d1 = {"items": [{"qty_refunded": "US"}]}

d3 = {"items": [{"Test": "test"}]}

d2 = {"items": [{"base_amount_refunded": "2016-08-01T10:14:35.000Z"}]}

e_data = [{"company": {"phone":"089"}}, {"field": "temp"}, {"Test":"test"}, {"Test11":"test11"},{"company":{"PostCode":"g4"}}, d1, d2,d3]

e_data = [
   {
      "OrderStatus": 1
   },
   {
      "TransactionArray": {
         "Transaction": [
            {
               "Taxes": {
                  "TotalTaxAmount": {
                     "_currencyID": "Prado"
                  }
               }
            }
         ]
      }
   },
   {
      "TransactionArray": {
         "Transaction": [
            {
               "TransactionPrice": {
                  "value": 100
               }
            }
         ]
      }
   }
]

# Rearranging the items of data, so that item with similar keys are separate
lists_group = []
# Step1: grab 1st element and compare, and make two lists with identical keys and non_identials
def extract_unique_key(lists):
	identical_group=[]
	non_identical_group=[]

	first_element = lists[0]
	first_element_key = first_element.keys()[0]
	# pdb.set_trace()
	for data in lists:
		if first_element_key == data.keys()[0]:
			identical_group.append(data) #List of dicts wth same keys
		else:
			non_identical_group.append(data) #List of dicts wth different keys

	if identical_group!=[]: lists_group.append(identical_group)

	if non_identical_group != []:
		extract_unique_key(non_identical_group)

	return lists_group # lists_group is a list of lists of dicts

y = extract_unique_key(e_data)
pdb.set_trace()

# print y
# >>> [[{'company': {'phone': '089'}}, {'company': {'PostCode': 'g4'}}], [{'field': 'temp'}], [{'Test': 'test'}], [{'Test11': 'test11'}], [{'items': [{'qty_refunded': 'US'}]}, {'items': [{'base_amount_refunded': '2016-08-01T10:14:35.000Z'}]}, {'items': [{'Test': 'test'}]}]]

# Step 2: Making the final import data structure/dicts
new_non_identical_keys_list = []
new_identical_keys_list = []

for data in y:
	if len(data) == 1:
		new_non_identical_keys_list.append(data[0])
	else:
		new_identical_keys_list.append(data)

# print new_identical_keys_list
# >>> [[{'company': {'phone': '089'}}, {'company': {'PostCode': 'g4'}}], [{'items': [{'qty_refunded': 'US'}]}, {'items': [{'base_amount_refunded': '2016-08-01T10:14:35.000Z'}]}, {'items': [{'Test': 'test'}]}]]
# print new_non_identical_keys_list
# >>> [{'field': 'temp'}, {'Test': 'test'}, {'Test11': 'test11'}]

# Merging dicts with identical keys
new_list = []
def merge_identical_keys(new_identical_keys_list11):
	# new_list = []
	for data in new_identical_keys_list11: 
		if isinstance(data[0].values()[0], dict): # [{'company': {'phone': '089'}}, {'company': {'PostCode': 'g4'}}]
			if data[0].values()[0].keys()[0] != data[1].values()[0].keys()[0]:
				data[1].values()[0].update(data[0].values()[0])
				rr = data[1].copy()
				# pdb.set_trace()
				# for i in range(len(data[2:])):
				# 	rr.values()[0].update(data[i+2].values()[0])
			else:
				if isinstance(data[0].values()[0].values()[0], list): # {"Transaction": [{"Taxes": {"TotalTaxAmount": {"_currencyID": "Prado"}},"TransactionPrice": {"value": 100}}]}
					if data[0].values()[0].values()[0][0].keys()[0] != data[1].values()[0].values()[0][0].keys()[0]:
						data[1].values()[0].values()[0][0].update(data[0].values()[0].values()[0][0])
						rr = data[1].copy()

			for i in range(len(data[2:])):
				rr.values()[0][0].update(data[i+2].values()[0][0])

			# print rr

			new_list.append(rr)
			# merge_identical_keys(new_list[0].values())
		
		if isinstance(data[0].values()[0], list): # {'items': [{'qty_refunded': 'US'}]}
			data[1].values()[0][0].update(data[0].values()[0][0])
			rr = data[1].copy()

			for i in range(len(data[2:])):
				rr.values()[0][0].update(data[i+2].values()[0][0])

			# print rr
			new_list.append(rr)
			# print new_list

merge_identical_keys(new_identical_keys_list)


new_non_identical_keys_list.extend(new_list)
# print new_non_identical_keys_list

final_import_dict = {}
for data in new_non_identical_keys_list:
	final_import_dict.update(data)

import json
a=json.dumps(final_import_dict, indent=3, sort_keys=True)


print a
# >>> {
#    "Test": "test",
#    "Test11": "test11",
#    "company": {
#       "PostCode": "g4",
#       "phone": "089"
#    },
#    "field": "temp",
#    "items": [
#       {
#          "Test": "test",
#          "base_amount_refunded": "2016-08-01T10:14:35.000Z",
#          "qty_refunded": "US"
#       }
#    ]
# }



# INFO     2016-08-15 09:26:34,584 handlers.py:3805] This is Field_Mapping logList: {
#    "OrderStatus": 1,
#    "TransactionArray": {
#       "Transaction": [
#          {
#             "Taxes": {
#                "TotalTaxAmount": {
#                   "_currencyID": "Prado"
#                }
#             }
#          }
#       ]
#    }
# }
















