import inspect

import justpy as jp
import page

imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj): #checks if obj is actually a class
        if issubclass(obj, page.Page) and obj is not page.Page:  # checks if the following path conatins page.
            # Page and whether it has attributes
            jp.Route(obj.path, obj.serve)

# jp.Route(Home.path, Home.serve)

# jp.Route(About.path, About.serve)

# jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy(port=8001)
