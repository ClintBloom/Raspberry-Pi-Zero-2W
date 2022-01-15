import requests
from bs4 import BeautifulSoup

# Tags for website
# PiShop
tag_pishop_login = 'login_email'
tag_pishop_pass = 'login_pass'

# Post credentials
# PiShop
post_pishop_url = 'https://www.pishop.us/login.php?action=check_login'
request_pishop_url = 'https://www.pishop.us/product/raspberry-pi-zero-2-w/'

# Login Info
# PiShop
pishop_payload = {
    'login_email': '<Your email>',
    'login_pass': '<Your email>'
}


session = requests.session()
post = session.post(post_pishop_url, data=pishop_payload)
response = session.get(request_pishop_url)
soup = BeautifulSoup(response.content, 'html.parser')
check_button = soup.find('input', id="form-action-addToCart")
button_value = check_button.attrs['value']

if 'Out of stock' in button_value:
    print('Out Of Stock')
else:
    print('In stock')
