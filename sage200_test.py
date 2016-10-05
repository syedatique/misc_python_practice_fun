import httplib, urllib, base64, pdb

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '7ecc4d8095eb442c80e07cbeb3143a1b',
    'Content-Type': 'application/json'
	}

params = urllib.urlencode({
	})

# >>> urllib.urlencode({"data": {"wifi":{"ssid":"guest","rssi":"80"}}})
# 'data=%7B%27wifi%27%3A+%7B%27rssi%27%3A+%2780%27%2C+%27ssid%27%3A+%27guest%27%7D%7D'

try:
    conn = httplib.HTTPSConnection('api.columbus.sage.com')
    conn.request("GET", "/uk/sage200/accounts/v1/current_user?%s" % params, "", headers)
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    # pdb.set_trace()
    print(data)
    conn.close()
except Exception as e:
    # print("[Errno {0}] {1}".format(e.errno, e.strerror))
    print "Error occured"


# @ECHO OFF

# curl -v -X GET "https://api.columbus.sage.com/uk/sage200/accounts/v1/current_user"
# -H "Ocp-Apim-Subscription-Key: 503d72ad6f5f4100bbbfe5e861e9266a"

# # --data-ascii "{body}" 