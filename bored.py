from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.network.urlrequest import UrlRequest
from kivy.core.window import Window
Window.size = (450,850)

screen_manager = """
ScreenManager:
    FirstScreen:
    SecondScreen:


<FirstScreen>
    name : "first"
    canvas.before:
        Color :
            rgba : (1,3,5,6)

    MDLabel:
        text : "Welcome!"
        pos_hint : {"cebter_x": 0.5, "center_y" : 0.8}
        halign : "center"
        font_style: "H5"

    MDLabel:
        text : "Change your bore time into something special"
        pos_hint : {"center_x" : 0.5, "center_y" : 0.7}
        halign : "center"

    MDRaisedButton:
        text : "Start"
        pos_hint : {"center_x" : 0.5, "center_y" : 0.3}
        halign : "center"
        font_style : "Button"
        on_press : root.manager.current = "second"

<SecondScreen>
    name : "second"
    MDLabel:
        text : "You wil not be bored anymore!"
        pos_hint : {"center_x": 0.5, "center_y" : 0.9}
        halign : "center"
        font_style : "H6"
    MDLabel:
        id : popuptext
        text : ""
        pos_hint : {"center_x" : 0.5, "center_y" : 0.8}
        halign : "center"
        font_style : "Body1"
    MDLabel:
        id : boredans
        text : ""
        pos_hint : {"center_x" : 0.5, "center_y" : 0.7}
        halign : "center"
        font_style : "Body1"
    MDLabel:
        id : boredtype
        text : ""
        pos_hint : {"center_x" : 0.5, "center_y" : 0.6}
        halign : "center"
        font_style : "Body1"
    MDLabel:
        id : participants
        text : ""
        pos_hint : {"center_x" : 0.5, "center_y" : 0.5}
        halign : "center"
        font_style : "Body1"
    MDRaisedButton:
        text : "Get Thrilled"
        pos_hint : {"center_x" : 0.5, "center_y" : 0.1}
        halign : "center"
        font_style : "Button"
        on_press : app.action()
"""

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

screen = ScreenManager()
screen.add_widget(FirstScreen(name = "first"))
screen.add_widget(SecondScreen(name = "second"))

class Bored(MDApp):
    def build(self):
        self.strng = Builder.load_string(screen_manager)
        return self.strng

    def action(self):
        url = f'https://www.boredapi.com/api/activity/'
        self.request = UrlRequest(url = url, on_success = self.res)

    def res(self, *args):
        self.data = self.request.result
        ans = self.data
        result = ans['activity']
        type = ans['type']
        participants = ans['participants']
        print(result)
        print(ans)
        try:
            self.strng.get_screen("second").ids.popuptext.text = "Here is something to keep you busy and your day/night interesting"
            self.strng.get_screen("second").ids.boredans.text = f'Task : {result}'
            self.strng.get_screen("second").ids.boredtype.text = f'Type : {type}'
            self.strng.get_screen("second").ids.participants.text = f'Participants: {participants}'
        except:
            self.strng.get_screen("second").ids.boredans.text = "Please Connect to Internet!"


if __name__ == "__main__":
    Bored().run()
