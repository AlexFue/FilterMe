import speech_recognition as sr

class Speech:
	def audio(self):
		r = sr.Recognizer()
		text = ""
		with sr.Microphone() as source:
			print("Say something")
			audio = r.listen(source)

			try: 
				text = r.recognize_google(audio)
				print('You said: {}'.format(text))
				
			except:
				print('Sorry, could not understand')

		return text