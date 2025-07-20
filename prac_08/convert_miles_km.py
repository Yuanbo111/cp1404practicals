from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

CONVERSION_FACTOR = 1.60934

class MilesConverterApp(App):
    """Application class for the Miles to Kilometres converter"""
    output_km = StringProperty("0.0")

    def build(self):
        """Set up the GUI from the KV file."""
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        """Convert miles to km and update the label."""
        try:
            miles = float(self.root.ids.input_miles.text)
            km = miles * CONVERSION_FACTOR
            self.output_km = f"{km:.3f}"
        except ValueError:
            self.output_km = "0.0"

    def handle_up(self):
        """Increase miles by 1 and update conversion."""
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0
        miles += 1
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()

    def handle_down(self):
        """Decrease miles by 1 and update conversion."""
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0
        miles -= 1
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()



MilesConverterApp().run()
