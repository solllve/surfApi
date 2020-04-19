from flask import jsonify
from bs4 import BeautifulSoup
import requests
import json
import re
import urllib
import time
import json

class ScrapeAPI():
    def get(self, domain):
        print(domain)
        http = 'https://www.'
        url = domain
        headers = {
            'User-Agent': 'Chrome/[.0-9]*'
        }

        #vars
        response = requests.get(http + url, headers=headers)

        content = BeautifulSoup(response.content, "html.parser")

        loading = ['\\', '|', '/', '-']


        #if website exists
        if response.status_code == 200:

            #grabMetaDescription
            def getMetaDescription():
                if content.find("meta",  property="og:description") != None:
                    return description["content"]
                elif content.find('meta', property="description") != None:
                    return description["content"]

            #vars
            title = content.find('title').text.strip()
            description = content.find("meta",  property="og:description")

            #grab all meta
            metaList = []
            for meta in content.find_all('meta'):
                metaList.append(meta.get('content'))

            #arrays & objects
            scrapeArr = []
            metaObject = {
                'data': metaList
            }
            scrapeObj = {
                'title': title,
                'meta': metaObject,
                'description': getMetaDescription()
            }

            #generate JSON
            scrapeArr.append(scrapeObj)
            # with open('websiteData.json','w') as outfile: json.dump(scrapeArr, outfile)

            content = jsonify({
               "success": True,
               "results": scrapeArr
            })
            return content
