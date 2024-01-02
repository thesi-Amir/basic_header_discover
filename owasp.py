import json, requests, sys

try:
   inputs = sys.argv[1]
   response = requests.head(inputs)
   headers_json = json.dumps(dict(response.headers))
   test = headers_json
   amir = (json.loads(headers_json))
   for i in amir:
       print("[+]=>  " + i + ":" + amir[i] + "\n")
except IndexError:
    print("please enter a url")
except requests.exceptions.MissingSchema:
    print("please enter correct url and address")