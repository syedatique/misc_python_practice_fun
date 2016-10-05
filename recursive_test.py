# def recursiveList(traversedata,list):
#     tempData = traversedata
#     print ("Line 4: %s" %tempData)
#     if not list:
#         return tempData
#     else:
#         for i,val in enumerate(list):
#             if val is not 0:
#                 data = traversedata.get(val) # if val not found in Keys, it would return None.
#                 if data == "Invalid Request": # "Invalid request" or None?!
#                     data = ""
#             else:
#                 data = traversedata[0] # ???? traversedata is a list??!
            
#             del list[i]
#             print ("The Data: %s" %data)

#             return recursiveList(traversedata,list) # ???? will it be : recursiveList(traversedata, list) ?!


# loggingMapping = {  "companyid":"EU",
#                     "uniqueid": ["Transaction","TransactionArray",0,"ShippingDetails","SellingManagerSalesRecordNumber"],
#                 }
# logDict = {}
# exportdata = {"company": "EU", "field": "temp", "uniqueid": ["P", "B"], "TransactionArray": "Test"}
    
# for key,value in loggingMapping.viewitems():     
#     if type(value) is list:
#         tempLogMap = list(value)
#         print tempLogMap
#         fieldvalue = recursiveList(exportdata,tempLogMap)
#         logDict[key] = fieldvalue
#     else:
#         logDict[key] = exportdata.get(value)  #?? exportdata.get(key)

# print ("This is final output: %s" %logDict)





orderArray = {
            'SellerEmail': 'andrew.douglas@eurekasolutions.co.uk',
            'ShippingAddress': {
                'PostalCode': None,
                'Street1': None,
                'Street2': None,
                'StateOrProvince': None,
                'Phone': None,
                'ExternalAddressID': None,
                'Name': None,
                'CountryName': None,
                'CityName': None
            },
            'PaymentHoldStatus': 'None',
            'Total': {
                '_currencyID': 'USD',
                'value': '15.0'
            },
            'Subtotal': {
                '_currencyID': 'USD',
                'value': '10.0'
            },
            'OrderID': '110182207843-0',
            'CheckoutStatus': {
                'Status': 'Incomplete',
                'eBayPaymentStatus': 'NoPaymentFailure',
                'LastModifiedTime': '2016-08-01T10:14:35.000Z',
                'PaymentMethod': 'None',
                'IntegratedMerchantCreditCardEnabled': 'false'
            },
            'OrderStatus': 'Active',
            'AmountSaved': {
                '_currencyID': 'USD',
                'value': '0.0'
            },
            'AdjustmentAmount': {
                '_currencyID': 'USD',
                'value': '0.0'
            },
            'CreatedTime': '2016-08-01T10:14:35.000Z',
            'IsMultiLegShipping': 'false',
            'EIASToken': 'nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GhDJWApgqdj6x9nY+seQ==',
            'IntegratedMerchantCreditCardEnabled': 'false',
            'ShippingServiceSelected': {
                'ShippingService': 'StandardShippingFromOutsideUS',
                'ShippingServiceCost': {
                    '_currencyID': 'USD',
                    'value': '5.0'
                }
            },
            'ShippingDetails': {
                'GetItFast': 'false',
                'SellingManagerSalesRecordNumber': '111',
                'ShippingServiceOptions': {
                    'ExpeditedService': 'false',
                    'ShippingService': 'StandardShippingFromOutsideUS',
                    'ShippingServicePriority': '1',
                    'ShippingTimeMax': '10',
                    'ShippingServiceCost': {
                        '_currencyID': 'USD',
                        'value': '5.0'
                    },
                    'ShippingTimeMin': '5'
                },
                'SalesTax': {
                    'SalesTaxPercent': '0.0',
                    'ShippingIncludedInTax': 'false',
                    'SalesTaxAmount': {
                        '_currencyID': 'USD',
                        'value': '0.0'
                    },
                    'SalesTaxState': None
                }
            },
            'AmountPaid': {
                '_currencyID': 'USD',
                'value': '0.0'
            },
            'BuyerUserID': 'testuser_eureka2',
            'PaymentMethods': 'PayPal',
            'TransactionArray': {
                'Transaction': [{
                    'TransactionID': '0',
                    'QuantityPurchased': '1',
                    'TransactionPrice': {
                        '_currencyID': 'USD',
                        'value': '10.0'
                    },
                    'Status': {
                        'PaymentHoldStatus': 'None'
                    },
                    'TransactionSiteID': 'US',
                    'Buyer': {
                        'UserFirstName': None,
                        'UserLastName': None,
                        'Email': 'david.moran.eureka@gmail.com'
                    },
                    'Platform': 'eBay',
                    'CreatedDate': '2016-08-01T10:14:35.000Z',
                    'OrderLineItemID': '110182207843-0',
                    'Item': {
                        'ItemID': '110182207843',
                        'ConditionID': '1000',
                        'Site': 'US',
                        'ConditionDisplayName': 'New with box',
                        'Title': 'men timberland shoes'
                    },
                    'Taxes': {
                        'TotalTaxAmount': {
                            '_currencyID': 'USD',
                            'value': '0.0'
                        },
                        'TaxDetails': [{
                            'TaxAmount': {
                                '_currencyID': 'USD',
                                'value': '0.0'
                            },
                            'TaxOnSubtotalAmount': {
                                '_currencyID': 'USD',
                                'value': '0.0'
                            },
                            'TaxOnHandlingAmount': {
                                '_currencyID': 'USD',
                                'value': '0.0'
                            },
                            'Imposition': 'SalesTax',
                            'TaxDescription': 'SalesTax',
                            'TaxOnShippingAmount': {
                                '_currencyID': 'USD',
                                'value': '0.0'
                            }
                        }, {
                            'TaxAmount': {
                                '_currencyID': 'USD',
                                'value': '0.0'
                            },
                            'Imposition': 'WasteRecyclingFee',
                            'TaxDescription': 'ElectronicWasteRecyclingFee'
                        }]
                    },
                    'ShippingDetails': {
                        'SellingManagerSalesRecordNumber': '111'
                    }
                }]
            }
        }

# print orderArray
fields = []

def walk_dict(d):

    for k,v in d.items():
        if isinstance(v, dict):
            walk_dict(v)
        elif isinstance(v, list):
            for data in v:
                walk_dict(data)
        else:
            fields.append(k)
            # print "%s %s" % (k, v)
            # print fields

walk_dict(orderArray)
print fields

# ressult:
# rderID 110182207843-0
# CountryName None
# Phone None
# Name None
# ExternalAddressID None
# PostalCode None
# Street1 None
# Street2 None
# StateOrProvince None
# CityName None
# PaymentHoldStatus None
# BuyerUserID testuser_eureka2
# SellerEmail andrew.douglas@eurekasolutions.co.uk
# Status Incomplete
# PaymentMethod None
# LastModifiedTime 2016-08-01T10:14:35.000Z
# eBayPaymentStatus NoPaymentFailure
# IntegratedMerchantCreditCardEnabled false
# EIASToken nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GhDJWApgqdj6x9nY+seQ==
# _currencyID USD
# value 10.0
# CreatedDate 2016-08-01T10:14:35.000Z
# _currencyID USD
# value 0.0
# _currencyID USD
# value 0.0
# _currencyID USD
# value 0.0
# Imposition SalesTax
# _currencyID USD
# value 0.0
# TaxDescription SalesTax
# _currencyID USD
# value 0.0
# _currencyID USD
# value 0.0
# Imposition WasteRecyclingFee
# TaxDescription ElectronicWasteRecyclingFee
# Platform eBay
# OrderLineItemID 110182207843-0
# PaymentHoldStatus None
# ItemID 110182207843
# ConditionID 1000
# Site US
# ConditionDisplayName New with box
# Title men timberland shoes
# TransactionSiteID US
# QuantityPurchased 1
# UserFirstName None
# UserLastName None
# Email david.moran.eureka@gmail.com
# TransactionID 0
# SellingManagerSalesRecordNumber 111
# _currencyID USD
# value 0.0
# IntegratedMerchantCreditCardEnabled false
# ShippingService StandardShippingFromOutsideUS
# _currencyID USD
# value 5.0
# IsMultiLegShipping false
# OrderStatus Active
# _currencyID USD
# value 0.0
# PaymentMethods PayPal
# CreatedTime 2016-08-01T10:14:35.000Z
# _currencyID USD
# value 15.0
# _currencyID USD
# value 10.0
# _currencyID USD
# value 0.0
# GetItFast false
# SellingManagerSalesRecordNumber 111
# ShippingTimeMax 10
# _currencyID USD
# value 5.0
# ShippingServicePriority 1
# ShippingService StandardShippingFromOutsideUS
# ExpeditedService false
# ShippingTimeMin 5
# SalesTaxPercent 0.0
# ShippingIncludedInTax false
# _currencyID USD
# value 0.0
# SalesTaxState None



# Also, you are missing the keys when the values are dictionaries.
def walk_dict_all_keys(d,depth=0):
    for k,v in sorted(d.items(),key=lambda x: x[0]):
        if isinstance(v, dict):
            print ("  ")*depth + ("%s" % k)
            walk_dict_all_keys(v,depth+1)
        elif isinstance(v, list):
            print ("  ")*depth + ("%s" % k)
            for data in v:
                walk_dict_all_keys(data,depth+1)

        else:
            print ("  ")*depth + "%s %s" % (k, v)


# walk_dict_all_keys(orderArray)

# ressult:
# AdjustmentAmount
#   _currencyID USD
#   value 0.0
# AmountPaid
#   _currencyID USD
#   value 0.0
# AmountSaved
#   _currencyID USD
#   value 0.0
# BuyerUserID testuser_eureka2
# CheckoutStatus
#   IntegratedMerchantCreditCardEnabled false
#   LastModifiedTime 2016-08-01T10:14:35.000Z
#   PaymentMethod None
#   Status Incomplete
#   eBayPaymentStatus NoPaymentFailure
# CreatedTime 2016-08-01T10:14:35.000Z
# EIASToken nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GhDJWApgqdj6x9nY+seQ==
# IntegratedMerchantCreditCardEnabled false
# IsMultiLegShipping false
# OrderID 110182207843-0
# OrderStatus Active
# PaymentHoldStatus None
# PaymentMethods PayPal
# SellerEmail andrew.douglas@eurekasolutions.co.uk
# ShippingAddress
#   CityName None
#   CountryName None
#   ExternalAddressID None
#   Name None
#   Phone None
#   PostalCode None
#   StateOrProvince None
#   Street1 None
#   Street2 None
# ShippingDetails
#   GetItFast false
#   SalesTax
#     SalesTaxAmount
#       _currencyID USD
#       value 0.0
#     SalesTaxPercent 0.0
#     SalesTaxState None
#     ShippingIncludedInTax false
#   SellingManagerSalesRecordNumber 111
#   ShippingServiceOptions
#     ExpeditedService false
#     ShippingService StandardShippingFromOutsideUS
#     ShippingServiceCost
#       _currencyID USD
#       value 5.0
#     ShippingServicePriority 1
#     ShippingTimeMax 10
#     ShippingTimeMin 5
# ShippingServiceSelected
#   ShippingService StandardShippingFromOutsideUS
#   ShippingServiceCost
#     _currencyID USD
#     value 5.0
# Subtotal
#   _currencyID USD
#   value 10.0
# Total
#   _currencyID USD
#   value 15.0
# TransactionArray
#   Transaction
#     Buyer
#       Email david.moran.eureka@gmail.com
#       UserFirstName None
#       UserLastName None
#     CreatedDate 2016-08-01T10:14:35.000Z
#     Item
#       ConditionDisplayName New with box
#       ConditionID 1000
#       ItemID 110182207843
#       Site US
#       Title men timberland shoes
#     OrderLineItemID 110182207843-0
#     Platform eBay
#     QuantityPurchased 1
#     ShippingDetails
#       SellingManagerSalesRecordNumber 111
#     Status
#       PaymentHoldStatus None
#     Taxes
#       TaxDetails
#         Imposition SalesTax
#         TaxAmount
#           _currencyID USD
#           value 0.0
#         TaxDescription SalesTax
#         TaxOnHandlingAmount
#           _currencyID USD
#           value 0.0
#         TaxOnShippingAmount
#           _currencyID USD
#           value 0.0
#         TaxOnSubtotalAmount
#           _currencyID USD
#           value 0.0
#         Imposition WasteRecyclingFee
#         TaxAmount
#           _currencyID USD
#           value 0.0
#         TaxDescription ElectronicWasteRecyclingFee
#       TotalTaxAmount
#         _currencyID USD
#         value 0.0
#     TransactionID 0
#     TransactionPrice
#       _currencyID USD
#       value 10.0
#     TransactionSiteID US

field_data = {}

def recursiveField(d):
    for key,value in d.iteritems():
        if isinstance(value, dict):
            recursiveField(value)
        elif isinstance(value, list):
            for data in value:
                recursiveField(data)
        else:
            field_data[key] = value
            # print "%s %s" % (k, v)

recursiveField(orderArray)

for field_name, field_value in field_data.iteritems():
    if field_name == 'SellingManagerSalesRecordNumber':
        print field_value

