
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

FACTOR_MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    output_km = StringProperty("Result will appear here")

    def build(self):
        self.title = "Miles to Kilometres"
        return Builder.load_file("convert_miles_km.kv")

    def handle_calculate(self, text):
        """Convert miles to kilometers."""
        miles = self.convert_to_number(text)
        self.output_km = f"{miles * FACTOR_MILES_TO_KM:.2f} km" if miles != 0 else "Invalid input"

    def handle_increment(self, text, change):
        """Adjust miles value and recalculate."""
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(max(0, miles))  # Avoid negative values

    @staticmethod
    def convert_to_number(text):
        """Convert text input to float; return 0.0 if invalid."""
        try:
            return float(text.strip())
        except ValueError:
            return 0.0


MilesConverterApp().run()
