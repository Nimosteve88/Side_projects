import justpy as jp
import definition
import json

class Api:
    """ Handles request at /api?w=word"""
    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')  #w is the URL parameter

        defined = definition.Definition(word).get()

        response = {
            "word": word,
            "definition": defined
        }
        wp.html = json.dumps(response) #produces a string out of the dictionary
        return wp


