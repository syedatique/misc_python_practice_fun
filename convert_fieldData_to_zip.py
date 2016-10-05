# Test creating field set for autocomplete

import pdb
postItem = {
                "id":"Product ID",
                "sku":"SKU",
                "name":"Product Name",
                "attribute_set_id":"Attribute ID",
                "price":"Price",
                "status":"Status, 0/1",
                "visibility":"e.g., 4",
                "type_id":"e.g., simple",
                "created_at":"e.g., 2016-05-20 18:09:56",
                "updated_at":"e.g., 2016-05-20 18:09:56",
                "weight":"e.g., 1",
                "extension_attributes":"e.g., []",
                "product_links":"e.g., []",
                "tier_prices":"e.g., []",
            }

# Extracting the path
def traverse(dic, key_name=None):
    if not key_name:
        key_name=[]
    if isinstance(dic,dict):
        for x in dic.keys():
            local_key_name = key_name[:]
            local_key_name.append(x)
            for b in traverse(dic[x], local_key_name):
                 yield b
    elif isinstance(dic, list):
        for data in dic:
            local_key_name = key_name[:]
            p = local_key_name
            path = p.append(0)
            # local_key_name = local_key_name.append(0)
            # key_name = local_key_name.append(0)
            for b in traverse(data, local_key_name):
                yield b
    else: 
        yield key_name,dic

if isinstance(postItem, dict):
    mykey_name = traverse(postItem) # mykey_name contains path(as key_name) and values(as dic) as well

    # pdb.set_trace()

    Keys = ["name", "label"]
    myList = []
    
    for i in mykey_name: # i = ([u'total_qty_ordered'], 0)
        Values = []
        Values.extend([ i[0],i[1] ])
        Dict = dict(zip(Keys, Values))
        
        myList.append(Dict)
elif isinstance(postItem, list):
    myList = postItem


return_data = {"data_preprocessed": postItem, "data_postprocessed": myList}

print return_data

