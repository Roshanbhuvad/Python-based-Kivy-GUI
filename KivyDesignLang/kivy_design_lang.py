import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
	name = ObjectProperty(None)  #We are setting this (None) blank bcoz we are initially created this class when we build it there will be no actual object property until it read the KV file, We have to initialize it as none to start and then it will be given a value
	email = ObjectProperty(None) #Please note that these name & email name needs to be the same as mentioned in my.kv file as a global variable bcoz we have to sync up these to with my.kv file global varibles , here this are class variables

	def btn(self):
		print("Name:", self.name.text, "email", self.email.text) # This is require to get the data when submit button pressed why we used self here bcoz we are referencing the variables from the class MyGrid(Widget), We referencing thE class variable(MyGrid) here by using the self attribute
		self.name.text = ""
		self.email.text = ""  #these two lines for clearning GUI user Data to get the new information from the next user


class MyApp(App):

    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()
