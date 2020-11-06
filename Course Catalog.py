import requests
response=requests.get('http://www.marymount.edu')

We are doing two things in this call. w=Our library is going to the marymount webpage and returning the html/javascript/and full network response. We are assigning the response to a variable called 'response'
print(response.headers)
print(response.status_code)

The headers gives alot of information about the request/response such as encodings. Some of this information will be uised in advanced scripting. The Status Code is more useful immediately for us as it tells us if we correctly loaded the page. a code of 200 is Successful

import re

matches = re.findall(r'eventid=\d+"><h6>([\w,\s]+)</h6>', text)
for event in matches:
    print(event)