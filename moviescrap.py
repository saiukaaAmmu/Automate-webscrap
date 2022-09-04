from bs4 import BeautifulSoup
import requests,openpyxl
#from openpyxl_image_loader import SheetImageLoader

excel=openpyxl.Workbook()
sheet=excel.active
#img_loader=SheetImageLoader(sheet)
sheet.title="Movie List"
sheet.append(['Rank','Movie Name','year Of Release','IMDB rating'])

try:
    response=requests.get("https://www.imdb.com/chart/top/")
    soup=BeautifulSoup(response.text,'html.parser')
    #print(soup)
    movies=soup.find('tbody',class_="lister-list").find_all("tr")
    for movie in movies:
        #print(movie)
        #img_url=movie.find_element('By_XPATH,//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[1]/td[1]/a')
        rank=movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
        movie_name=movie.find('td',class_="titleColumn").a.text
        rate=movie.find('td',class_="ratingColumn").strong.text
        year=movie.find('td',class_="titleColumn").span.text.replace('(',"")
        year=year.replace(')',"")
        #print(rank,movie_name,year,rate)
        sheet.append([rank,movie_name,year,rate])
    print("successfully scraped")

except Exception as e:
    print(e)

excel.save("Movies.xlsx")
