"""The ScrollView in Kivy provides a scrollable view. Using scrollview, we can scroll through x axis as well as y axis on the screen.

First, we will import a new function called runTouchApp(). This function will make our scrollview touch enabled."""\

from kivy.base import runTouchApp

from kivy.lang import Builder

root = Builder.load_string(r'''

ScrollView:

    Label:
    
        text: 'Scrollview Example' * 100
        
        font_size: 30
        
        size_hint_x: 1.0
        
        size_hint_y: None
        
        text_size: self.width, None
        
        height: self.texture_size[1]
        
''')

runTouchApp(root)