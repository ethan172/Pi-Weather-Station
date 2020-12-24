"""
Author: Ethan Rockaway
"""


from guizero import App, Text, PushButton
app = App(title="testyTest")
intro = Text(app, text="flaggyFlag :D")
ok = PushButton(app, text="Button")


if __name__ == "__main__":
    print("Starting ", __file__)
    app.display()
