
# First we need to import document modules from browser module
from browser import document, window
from browser import ajax

# Selecting button elements from dom
qodButtonElem = document.select('#qodButton')[0]
randomButtonElem = document['randomButton']

# Selecting Author and title element
authorElem = document['author']
quoteElem = document['quote']

URL_PREFIX = 'https://quotes.rest/'
QUOTE_OF_DAY_ROUTE = 'qod'

# Defining handler function


def getQouteOfTheDay(ev):
    req = ajax.Ajax()
    req.bind('complete', onCompleteQod)
    req.open('GET', 'https://quotes.rest/qod', True)
    req.set_header('accept', 'application/json')
    req.send()


def getRandomQuote(ev):
    req = ajax.Ajax()
    req.bind('complete', onCompleteQod)
    req.open('GET', 'https://quotes.rest/quote/random?language=en&limit=1', True)
    req.set_header('accept', 'application/json')
    req.set_header('X-TheySaidSo-Api-Secret', '<Your_Secret_API_KEY')
    req.send()
    print('Getting some random quote')


# Binding qodButtonElem to click event and passing handler function
qodButtonElem.bind('click', getQouteOfTheDay)
randomButtonElem.bind('click', getRandomQuote)

# Handler to handle what to do when request is completed
def onCompleteQod(req):
    if req.status == 200 or req.status == 0:
        obj = window.JSON.parse(req.text)
        quoteElem.text = '"'+obj["contents"]["quotes"][0]["quote"]+'"'
        authorElem.text = obj["contents"]["quotes"][0]["author"]
    else:
        print("error " + req.text)
