import json,requests,os,time
from bs4 import BeautifulSoup as parse
import requests as r

def info():
	user = input('[?] username: ')
	req = requests.get('https://instagram.com/'+user+'/?__a=1')
	js = req.json()['graphql']['user']['full_name']
	jss = req.json()['graphql']['user']['edge_followed_by']['count']
	jsss = req.json()['graphql']['user']['edge_follow']['count']
	print ('[+] username  : '+user)
	print ('[+] Name      :', js)
	print ('[+] Follower  :', jss)
	print ('[+] Following :', jsss)
	print()
	t = input('[?] back to menu (y/n): ')
	if t == 'y' or t  == 'Y':
		menu()
	elif t == 'n' or t == 'n':
		exit()
	else:
		print('salah tolol')
		info()
def instagram():
	url = input('\n[?] URL : ')
	ct = input('[?] Download? (y/n): ')
	if 'y' in ct:
		bra = input('[?] File Name: ')
		print('[!] Loading...')
		save = r.get(url).text
		soup = parse(save, 'html.parser')
		love = soup.findAll('script', type='text/javascript')
		for heart in love:
			if 'window._sharedData = ' in heart.text:
				jonson = heart.text.replace('window._sharedData = ','').replace(';','')
		jonson = json.loads(jonson)
		jonson = jonson["entry_data"]['PostPage'][0]["graphql"]['shortcode_media']["video_url"]
		time.sleep(5)
		alukar = r.get(jonson)
		pants = open(bra, 'wb')
		pants.write(alukar.content)
		pants.close
		print('[!] \x1b[32;1mDownload Succesfully\x1b[37;1m')
		time.sleep(2)
		os.system('cp '+bra+' /sdcard && rm -rf '+bra)
	exit()
def menu():
	os.system('clear')
	print("""
[ Instagram Toolkit ] coded by fajar
-----------------v2.0 ig: fajarid05_

[ Menu ]
1.instagram info
2.instagram vid-dl

	""")
	tanya = input('[?]__> ')
	if tanya == '1' or tanya == '02':
		info()
	elif tanya == '02' or tanya == '2':
		instagram()
	else:
		print('[!] Salah Tolol')
		time.sleep(2)
		return menu()
menu()