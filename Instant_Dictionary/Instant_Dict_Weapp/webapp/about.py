import justpy as jp
import layout
import page
# About is more concerned about handling the url. This will make the connection
# between the routing and the visual page
class About(page.Page): #this class 'has a' quasar page framework. This is composition
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the About page!", classes="text-4xl n-2")
        jp.Div(a=div,
               text="""You are provided with demonstration code that shows the use of basic functions of the Metro board. 
               The WiFi interface is used to host a basic webpage, which you will see hard-coded into the demonstration code. 
               The webpage provides two links which, when pressed, 
               turn on and off the onboard LED. Use the Arduino Serial Monitor to connect to the board via USB and you 
               will see some debug messages reporting on the connection status. Whenever the webpage is retrieved you 
               will see the HTML request made by the web browser. """,
               classes="text-lg")
        return wp

