from kivy.app import App
from kivy.lang import Builder


kv= '''
FloatLayout:
	Button:
		text: 'Hello World'
		size_hint: None, None
		pos_hint: {'center_x': .5, 'center_y': .5}
		canvas.before:
			Rotate:
				angle: 180
				origin: self.center


'''

class rotate(App):
	def build(self):
		return Builder.load_string(kv)

rotate().run()
