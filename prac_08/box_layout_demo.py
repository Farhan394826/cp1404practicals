
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Interactive Box Layout"
        return Builder.load_file("box_layout.kv")

    def handle_greet(self):
        """Display a greeting message based on user input."""
        name = self.root.ids.input_name.text.strip()
        self.root.ids.output_label.text = f"Hello, {name}!" if name else "Please enter your name."

    def handle_clear(self):
        """Clear the input and reset the greeting message."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = "Cleared!"


BoxLayoutDemo().run()
