from kivy.app import App
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget

Config.set("graphics", "resizeble", 0)
Config.set("graphics", "width", 400)
Config.set("graphics", "height", 600)

class CalculatorApp(App):
    def update_label(self):
        self.lbl.text=self.formula

    def add_number(self,instance):
        if(self.formula=="0"):
            self.formula = ""
        
        self.formula += str(instance.text)
        self.update_label()


    def add_operation(self, instance):
        if (str(instance.text).lower() == "x"):
            self.formula += "*" 
        elif (str(instance.text) == "÷"):
            self.formula += "/" 
        elif (str(instance.text)=="C"):
            self.formula = "0"
        elif (str(instance.text)=="<--"):
            self.formula = self.formula[:-1]
        elif (str(instance.text)=="-->"):
            self.formula = self.formula[1:]
        else:
            self.formula += str(instance.text)
        self.update_label()


    def calculator_result(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = "0"


    def build(self):
        self.formula="0"
        bl = BoxLayout(orientation="vertical", padding = 25)
        gl = GridLayout(cols = 4, spacing = 3, size_hint = (1, .6))

        self.lbl = Label(text="0", font_size = 40 , halign = "right", valign = "center", size_hint = (1, .6), text_size=(400-50,600 * .4-50))
        bl.add_widget(self.lbl)
        
        
        gl.add_widget(Button(text="-->", font_size=50, on_press = self.add_operation))
        gl.add_widget(Button(text="C", font_size=50, on_press = self.add_operation))
        gl.add_widget(Button(text="<--", font_size=50, on_press = self.add_operation))
        gl.add_widget(Button(text="÷", font_size=50, on_press = self.add_operation))

        gl.add_widget(Button(text="7", font_size=50, on_press = self.add_number))
        gl.add_widget(Button(text="8", font_size=50, on_press = self.add_number))
        gl.add_widget(Button(text="9", font_size=50, on_press = self.add_number))
        gl.add_widget(Button(text="X", font_size=50, on_press = self.add_operation))

        gl.add_widget(Button(text="4", font_size=50, on_press = self.add_number))
        gl.add_widget(Button(text="5", font_size=50, on_press = self.add_number))
        gl.add_widget(Button(text="6", font_size=50, on_press = self.add_number))
        gl.add_widget(Button(text="-", font_size=50, on_press = self.add_operation))

        gl.add_widget(Button(text="1", font_size=50, on_press = self.add_number))
        gl.add_widget(Button(text="2", font_size=50, on_press = self.add_number))
        gl.add_widget(Button(text="3", font_size=50, on_press = self.add_number))
        gl.add_widget(Button(text="+", font_size=50, on_press = self.add_operation))

        gl.add_widget(Widget())
        gl.add_widget(Button(text="0", font_size=50, on_press = self.add_number))
        gl.add_widget(Button(text=".", font_size=50, on_press = self.add_number))
        gl.add_widget(Button(text="=", font_size=50, on_press = self.calculator_result))#background_color=[0, 55, 100, 1] для цвета кнопок
        
        bl.add_widget(gl)
        return(bl)



if __name__ == "__main__":
    CalculatorApp().run()
