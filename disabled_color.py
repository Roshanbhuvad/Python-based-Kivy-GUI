from kivy.app import App
from kivy.lang import Builder

kv = """
<Lab@Label>:
	size_hint_y: None
	height: dp(200)
	font_size: dp(80)
	text: 'Roshan Bhuvad'
	color: 0.4, 0.4, 0.5, 1
	disabled_color: self.color
	disabled : True

BoxLayout:
	orientation: 'vertical'
	Lab:
		markup: True
	Lab:
		markup: False
"""
class TextApp(App):
	def build(self):
		return Builder.load_string(kv)
TextApp().run()
#if __name__ == '__main__':
	
