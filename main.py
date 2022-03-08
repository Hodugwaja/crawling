import urllib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import platform
from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.request import urlopen

path = "C:\Windows\Fonts/malgun.ttf"
from matplotlib import font_manager, rc


if platform.system() == "DarWin": #운영체제가 Mac이라면 애플고딕으로 폰트 설정 - Mac OS의 코어가 DarWin OS이기 때문
    rc('font', family="AppleGothic")
elif platform.system() == "Windows": #운영체제가 Windows라면 막은 고딕
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print("해당 운영체제는 지원하지 않습니다")

url_base = "https://movie.naver.com/"
url_syb = "movie/sdb/rank/rmovie.naver?sel=cur&date=20220306"

page = urlopen(url_base + url_syb)

soup = BeautifulSoup(page, "html.parser")



# 해당 시점에서 가장 평점이 높은 영화
print(soup.find_all('div', 'tit5')[0].a.string)

# 해당 시점에서 가장 평점이 높은 점수
print(soup.find_all('td', 'point')[0].string)

date = pd.date_range('2022-1-1', periods=65, freq='D')


movie_date = []
movie_name = []
movie_point = []

for today in tqdm(date):
    html = "https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date={date}"
    response = urlopen(html.format(date=urllib.parse.quote(today.strftime('%Y%m%d'))))
    soup = BeautifulSoup(response, "html.parser")
    end = len(soup.find_all('td', 'point'))

    movie_date.extend([today for n in range(0, end)])
    movie_name.extend([soup.find_all('div', 'tit5')[n].a.string for n in range(0, end)])
    movie_point.extend([soup.find_all('td', 'point')[n].string for n in range(0, end)])

movie = pd.DataFrame({'date': movie_date, 'name': movie_name, 'point': movie_point})
movie['point'] = movie['point'].astype(float)
movie.head()

movie_unique = pd.pivot_table(movie, index=['name'], aggfunc=np.sum)
movie_best = movie_unique.sort_values(by='point', ascending=False)
movie_best.head()

tmp = movie.query('name == ["언차티드"]')
print(tmp)

#plt.figure(figsize=(12, 8))
#plt.plot(tmp['date'], tmp['point'])
#plt.grid()
#plt.show()

movie_pivot = pd.pivot_table(movie, index=["date"], columns=['name'], values=['point'])
movie_pivot.head()

movie_pivot.columns = movie_pivot.columns.droplevel()

print(movie_pivot.head())

# movie_pivot.plot(y=['언차티드', '스파이더맨 노 웨이 홈', '이상한 나라의 수학자', '특송', '킹메이커'], figsize=(12, 6))
# plt.legend(loc='best')
# plt.grid()
# plt.show()
