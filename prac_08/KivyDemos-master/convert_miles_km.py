from kivy.app import App
from kivy.lang import Builder

# Conversion factor from miles to kilometers
CONVERSION_FACTOR = 1.60934



class ConvertMilesKmApp(App):
    def build(self):
        self.title = "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root
    def handle_increment(self, value):
        try:
            miles = float(value)
        except ValueError:
            miles = 0.0

        miles += value
        self.root.ids.input_label.text = str(miles)

    def handle_decrement(self, value):
        try:
            miles = float(value)
        except ValueError:
            miles = 0.0

        miles += value
        self.root.ids.input_label.text = str(miles)


    def calculate_conversion(self,value):
        try:
            miles = float(value)
        except ValueError:
            miles = 0.0

        kilometers = miles * CONVERSION_FACTOR
        self.root.ids.output_label.text = f'{kilometers:.2f}'

ConvertMilesKmApp().run()
