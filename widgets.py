from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):
	
	def __init__(self, **kwargs):

		super(LoginScreen, self).__init__(**kwargs)  # We use super to avoid needing to refer to the base class(Not refer only GridLayout class), as well as utilize multi inheritance
		self.cols = 2
		self.add_widget(Label(text="Username:"))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)

		self.add_widget(Label(text="Password:"))
		self.password = TextInput(multiline=False, password=True) #password =True parameter helps to make password asterisk form link ***** when you enter in password section  
		self.add_widget(self.password)


class SimpleKivy(App):
	def build(self):
		return LoginScreen()
		
if __name__ == "__main__":
	SimpleKivy().run()
