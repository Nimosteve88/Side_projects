import justpy as jp


@jp.SetRoute("/home")  # connects the url to the function below
def home():
    wp = jp.QuasarPage(tailwind=True)
    div = jp.Div(a=wp, classes="bg-gray-200 h-screen")

    div1 = jp.Div(a=div, classes="grid grid-cols-3 gap-4 p-4 bordr border-black")
    in_1 = jp.Input(a=div1, placeholder="Enter First Value", classes="form-input")
    in_2 = jp.Input(a=div1, placeholder="Enter Second Value", classes="form-input")

    jp.Div(a=div1, placeholder="Just another div", classes="text-gray-600")
    jp.Div(a=div1, placeholder="Yet another div", classes="text-gray-600")
    d_output = jp.Div(a=div1, text="Result goes here....", classes="text-gray-600")

    div2 = jp.Div(a=div, classes="grid grid-cols-2 gap-4")
    jp.Button(a=div2, text="Calculate", click = sum_up, in1=in_1, in2=in_2, d = d_output,
              classes="border border-blue-500 m-2 py-1 px-4 rounded"
              "text-blue-600 hover:bg-red-500 hover:text-white")
    jp.Div(a=div2, text="I am a cool interactive div!", mouseenter=mouse_enter,
    mouseleave=mouse_leave,
    classes="hoover:bg-red-500")
    return wp

def sum_up(widget, msg): #msg is a dict which contains info about the event,
    # widget represents the button to be clicked
   sum = float(widget.in1.value) + float(widget.in2.value)
   widget.d.text = sum

def mouse_enter(widget, msg):
    widget.text = "A mouse entered the house!"

def mouse_leave(widget, msg):
    widget.text = "The mouse left!"



jp.Route("/", home)

jp.justpy()
