from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):

    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):

    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    print(e)


def search_by_id(raw_html, id):

    html = BeautifulSoup(raw_html,'html.parser')
    table = html.find('table',{'id':'super-product-table'})
    data = table.find_all('a')
    for a in data:
        print(a.text)

raw_r = simple_get("http://www.dezmembraricorunca.ro/masini-dezmembrate/bmw-320-seria-3-e46-2001-stoc-25.html")
search_by_id(raw_r, 'calculator-airbag-bmw-320-seria-3-e46-2130.html')
