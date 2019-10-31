import sys
from bs4 import BeautifulSoup

# Remember to set the ENV variable properly to read UTF-8 character
# See: https://stackoverflow.com/a/35236698
soup = BeautifulSoup(sys.stdin.read(), 'html5lib')

for h4 in soup.findAll('h4'):
    category_tag = h4.contents[0]
    category_link = category_tag["href"]
    category_name = category_tag.contents[0]
    top3_tag = h4.next_sibling.findAll('a')
    for a in top3_tag:
        href = a['href']
        if href.startswith('/artifact') and not href.endswith('/usages'):
            library_group_id = href
            library_name = a.contents[0]
            print category_name + ',' + category_link + ',' + library_name + ',' + library_group_id
