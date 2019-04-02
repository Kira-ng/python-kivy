from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 330)
Config.set('graphics', 'height', 450)

class CalcApp(App):
	title = 'Calculator'
	def update_label(self):
		self.lbl.text = self.formula

	def add_number(self, instance):
		if(self.formula == "0"):
			self.formula = ""
		self.formula += str(instance.text)
		self.update_label()

	def add_operation(self, instance):
		if(str(instance.text).lower() == "x"):
			self.formula += "*"
		else:
			self.formula += str(instance.text)
		self.update_label()

	def cancel(self, instance):
		self.lbl.text = self.lbl.text[:-1]
		self.formula = self.formula[:-1]

	def calc_result(self, instance):
		try:
			self.lbl.text = str(eval(self.lbl.text))
		except SyntaxError:
			self.lbl.text = "Error"
		except ZeroDivisionError:
			self.lbl.text = "Error"
		self.formula = ""

	def build(self):
		self.formula = "0"
		bl = BoxLayout(orientation = 'vertical', padding = 6)
		gl = GridLayout(cols = 5, spacing = 4, size_hint = [1, 0.65])
		self.lbl = Label(text = "Write your instance", font_size = 32, halign = 'right', size_hint = [1, .35], text_size = [330 - 12, 450 * .35 - 12], valign = "center")
		bl.add_widget(self.lbl)
		gl.add_widget(Button(text = "7", on_press = self.add_number))
		gl.add_widget(Button(text = "8", on_press = self.add_number))
		gl.add_widget(Button(text = "9", on_press = self.add_number))
		gl.add_widget(Button(text = "X", on_press = self.add_operation))
		gl.add_widget(Button(text = "C", on_press = self.cancel))
		gl.add_widget(Button(text = "4", on_press = self.add_number))
		gl.add_widget(Button(text = "5", on_press = self.add_number))
		gl.add_widget(Button(text = "6", on_press = self.add_number))
		gl.add_widget(Button(text = "-", on_press = self.add_operation))
		gl.add_widget(Button(text = "(", on_press = self.add_operation))
		gl.add_widget(Button(text = "1", on_press = self.add_number))
		gl.add_widget(Button(text = "2", on_press = self.add_number))
		gl.add_widget(Button(text = "3", on_press = self.add_number))
		gl.add_widget(Button(text = "+", on_press = self.add_operation))
		gl.add_widget(Button(text = ")", on_press = self.add_operation))
		gl.add_widget(Button(text = "/", on_press = self.add_operation))
		gl.add_widget(Button(text = "0", on_press = self.add_number))
		gl.add_widget(Button(text = ".", on_press = self.add_number))
		gl.add_widget(Button(text = "=", on_press = self.calc_result))
		gl.add_widget(Button(text = "%", on_press = self.add_operation))
		bl.add_widget(gl)
		return bl

if __name__ == "__main__":
	CalcApp().run()