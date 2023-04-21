import pyvisa
import tkinter as tk

class LaserController(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        
        # 连接设备
        self.rm = pyvisa.ResourceManager()
        self.instrument = self.rm.open_resource('USB0::0x1313::0x8089::M00426573::INSTR')
        
    def create_widgets(self):
        # 电流输入框和按钮
        self.current_label = tk.Label(self, text="Current (A):")
        self.current_label.pack(side="left")
        self.current_entry = tk.Entry(self)
        self.current_entry.pack(side="left")
        self.current_button = tk.Button(self, text="Set", command=self.set_current)
        self.current_button.pack(side="left")
        
        # 输出按钮
        self.output_button = tk.Button(self, text="Output ON", command=self.toggle_output)
        self.output_button.pack(side="left")
        
        # 关闭按钮
        self.quit_button = tk.Button(self, text="Quit", fg="red", command=self.quit)
        self.quit_button.pack(side="right")
    
    def set_current(self):
        # 设置电流
        current = float(self.current_entry.get())
        self.instrument.write(f'LASer:CURRent {current}')
        self.current_entry.delete(0, tk.END)
        
    def toggle_output(self):
        # 切换输出状态
        if self.output_button["text"] == "Output ON":
            self.instrument.write('LASer:OUTPut ON')
            self.output_button["text"] = "Output OFF"
        else:
            self.instrument.write('LASer:OUTPut OFF')
            self.output_button["text"] = "Output ON"
            
    def quit(self):
        # 关闭设备并退出应用程序
        self.instrument.close()
        self.rm.close()
        self.master.destroy()
        
root = tk.Tk()
app = LaserController(master=root)
app.mainloop()
