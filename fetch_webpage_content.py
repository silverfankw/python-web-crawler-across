import requests
import mapper
from bs4 import BeautifulSoup

# PlateNumber  re.compile("^(([A-Z][A-Z]) ?(\d{3,4}))")

def handle_content(ctx):
	soup = BeautifulSoup(ctx, 'html.parser')

	# Plate Number filter
	targets = soup.find_all(string=mapper.regex["plate"])

	# print(targets)
	for target in targets:
		print(target[:7])

headers = {'Cookie': 'l=0; hints=1; vid=8351569'}
response = requests.get(f'http://1005.idv.hk/index.php?page=11&p={mapper.type["E6X"]}', headers=headers)


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