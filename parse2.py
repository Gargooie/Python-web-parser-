import requests
from bs4 import BeautifulSoup as BS

s = requests.Session()
#get csrf
auth_html = s.get('https://smartprogress.do/')
auth_bs = BS(auth_html.content, 'html.parser')
csrf = auth_bs.select('input[name=YII_CSRF_TOKEN]')[0]['value']


#do login
payload = {
#post data
'YII_CSRF_TOKEN': csrf,
'returnUrl': '/',
'UserLoginForm[email]': 'ibanezed123@gmail.com',
'UserLoginForm[password]': 'test',
'UserLoginForm[rememberMe]': 1
}

answ = s.post('https://smartprogress.do/user/login/',data=payload)
anw_bs = BS(answ.content, 'html.parser')

#print(anw_bs)
print( 'Имя: ' + anw_bs.select('.user-menu__name')[0].text.strip() )
print('Уровень ' + anw_bs.select('.user-menu__info-text--lvl')[0].text.strip())
print('Опыт ' + anw_bs.select('.user-menu__info-text--exp')[0].text.strip())

#.user-menu__

#<input type="hidden" value="d795a576bf7cc57fb59e9abe7c01b019855b47ae" name="YII_CSRF_TOKEN"> #current token
