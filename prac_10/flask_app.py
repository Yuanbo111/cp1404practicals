from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name')
        return render_template('greet.html', name=name)
    return render_template('greet.html', name=None)

def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32

@app.route('/f/<celsius>')
def convert_to_fahrenheit(celsius):
    try:
        celsius_float = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius_float)
        # Required useful text: show both input and output
        return f"{celsius_float}°C is {fahrenheit:.2f}°F"
    except ValueError:
        return "Invalid input. Please enter a numeric Celsius value."

if __name__ == '__main__':
    app.run(debug=True)