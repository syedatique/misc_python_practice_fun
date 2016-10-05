import pdb
order1= {
    'ShippingAddress': {
        'PostalCode': "G4",
    },
}

order2= {
    'ShippingAddress': {
        'Mobile': 076,
    },
}



def merge_nested_dict(dict1, dict2):
    if dict1.keys()[0] == dict2.keys()[0]:
        # merge_dict(dict1.values()[0],dict2.values()[0])
        dict1.values()[0].update(dict2.values()[0])

    else:
        # new_order=dict1.copy()
        dict1.update(dict2)
        # print new_order
    # print dict1
    return dict1

new_order = merge_nested_dict(order1, order2)

print new_order






# Changing original dict
d1 = {
        "items": [
            {
                "qty_refunded": "US", "Test": "test"
            }
        ]
    }

d2 = {
        "items": [
            {
                "base_amount_refunded": "2016-08-01T10:14:35.000Z"
            }
        ]
    }

d3 = {}

rr={}

# pdb.set_trace()
d1.values()[0][0].update(d2.values()[0][0])
rr =d1.copy()
print d1
# >>> {'items': [{'Test': 'test', 'base_amount_refunded': '2016-08-01T10:14:35.000Z', 'qty_refunded': 'US'}]}

# Another way: Not Changing original dict
d1 = {
        "items": [
            {
                "qty_refunded": "US", "Test": "test"
            }
        ]
    }

d2 = {
        "items": [
            {
                "base_amount_refunded": "2016-08-01T10:14:35.000Z"
            }
        ]
    }

d3 = {}

for k, v in d1.iteritems():
    r = []
    k1 = dict(d.items()[0] for d in d1[k])
    r.append(k1)

    k2 = dict(d.items()[0] for d in d2[k])
    r.append(k2)
    d3[k]=r
    # d1[k] = r
    # d3=d1.copy() 
print d3
# >>> {'items': [{'Test': 'test'}, {'base_amount_refunded': '2016-08-01T10:14:35.000Z'}]}


# Another way: Not Changing original dict
new_list = []
new_list.extend([d1, d2])
# >>> [{'items': [{'qty_refunded': 'US'}]}, {'items': [{'base_amount_refunded': '2016-08-01T10:14:35.000Z'}]}]
new_dict = {}
for dicts in new_list:
   for key, value in dicts.items():
      new_dict.setdefault(key,[]).extend(value)

print new_dict
# >>>{'items': [{'Test': 'test', 'qty_refunded': 'US'}, {'base_amount_refunded': '2016-08-01T10:14:35.000Z'}]}
print d1, d2




    