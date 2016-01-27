# created using python 2.7

import requests
import json

apiKey = 'your API key'
baseUrl = 'http://api.reimaginebanking.com'
accId = 'your account ID'


def getAtms(lat, lng, rad):
    pageno = 1

    while True:
        url = '%s/atms?lat=%s&lng=%s&rad=%s&key=%s&page=%s' % (baseUrl, lat, lng, rad, apiKey, pageno)
        response = requests.get(url)

        if len(response.json()['data']) > 0:
            print json.loads(str(json.dumps(response.text)))
            pageno += 1

        else:
            return


def getCustomers():
    url = '%s/customers?key=%s' % (baseUrl, apiKey)
    response = requests.get(url)
    data = json.loads(str(json.dumps(response.text)))
    return data


def getAccounts():
    url = '%s/accounts?&key=%s' % (baseUrl, apiKey)
    response = requests.get(url)
    data = json.loads(str(json.dumps(response.text)))
    return data


def getBillsByAccountId():
    url = '%s/accounts/%s/bills?key=%s' % (baseUrl, accId, apiKey)
    response = requests.get(url)
    data = json.loads(str(json.dumps(response.text)))
    return data


def getPurchasesByAccountId():
    url = '%s/accounts/%s/purchases?key=%s' % (baseUrl, accId, apiKey)
    response = requests.get(url)
    data = json.loads(str(json.dumps(response.text)))
    return data


def createDeposit(deposit):
    url = '%s/accounts/%s/deposits' % (baseUrl, accId)
    headers = {'content-type': 'application/json'}
    params = {'key': apiKey}
    response = requests.post(url, params=params, data=json.dumps(deposit), headers=headers)
    return response


def getEnterpriseByAccountId():
    url = '%s/enterprise/accounts/%s?key=%s' % (baseUrl, accId, apiKey)
    response = requests.get(url)
    data = json.loads(str(json.dumps(response.text)))
    return data


#  examples:

print 'atms GET: '
getAtms(38.882163, -77.1113105, 5)

print 'customers GET: ' + getCustomers()
print 'accounts GET: ' + getAccounts()
print 'bills GET: ' + getBillsByAccountId()
print 'purchases GET: ' + getPurchasesByAccountId()

deposit = {
    "medium": "balance",
    "transaction_date": "2016-01-27",
    "status": "pending",
    "amount": 500,
    "description": "test"
}

print 'deposit POST: ' + createDeposit(deposit).text
print 'enterprise GET: ' + getEnterpriseByAccountId()
