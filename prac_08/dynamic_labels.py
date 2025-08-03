from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """An app that dynamically creates Labels for each name in a list."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # This is your data model — just a list of names
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]


    def build(self):
        """Build the Kivy GUI and dynamically create Label widgets."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Dynamically create and add Label widgets to the GUI."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabelsApp().run()
