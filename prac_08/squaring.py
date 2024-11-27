
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):
    def build(self):
        Window.size = (400, 200)
        self.title = "Number Squaring"
        return Builder.load_file("squaring.kv")

    def handle_calculate(self, value):
        """Calculate the square of the input value."""
        try:
            number = float(value.strip())
            self.root.ids.output_label.text = f"Square: {number ** 2}"
        except ValueError:
            self.root.ids.output_label.text = "Invalid input. Enter a valid number."


SquareNumberApp().run()
