# -*- coding: utf-8 -*-

from kivy.lang import Builder
from kivy.uix.modalview import ModalView
from kivy.uix.floatlayout import FloatLayout
from kivymd.theming import ThemableBehavior
from kivymd.elevationbehavior import ElevationBehavior
from kivy.properties import ObjectProperty, ListProperty

Builder.load_string("""
#:import MDFlatButton kivymd.button.MDFlatButton
#:import CircularTimePicker kivymd.MDTimePicker.circularTimePicker
#:import dp kivy.metrics.dp
<MDTimePicker>:
    size_hint: (None, None)
    size: dp(270), dp(335)+dp(95)
    pos_hint: {'center_x': .5, 'center_y': .5}
    canvas:
        Color:
            rgba: 1, 0, 0, 0.3
        Rectangle:
            size: root.size
            pos: root.pos
        Color:
            rgba: self.theme_cls.bg_dark
        Rectangle:
            size: dp(270), dp(335)
            pos: root.pos[0], root.pos[1] + root.height - dp(335) - dp(95)
        Color:
            rgba: self.theme_cls.primary_color
        Rectangle:
            size: dp(270), dp(95)
            pos: root.pos[0], root.pos[1] + root.height - dp(95)
        Color:
            rgba: self.theme_cls.bg_light
        Ellipse:
            size: dp(220), dp(220)
            pos: root.pos[0]+dp(270)/2-dp(220)/2, root.pos[1] + root.height - (dp(335)/2+dp(95)) - dp(220)/2 + dp(35)
        #Color:
            #rgba: (1, 0, 0, 1)
        #Line:
            #width: 4
            #points: dp(270)/2, root.height, dp(270)/2, 0
    CircularTimePicker:
        id: time_picker
        pos: (dp(270)/2)-(self.width/2), root.height-self.height
        size_hint: .8, .8
        pos_hint: {'center_x': 0.5, 'center_y': 0.585}
    MDFlatButton:
        pos: root.pos[0]+root.size[0]-dp(72)*2, root.pos[1] + dp(10)
        text: "Cancel"
        on_release: root.close_cancel()
    MDFlatButton:
        pos: root.pos[0]+root.size[0]-dp(72), root.pos[1] + dp(10)
        text: "OK"
        on_release: root.close_ok()
""")


class MDTimePicker(ThemableBehavior, FloatLayout, ModalView, ElevationBehavior):
    background_color = ListProperty((0, 0, 0, 0.4))
    time = ObjectProperty()

    def __init__(self, **kwargs):
        super(MDTimePicker, self).__init__(**kwargs)
        self.current_time = self.ids.time_picker.time

    def set_time(self, time):
        try:
            self.ids.time_picker.set_time(time)
        except AttributeError:
            raise TypeError("MDTimePicker._set_time must receive a datetime object, not a \"" +
                            type(time).__name__ + "\"")

    def close_cancel(self):
        self.dismiss()

    def close_ok(self):
        self.current_time = self.ids.time_picker.time
        self.time = self.current_time
        self.dismiss()
