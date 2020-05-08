from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

#html = urlopen("http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf") # 교보문고 베스트셀러
novelBest_html = urlopen("http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?mallGb=KOR&linkClass=B&range=1&kind=0&orderClick=DAb")

bsObject = bs(novelBest_html, "html.parser") 
week_standard = bsObject.find('h4', {'class':'title_best_basic'}).find('small').text
bestseller_contents = bsObject.find('ul', {'class':'list_type01'})
bestseller_list = bestseller_contents.findAll('div', {'class':'detail'})

title_list = [b.find('div', {'class': 'title'}).find('strong').text for b in bestseller_list]
book_img_src = [t.find('img')['src'] for t in bestseller_contents.findAll('div', {'class': 'cover'})]
subtitle_list = [b.find('div', {'class': 'subtitle'}).text.strip() for b in bestseller_list]

# print("\n"+week_standard+"\n\n")
# for i in range(len(title_list)):
#     print("Title: "+title_list[i])
#     print("Description: "+subtitle_list[i]+"\n")

print(book_img_src[0])
