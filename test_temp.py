import httplib
import urllib

params = urllib.urlencode({'id':'-1','operator_id':'x'})
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
conn = httplib.HTTPConnection("sandbox.settlement.yongche.org")
conn.request("POST", "/V1/Citycommission/deleteById", params, headers)
response = conn.getresponse()
print response.read()

