import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

class wms_app(toga.App):
    def startup(self):
        # Create the main box with flex layout
        main_box = toga.Box(
            style=Pack(
                flex=1,
                direction=COLUMN,
                alignment=CENTER,
                padding=0,
                #margin=0
            )
        )

        # Create the WebView with full flex (to fill available space)
        webview = toga.WebView(
            url='https://wmsvictoria-3d9b896f40e5.herokuapp.com/',
            style=Pack(
                flex=1,   # Use flex to fill space
                padding=0,
                #margin=0
            )
        )

        # Add the WebView to the main box
        main_box.add(webview)

        # Create the main window with full size
        self.main_window = toga.MainWindow(
            title=self.formal_name
        )
        self.main_window.content = main_box
        #self.main_window.show_full_screen()  # Show the app in full screen mode

def main():
    return wms_app()
