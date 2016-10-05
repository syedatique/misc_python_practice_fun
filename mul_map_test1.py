import pdb


data = {
    'ReturnedOrderCountActual': '1',
    'OrderArray': {
        'Order': [{
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
                        'TotalTaxAmount': {'_currencyID': 'USD','value': '0.0'},
                        'TaxDetails': [
                                    {
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
                                    },
                                    {
                                        'TaxAmount': {'_currencyID': 'USD','value': '0.0'},
                                        'Imposition': 'WasteRecyclingFee',
                                        'TaxDescription': 'ElectronicWasteRecyclingFee'
                                }
                        ]
                    },
                    'ShippingDetails': {
                        'SellingManagerSalesRecordNumber': '111'
                    }
                }]
            }
        }]
    },
    'Ack': 'Success',
    'PaginationResult': {
        'TotalNumberOfPages': '1',
        'TotalNumberOfEntries': '1'
    },
    'Build': 'E949_CORE_API_17937590_R1',
    'Timestamp': '2016-08-01T10:18:27.821Z',
    'OrdersPerPage': '100',
    'HasMoreOrders': 'false',
    'PageNumber': '1',
    'Version': '949'
}

pdb.set_trace()
# f = {"[u'columns', u'email']": 'david.moran.eureka@gmail.com', "[u'columns', u'tranid']": '111', "[u'columns', u'item', u'name']": 'men timberland shoes'}

def traverse(dic, path=None):
    if not path:
        path=[]
    if isinstance(dic,dict):
        for x in dic.keys():
            local_path = path[:]
            local_path.append(x)
            # pdb.set_trace()
            for b in traverse(dic[x], local_path):
                 yield b
    elif isinstance(dic, list):
        for data in dic:
            local_path = path[:]
            p = local_path
            path = p.append(0)
            # path = p
            for b in traverse(data, local_path):
                yield b
    else: 
        yield path,dic

mypath = traverse(data)

for i in mypath:
    print i[0]



