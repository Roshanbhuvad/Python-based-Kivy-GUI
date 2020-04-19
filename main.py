import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)  #super(MyGrid, self).__init__(**kwargs) just calling the grid layouts constructor giving it a few parameters
		self.cols = 1 #this our main grid(layout) for submit button that is why we set columns in only 1

		self.inside = GridLayout() # This is our new grid (or main grid or parent grid ) layout for seperating email,name girds from submit buttons
		self.inside.cols = 2

# previous syntax was self.add_widget() but now we have changed to self.inside.add_widget() bcoz we have to add this all grids(name, emails) in inside grid becoz we have to separating the 2 grid layouts one for email,name and second for submit button.that is why we have adding all this in main grid(self.inside)
		#self.cols = 2 # We are change property that is belongs to grid layout, self.cols = 2 means amount of colums equal to 2  
		self.inside.add_widget(Label(text="First Name: ")) # this will add the widgets method on GUI bcoz that is a part of GridLayout Class  
		self.firstName = TextInput(multiline=False)
		self.inside.add_widget(self.firstName)


		self.inside.add_widget(Label(text="Last Name: ")) # this will add the widgets method on GUI bcoz that is a part of GridLayout Class  
		self.lastName = TextInput(multiline=False)
		self.inside.add_widget(self.lastName)


		self.inside.add_widget(Label(text="Email ID: ")) # this will add the widgets method on GUI bcoz that is a part of GridLayout Class  
		self.email = TextInput(multiline=False)
		self.inside.add_widget(self.email)


		self.add_widget(self.inside) #this is class for declaring the inside for calling emails, name layout

		self.submit = Button(text="Submit", font_size=40)
		self.submit.bind(on_press=self.pressed) #self.pressed is amethod, We are calling pressed function when submit button is being pressed
		self.add_widget(self.submit)
	

	def pressed(self, instance):
		#print("pressed") # This will printed on console, not on GUI
		name = self.firstName.text
		last = self.lastName.text
		email = self.email.text

		print("Name:", name, "Last Name:", last, "email:", email) #This will display in console not in GUI windows
		self.firstName.text = ""
		self.lastName.text = ""
		self.email.text = ""  # In this three syntax we have clear the name, last name , email layout contain once you clicked submit button  

class MyApp(App):
	def build(self):
		return MyGrid()


if __name__ == "__main__":
	MyApp().run()

