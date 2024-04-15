from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

NEW_COLOUR = (1, 0, 1, 1)  # RGBA for red

class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names: phone numbers
        self.name_to_phone = ['Bob', 'Brian', 'Betty', 'Billy']

    def build(self):
        """The Kivy GUI."""
        self.title = "Dynamic labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root
    
    def create_labels(self):
        """Create buttons from data and add them to the GUI."""
        for name in self.name_to_phone:
            # create a label for each data entry, specifying the text
            temp_label = Label(text=name)

            # set the label's background colour
            temp_label.color = NEW_COLOUR
            # add the button to the "entries_box" layout widget
            self.root.ids.main.add_widget(temp_label)
            
DynamicLabelsApp().run()
