import requests
import mapper
from bs4 import BeautifulSoup

selection = "ATE"

def handle_content(ctx):
	soup = BeautifulSoup(ctx, 'html.parser')

	# targets = soup.prettify()
	fleets = soup.find_all(href=mapper.regex["fleet"])
	plates = soup.find_all(string=mapper.regex["plate"])

	# print(targets)
	for fleet in fleets:
		print(f'{fleet.get_text()}')
	for plate in plates:
		print(f'{plate.get_text()}')



headers = {'Cookie': 'l=0; hints=1; vid=8351569'}
response = requests.get(f'http://1005.idv.hk/index.php?page=11&p={mapper.type[selection]}', headers=headers)


# Check redirect
if response.history:
	print("Request was redirected")
	for resp in response.history:
		print(resp.status_code, resp.url)
	print ("Final Destination:", response.status_code, response.url)
	

# Process HTML content
if response.ok:
	handle_content(response.content)
else:
  print(response.status_code + " " + response.text)