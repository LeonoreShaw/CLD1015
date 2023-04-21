from flask import Flask, render_template, request
import pyvisa

app = Flask(__name__)

# Open the connection to the device
rm = pyvisa.ResourceManager()
# instr = rm.open_resource('USB0::0x1313::0x804F::M00295819::INSTR')

@app.route('/')
def index():
    # Get the current setpoint
    # setpoint = instr.query("source1:current:level:amplitude?")
    return render_template('index.html', setpoint=1)

@app.route('/set_setpoint', methods=['POST'])
def set_setpoint():
    # Set the new setpoint
    setpoint = request.form['setpoint']
    # instr.write("source1:current:level:amplitude {}".format(setpoint))
    return "Setpoint set to {}".format(setpoint)

@app.route('/turn_on')
def turn_on():
    # Turn on the LD
    # instr.write("output1:state on")
    return "LD turned on"

@app.route('/turn_off')
def turn_off():
    # Turn off the LD
    # instr.write("output1:state off")
    return "LD turned off"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)