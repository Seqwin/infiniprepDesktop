from kivy.app import App
from kivy.lang import Builder
from kivy.uix.behaviors import DragBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window

kv = """
BoxLayout:
    orientation: 'horizontal'
    FunctionList:
        id: function_list
        size_hint_x: 0.5
    ProtocolContainer:
        id: protocol_container
        size_hint_x: 0.5

<DraggableFunction>:
    size_hint: None, None
    size: 120, 40
    drag_rectangle: self.x, self.y, self.width, self.height
    drag_timeout: 10000000
    drag_distance: 0

<FunctionList>:
    orientation: 'vertical'

<ProtocolContainer>:
    orientation: 'vertical'
"""

class DraggableFunction(DragBehavior, Label):
    def __init__(self, **kwargs):
        super(DraggableFunction, self).__init__(**kwargs)
        self.original_pos = self.pos

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.original_pos = self.parent.to_widget(*self.center)
        return super(DraggableFunction, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            return super(DraggableFunction, self).on_touch_move(touch)
        return False

    def on_touch_up(self, touch):
        container = App.get_running_app().root.ids.protocol_container
        if self.collide_point(*touch.pos) and container.collide_point(*touch.pos):
            App.get_running_app().add_to_protocol(self.text)
            self.parent.remove_widget(self)
            container.add_widget(Label(text=self.text, size_hint_y=None, height=40))
        else:
            self.pos = self.original_pos
        return super(DraggableFunction, self).on_touch_up(touch)

class FunctionList(BoxLayout):
    pass

class ProtocolContainer(BoxLayout):
    pass

class DragDropLiquidHandlingApp(App):
    def build(self):
        self.protocol = {}
        return Builder.load_string(kv)

    def on_start(self):
        functions = ['Pipetting', 'Mixing', 'Diluting', 'Centrifuging', 'Heating']
        for func in functions:
            self.root.ids.function_list.add_widget(DraggableFunction(text=func))

    def add_to_protocol(self, function_name):
        if function_name not in self.protocol:
            self.protocol[function_name] = {"steps": []}
            print(f"Updated protocol: {self.protocol}")

if __name__ == '__main__':
    DragDropLiquidHandlingApp().run()
