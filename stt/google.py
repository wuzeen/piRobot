import requests
import json

class google:

	def __init__(self,audio):
		self.audio=audio

	def sst_google(self):
		lang_code='zh-CN'
		
		google_speech_url = 'https://www.google.com.ua/speech-api/v1/recognize?xjerr=1&client=chromium&pfilter=2&lang=%s&maxresults=6'%(lang_code)
		
		hrs = {"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7",'Content-type': 'audio/L16; rate=16000'}
		
		recording_flac_data = open(self.audio.savepath, 'rb').read()

		r = requests.post(google_speech_url, data=recording_flac_data, headers=hrs)
        # grab the response
		response = r.text

		print response

		return json.loads(response)['hypotheses'][0]['utterance']
