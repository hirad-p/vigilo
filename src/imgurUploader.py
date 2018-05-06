import requests
import base64
from imgurpython import ImgurClient

def uploadImage(imgPath):
	"""takes in an image path and returns the imgur URL """
	config = get_config()
	config.read('credentials.ini')
	client_id = config.get('Imgur', 'CLIENT_ID')
	client_secret = config.get('Imgur', 'CLIENT_SECRET')
	access_token = config.get('Imgur', 'ACCESS_TOKEN')
	refresh_token = config.get('Imgur', 'REFRESH_TOKEN')
	client = ImgurClient(client_id, client_secret, 
						 access_token=access_token,
						 refresh_token=refresh_token)
	config = {
		'album': None,
		'name':  'Intruder!',
		'title': 'Intruder!',
		'description': 'possible Intruder'
	}	
	image = client.upload_from_path(imgPath, config=config, anon=True)
	return image['link']

def get_config():
	''' Create a config parser for reading INI files '''
	try:
		import ConfigParser
		return ConfigParser.ConfigParser()
	except:
		import configparser
		return configparser.ConfigParser()
if __name__ == '__main__':
	print(uploadImage("/Users/Nicholas/Desktop/Naruto.png"))