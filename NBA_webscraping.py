from bs4 import BeautifulSoup
import requests
import string

URL = "https://www.nba.com/stats"

header = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}

page = requests.get(URL, headers=header)

soup = BeautifulSoup(page.text, "html.parser")

# array of each statistical category's leaderboards, leaderboards[0] = points leaders, etc.
# only looking at index 1-9, beyond that is team stats not individual players
leaderboards = soup.find_all("div", {"class": "LeaderBoardCard_lbcWrapper__e4bCZ LeaderBoardWithButtons_lbwbCardGrid__Iqg6m LeaderBoardCard_leaderBoardCategory__vWRuZ"})[0:9]

# dict of all statistical category, and their corresponding table containing player information
categories = {}


# add category title and table corresponding to that category in the tables above
for div in leaderboards:
        print(div.findChildren()[0].text)
        categories[div.findChildren()[0].text] = div.findChildren()[2].tbody.contents
        # print(div.findChildren()[2].tbody.contents)
        #tables.append(div.findChildren()[2].tbody.contents)
        # print()

print()
print()

user_input = string.capwords(input("Enter Category: "))
while user_input in categories:
    for i in range(0, 5):
        print(str(i + 1) + '. ' + categories[user_input][i].a.text + ' ' + categories[user_input][i].td.next_sibling.next_sibling.text)
    print()
    user_input = string.capwords(input("Enter Category: "))