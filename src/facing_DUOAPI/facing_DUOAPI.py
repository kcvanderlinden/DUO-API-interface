import requests

'''
Example table for the use in this package = https://onderwijsdata.duo.nl/datasets/adressen_vo/resources/5187f8d5-ff9c-4284-8e06-4311f0354956
'''
RESULTDICT = []
BASEURL = "https://onderwijsdata.duo.nl/"

def request(url):
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response = response.json()
        
        if response['success']:
            global RESULTDICT
            RESULTDICT += response['result']['records']
            total = response['result']['total']
            limit = response['result']['limit']
            offset = response['result']['offset'] if 'offset' in response['result'] else 0
            if total - offset > limit:
                nextUrl = response['result']["_links"]["next"]
                request(f"{BASEURL}{nextUrl}")
        else:
            print('Error:', response.get('error'))

def query(**kwargs):
    '''
    Query a DUO API table with the option to filter based on values in a column/key
    Parameters:
        resource_id: str
            id of table (e.g. '5187f8d5-ff9c-4284-8e06-4311f0354956')
        filters: str
            dictionary containing keys corresponding to columns and lists with values to filter in those columns (e.g. '{"GEMEENTENUMMER":["0944","0907","0893","0984","1507","1894","0983","0889"]}')
        limit: int
            amount to limit the call by. However the API uses the limit to limit the items per page and not the total amount retrieved. So, by limiting to 10, the total amount of rows is limitted by 10 per page, resulting in pages = total amount / limit.
    Returns a dictionary.
    '''
    global RESULTDICT
    url = urlConstructer(f"{BASEURL}api/3/action/datastore_search?", **kwargs)
    request(url)
    result = RESULTDICT.copy()
    RESULTDICT = []
    return result

def urlConstructer(baseUrl, **kwargs):
    url = f"{baseUrl}"
    url += "&".join(["%s=%s" % (key, kwargs[key]) for key in kwargs])
    return url    