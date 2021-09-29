from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class WidgetsExample(BoxLayout):
    times = StringProperty("0")
    count = 0
    name = ''

    def plus(self):
        self.count += 1
        self.times = str(self.count)

    def minus(self):
        self.count -= 1
        self.times = str(self.count)

    # def press(self,instance):
    #     name = self.name.text
    #     self.add_widget(Label(text=name,pos_hint={"center_x": .5,"center_y": .95}))
    #     self.name.text = ''
    #     self.submit.clear_widgets()
    #
    # def change_name(self):
    #     self.name = TextInput(multiline=False)
    #     self.add_widget(self.name)
    #     self.submit = Button(text='Submit',font_size=32)
    #     self.submit.bind(on_press=self.press)
    #     self.add_widget(self.submit)
    #     self.submit.clear_widgets()

class CounterApp(App):
    pass


CounterApp().run()