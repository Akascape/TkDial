# TkDial
**This is a circular rotatory dial-knob widget for tkinter. It can be used in place of normal slider.**

## Usage

**Simple Example:**
```python
import tkinter as tk
from tkdial import Dial

app = tk.Tk()

dial = Dial(app, color_gradient=("white", "black"))
dial.grid(padx=10, pady=10)

app.mainloop()
```
![Screenshot1](https://user-images.githubusercontent.com/89206401/202906601-89bd91ed-d685-4a4e-9ddc-7824f278ca4b.png)

### **Example 2**
```python
import tkinter as tk
from tkdial import Dial

app = tk.Tk()

#Some color combinations
color_combinations = [("yellow", "red"), ("white", "cyan"), ("red", "pink"), ("black", "green"),
                    ("white", "black"), ("blue", "blue"), ("green", "green"), ("white", "pink"),
                    ("red", "black"), ("green", "cyan"), ("cyan","black"), ("pink", "blue")]

for i in range (12):
    dial = Dial(master=app, color_gradient=color_combinations[i],
                unit_length=10, radius=40, needle_color=color_combinations[i][1])
    if i<6:
        dial.grid(row=1, padx=10, pady=10, column=i)
    else:
        dial.grid(row=2, padx=10, pady=10, column=11-i)

app.mainloop()
```
![Screenshot2](https://user-images.githubusercontent.com/89206401/202906615-e4c484de-ed79-495e-b12f-d30b9d238eac.png)

### **Example 3**

**Implemented with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)**

```python
import customtkinter
from tkdial import Dial

customtkinter.set_appearance_mode("Dark") 
              
app = customtkinter.CTk()
app.geometry("350x400")
                
app.grid_columnconfigure((0,1), weight=1)
app.grid_rowconfigure((0,1), weight=1)

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.grid(padx=20, pady=20, sticky="nswe")

dial1 = Dial(master=frame_1, color_gradient=("green", "cyan"), bg="#2a2d2e",
             text_color="white", text="Current: ", unit_length=10, radius=50)
dial1.grid(padx=20, pady=20)

dial2 = Dial(master=frame_1, color_gradient=("yellow", "white"), bg="#2a2d2e",
             text_color="white", text="Position: ", unit_length=10, radius=50)
dial2.grid(padx=20, pady=20)

dial3 = Dial(master=frame_1, color_gradient=("white", "pink"), bg="#2a2d2e",
             text_color="white", text=" ", unit_length=10, radius=50)
dial3.grid(row=0, column=1, padx=20, pady=20)

dial4 = Dial(master=frame_1, color_gradient=("red", "red"), bg="#2a2d2e",
             text_color="white", text="", unit_width=15, radius=50)
dial4.grid(row=1, column=1, padx=20, pady=20)

app.mainloop()                  
```
![Screenshot 3](https://user-images.githubusercontent.com/89206401/202906638-a1c863b7-54b0-4e7a-9619-415e28b3ab51.png)

## Documentation
### Options:
  | Parameters  | Description |
  | -------- | ----------- |
  | _master_ | The master parameter is the parent widget |
  | _bg_  | The default background color of the dial widget |
  | _width_ | Define width of the widget manually (optional) |
  | _height_ | Define height of the widget manually (optional) |
  | _x_ | Determines the horizontal position of the dial in the canvas |
  | _y_ | Determines the vertical position of the dial in the canvas |
  | _start_ |  The start point of the range where the needle will rotate |
  | _end_ |  The end point of the range where the needle will rotate |
  | _radius_ | Determines the distance of the unit lines between the center and the edge and also the length of the needle line |
  | _unit_length_ | Specify the length of the lines |
  | _unit_width_ | Specify the width of the lines |
  | _unit_color_ |  Specify the color of the unit lines |
  | _needle_color_ | Specify the color of the needle line |
  | _color_gradient_ | Specify which color gradient will be used for the units |
  | _text_ | A string that will be displayed under the dial object |
  | _text_color_ | Specify the color of the text that will be displayed under the dial object |
  | _text_font_ | Specify the font of the text that will be displayed under the dial object |
  | _integer_ | A boolean (True/False), displays only the integer value in text if True |
  | _command_ | Call a function whenever the needle is rotated |
  
### Methods:

  | Methods   | Description |
  |-----------|-------------|
  | _.get()_ | get the current value of the dial |
  | _.set()_ | set the value of the dial |
  | _.set_text()_ | configure text of the dial |
## Conclusion
This widget is based on this [VolumeControl](https://github.com/dildeolupbiten/VolumeControl) widget with lots of modifications.

I hope it will be helpful for UI development in tkinter.

[<img src="https://img.shields.io/badge/LICENSE-CC0_v0.1-informational?&color=blue&style=for-the-badge" width="200">](https://github.com/Akascape/TkDial/blob/main/LICENSE)
