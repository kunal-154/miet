import pyttsx3
for num in range(0,pages):
page = pdfreader.getPage(num)
text = page.extractText()
player = pyttsx3.init()
player.say(text)
player.runAndWait()