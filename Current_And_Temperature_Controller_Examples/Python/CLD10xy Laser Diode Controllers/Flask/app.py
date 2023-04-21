from flask import Flask, render_template, request
import pyvisa

# 创建资源管理器对象
rm = pyvisa.ResourceManager()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/connect", methods=["POST"])
def connect_device():
    # 连接设备
    # instr = rm.open_resource('USB0::0x1313::0x804F::M00295819::INSTR')

    # 设置电流
    # instr.write("source1:current:level:amplitude 0.065")
    # current = instr.query("source1:current:level:amplitude?")

    # 关闭资源
    # instr.close()
    rm.close()

    # 将结果发送回前端
    return '0.065'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
