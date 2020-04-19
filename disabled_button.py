from kivy.uix.button import Button
from kivy.app import App 
from functools import partial #we have imported partial function from the functools so that we can use the bind() function.

class kivyButton(App):
	def disable(self, instance, *args):

		instance.disabled = True

	def update(self, instance, *args):
		instance.text = "I am disabled!"

	def build(self):
		mybtn = Button(text="click me to disable")
		mybtn.bind(on_press=partial(self.disable, mybtn))

		mybtn.bind(on_press=partial(self.update, mybtn))

		return mybtn

kivyButton().run()