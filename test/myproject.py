# import the flask library
from flask import Flask, render_template, Flask, Response, request, abort, render_template_string, send_from_directory, jsonify
import os

# create the app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    values = request.values

    print values


    action = ""

    if values.get('function') == 'sendKey':
        key = values.get('key')
        currentDisplay = values.get('currentDisplay')
        currentAction = values.get('currentAction')

        try:
            # just to check if the button is a number
            keyInt = int(key)

            # create the new display
            display = currentDisplay+key

            print display

            if currentAction == 'plus':
                display = round(float(currentDisplay) + float(key),3)

            if currentAction == 'minus':
                display = round(float(currentDisplay) - float(key),3)

            if currentAction == 'divide':
                display = round(float(currentDisplay) / float(key),3)

            if currentAction == 'multi':
                display = round(float(currentDisplay) * float(key),3)

        except:
            display = values.get('currentDisplay')

            if key == 'plus':
                action = "plus"
            if key == 'minus':
                action = "minus"
            if key == 'divide':
                action = "divide"
            if key == 'multi':
                action = "multi"
            if key == 'AC':
                display = ""


        return jsonify(display = display, action = action)


    return render_template("homepage.html")

# run it - debug=True so the server reloads when we make code change
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
