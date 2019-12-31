import urllib.request # Used to do get of get and post.
import urllib.parse

# x = urllib.request.urlopen('https://www.google.com') # To get the sourcecode of a web page.
# print(x.read())

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

print(varRespData)

try:
    varX = urllib.request.urlopen('https://www.google.com')
    print(varX.read())
except Exception as e:
    print(e)

try:
    varUrl = 'https://www.google.com/search?q=test'

    varHeaders = {}
    varHeaders['User-Agent'] = 'Mozilla/5.0 (X11;Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chromw/24.0.131.12.27 Safari/537.17' # Import from telegram.
    varReq = urllib.request.Request(varUrl, headers = varHeaders)
    varResp = urllib.request.urlopen(varReq)
    varRespData = varResp.read()

    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(varRespData))
    saveFile.close()
except Exception as e:
    print(e)
