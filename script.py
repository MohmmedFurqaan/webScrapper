import requests
from bs4 import BeautifulSoup

class HackerNews:
    def __init__(self, api_link):
        self.api_link = api_link

    def requesting_the_data_API(self):
        res = requests.get(self.api_link)        
        if res.status_code != 200:
            print(f'Error fetching data. Check the URL and try again! Status Code = {res.status_code}')
            return None, None  
        else:
            soup = BeautifulSoup(res.text, 'html.parser')
            links = soup.select('.titleline > a')
            subtext = soup.select('.subtext')
            return links, subtext  # Returning extracted data

    @staticmethod
    def sorting_the_data(hn):
        return sorted(hn, key=lambda x: x['votes'], reverse=True)  # Sorting based on votes in descending order
    def parsing_the_data(self, links, subtext):
        hn = []
        for idx, item in enumerate(links):
            title = item.getText()
            href = item.get('href', None)
            vote_section = subtext[idx].select('.score')
            points = int(vote_section[0].getText().replace(' points', '')) if vote_section else 0
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})

        return self.sorting_the_data(hn)  



# Creating objects for different pages

obj1 = HackerNews('https://news.ycombinator.com/news')

obj2 = HackerNews('https://news.ycombinator.com/?p=2')

# Fetching data for obj1

links1, subtext1 = obj1.requesting_the_data_API()
if links1 and subtext1:
    news_data1 = obj1.parsing_the_data(links1, subtext1)
    print("\n--- Page 1 News ---")
    for item in news_data1:
        print(item)

# Fetching data for obj2

links2, subtext2 = obj2.requesting_the_data_API()
if links2 and subtext2:
    news_data2 = obj2.parsing_the_data(links2, subtext2)
    print("\n--- Page 2 News ---")
    for item in news_data2:
        print(item)

