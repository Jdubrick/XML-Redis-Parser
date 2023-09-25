import xml.dom.minidom
import os
import redis

def readXml():
    file_path = os.environ.get("FILE_PATH")    # will be used for docker version
    if file_path:
        try:
            doc = xml.dom.minidom.parse(file_path)
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

            return key_value_pairs
        except FileNotFoundError:
            print(f"File not found at {file_path}")
            
    else:
        print(f"File path not in environment variables.")
    
    return False

def writeXml(redisEntry, pairs):
    if not pairs:
        return False
    try:
        redisEntry.ping()
    except AttributeError:
        return False
    
    for key, val in pairs.items():
        if key == 'subdomains':
            for subdomain in val:
                redisEntry.rpush('subdomains', subdomain)
        else:
            redisEntry.set(key, val)
    
    return [key for key in redisEntry.keys()]


redisCli = redis.Redis(
    host='cache',
    port=6379,
    charset="utf-8",
    decode_responses=True
    )

pairs = readXml()
state = writeXml(redisCli, pairs)
print(state if state is not False else "Connection Failed")



