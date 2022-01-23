from bs4 import BeautifulSoup
import requests


#search = input("Enter what you want to search:")
search = "pizza"
params = {"q": search}

a = requests.get('https://www.bing.com/search', params)
print(a.url)

soup = BeautifulSoup(a.text, "html.parser")
result = soup.find("ol", {"id":"b_results"})
links = result.findAll("li", {"class":"b_algo"})


for i in links:
    print("text", i.find('a').text)
    print("link", i.find('a').attrs['href'])
    print("summary:", i.find('a').parent.parent.find('p').text)
    chilren = i.children

    child = i.find('h2')
    print(child.next_sibling)



#print(soup.prettify())
