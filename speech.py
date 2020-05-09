import speech_recognition as sr

class Speech:
	def audio(self):
		r = sr.Recognizer()
		text = ""
		with sr.Microphone() as source:
			# Displays to the console when it begins listening
			print("Say something")
			# Here it is taking in what is being said
			audio = r.listen(source)

			try: 
				# This line is google interepreting what was said
				text = r.recognize_google(audio)
				# Prints what it belives you said.
				print('You said: {}'.format(text))
				
			except:
				# If you were not clear, this message would be prompted
				print('Sorry, could not understand')

		return text.lower()