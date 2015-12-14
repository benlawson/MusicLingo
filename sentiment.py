import requests, json


with open('key.txt','r') as f:
    user = f.readline().strip()
    pwd = f.readline().strip()

def personality_insights(list_of_items, filename='bluemix.csv'):
    r = requests.post('https://gateway.watsonplatform.net/personality-insights/api' + '/v2/profile', 
                      auth=(user, pwd),
                      headers = {
                      'content-type': 'text/plain',
                        },
                data=json.dumps({'contentItems':list_of_items}))
    return parse_tree(json.loads(r.text)['tree'])

def parse_tree(tree):
    ret = []
    for i in tree['children']:
        for j in i['children']:
            for l in j['children']:
                try:
                    for k in l['children']:
                        if k['percentage'] > 0.8:
                            ret.append(k['name'])
                except:
                    pass
    return ret
