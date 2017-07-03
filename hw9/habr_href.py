import re
import requests

re_href = re.compile(r'href=[\'"]?([^\'" >]+)')

def find_href(url):
    print("Find all hrefs on page {}".format(url))
    page = requests.get(url)
    return re_href.findall(page.text)


if __name__ == '__main__':
    url = "https://habrahabr.ru"
    hrefs = find_href(url)
    print("\n".join(hrefs))