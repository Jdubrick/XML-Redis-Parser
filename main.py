import xml.dom.minidom
import os
import sys

def readXml():
    #file_path = os.getenv("file")    # will be used for docker version
    doc = xml.dom.minidom.parse(sys.argv[1])
    key_value_pairs = {"subdomains": []} # can set subdomains to an empty list by default 

    
    subdomains = doc.getElementsByTagName('subdomains')
    for sub in subdomains[0].getElementsByTagName('subdomain'):
        key_value_pairs['subdomains'].append(sub.firstChild.nodeValue)
        
    cookies = doc.getElementsByTagName('cookies')
    for cookie in cookies[0].getElementsByTagName('cookie'):
        name = cookie.getAttribute('name')
        host = cookie.getAttribute('host')
        val = cookie.firstChild.nodeValue
        key_value_pairs[f"cookie:{name}:{host}"] = val

    print(key_value_pairs) #TODO: this needs to not be a python dict but needs to go to Redis instead
readXml()