from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image

class MainApp(App):
	def build(self):
		#label = Label(text = 'Hello from Kivy',
		image = Image(source='index.jpeg', 
					size_hint = (.5,.5), 
					pos_hint = {'center_x':.5, 'center_y':.5})

		#return label
		return image


if __name__ == '__main__':
	app = MainApp()
	app.run()		

