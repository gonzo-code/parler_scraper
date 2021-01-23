import requests
import urllib3
import certifi
import json
import csv

# This enables https request to happen
http = urllib3.PoolManager(
     cert_reqs='CERT_NONE',
     ca_certs=certifi.where()
)

#
urllib3.disable_warnings()

# Cookies is where authentication happens
cookies = {
    'mst': 'INSERT HERE',
    'jst': 'INSERT HERE',
}

headers = {
    'Host': 'api.parler.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Origin': 'https://parler.com',
    'Connection': 'close',
    'Referer': 'https://parler.com/search?hashtag=savethechildren',
}

# This searches where hashtag to pull data for
params = (
    ('tag', 'savethechildren'),
    ('limit', '10'),
)


response = requests.get('https://api.parler.com/v1/post/hashtag', headers=headers, params=params, cookies=cookies, verify=False )
info = json.loads(response.text)
print(info['posts'])

posts = info['posts']
users = info['users']
links = info['urls']



postFile = open('post_test.csv', 'w', newline='')
postWriter = csv.writer(postFile, delimiter=',')



sheetRow = []

for post in posts:
    sheetRow.append(post['_id'])
    sheetRow.append(post['body'])
    sheetRow.append(post['links'])
    sheetRow.append(post['creator'])
    postWriter.writerow([sheetRow[0], sheetRow[1], sheetRow[2], sheetRow[3]])
    print(post['links'])
    sheetRow.clear()

postFile.close()



usersFile = open('users_test.csv', 'w', newline='')
usersWriter = csv.writer(usersFile, delimiter=',')



for user in users:
    print(user['id'])
    sheetRow.append(user['id'])
    sheetRow.append(user['name'])
    sheetRow.append(user['username'])
    usersWriter.writerow([sheetRow[0], sheetRow[1], sheetRow[2]])
    #print(post['links'])
    sheetRow.clear()


linksFile = open('links_test.csv', 'w', newline='')
linksWriter = csv.writer(linksFile, delimiter=',')

for link in links:
    print(link['_id'])
    sheetRow.append(link['_id'])
    sheetRow.append(link['domain'])
    sheetRow.append(link['long'])
   # sheetRow.append(link['metadata']['description']description)
    linksWriter.writerow([sheetRow[0], sheetRow[1], sheetRow[2]])
    #print(post['links'])
    sheetRow.clear()
