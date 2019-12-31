import urllib.request
import urllib.parse
import re

varUrl = 'http://pythonprogramming.net'

varValues = {
                's': 'basic',
                'submit': 'search'
            }

varData = urllib.parse.urlencode((varValues)) # urlencode changes the text into url desired form.
varData = varData.encode('utf-8') # Puts your data into bytes.
varReq = urllib.request.Request(varUrl, varData)
varResp = urllib.request.urlopen(varReq) # Same as x.
varRespData =varResp.read()

paragraphs = re.findall((r'<p>(.*?)<p>'), str(varRespData))

for i in paragraphs:
    print(i)
