# TkDial
**This is a library containing some circular rotatory dial-knob widgets for Tkinter. It can be used in place of normal sliders and scale.**

[![PyPI](https://img.shields.io/pypi/v/tkdial)](https://pypi.org/project/tkdial)
![Platform](https://img.shields.io/powershellgallery/p/Pester?color=blue)
[![Downloads](https://static.pepy.tech/personalized-badge/tkdial?period=total&units=international_system&left_color=green&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/tkdial)

## Installation
```
pip install tkdial
```

# Dial Widget

## Usage

**Simple Example:**
```python
import tkinter as tk
from tkdial import Dial

app = tk.Tk()

dial = Dial(app)
dial.grid(padx=10, pady=10)

app.mainloop()
```
![Screenshot1](https://user-images.githubusercontent.com/89206401/202906601-89bd91ed-d685-4a4e-9ddc-7824f278ca4b.png)

### **Example 2**
```python
import tkinter as tk
from tkdial import Dial

app = tk.Tk()

# some color combinations
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

dial1 = Dial(master=frame_1, color_gradient=("green", "cyan"),
             text_color="white", text="Current: ", unit_length=10, radius=50)
dial1.grid(padx=20, pady=20)

dial2 = Dial(master=frame_1, color_gradient=("yellow", "white"),
             text_color="white", text="Position: ", unit_length=10, radius=50)
dial2.grid(padx=20, pady=20)

dial3 = Dial(master=frame_1, color_gradient=("white", "pink"),
             text_color="white", text=" ", unit_length=10, radius=50)
dial3.grid(row=0, column=1, padx=20, pady=20)

dial4 = Dial(master=frame_1, color_gradient=("green", "green"),
             text_color="white", text="", unit_width=15, radius=50)
dial4.grid(row=1, column=1, padx=20, pady=20)

app.mainloop()                
```
![Screenshot 3](https://user-images.githubusercontent.com/89206401/202906638-a1c863b7-54b0-4e7a-9619-415e28b3ab51.png)

## Arguments:
  | Parameters  | Description |
  | -------- | ----------- |
  | _master_ | The master parameter is the parent widget |
  | _bg_  | The default background color of the dial widget |
  | _width_ | Define width of the widget manually (optional) |
  | _height_ | Define height of the widget manually (optional) |
  | _x_ | Determines the horizontal position of the dial in the canvas |
  | _y_ | Determines the vertical position of the dial in the canvas |
  | _start_ |  The start point of the range from where the needle will rotate |
  | _end_ |  The end point of the range |
  | _radius_ | Determines the distance of the unit lines between the center and the edge and also the length of the needle line |
  | _unit_length_ | Specify the length of the lines |
  | _unit_width_ | Specify the width of the lines |
  | _unit_color_ |  Specify the color of the unit lines |
  | _needle_color_ | Specify the color of the needle line |
  | _color_gradient_ | Specify which color gradient will be used for the units |
  | _text_ | A string that will be displayed under the dial object with value |
  | _text_color_ | Specify the color of the text that will be displayed under the dial object |
  | _text_font_ | Specify the font of the text that will be displayed under the dial object |
  | _integer_ | A boolean (True/False), displays only the integer value in text if True (default=False) |
  | _scroll_ | A boolean (True/False), enables mouse scroll in dial (default=True) |
  | _scroll_steps_ | Number of steps per scroll |
  | _state_ | Specify the state of the needle |
  | _command_ | Call a function whenever the needle is rotated |
  
### Methods:

  | Methods   | Description |
  |-----------|-------------|
  | _.get()_ | get the current value of the dial |
  | _.set()_ | set the value of the dial |
  | _.configure()_ | configure parameters of the dial |
 
# Scroll Knob

## Usage
**Simple Example**
```python
import tkinter
from tkdial import ScrollKnob
    
app = tkinter.Tk()

knob = ScrollKnob(app, start=0, end=100, steps=10)
knob.grid()
                
app.mainloop()      
```
![Simple Program](https://user-images.githubusercontent.com/89206401/204139370-73c66402-ec9a-4edc-9891-c63b209fd5e4.png)

### **Different Knob styles:**
```python
import customtkinter
from tkdial import ScrollKnob

app = customtkinter.CTk()
app.geometry("500x500")

knob1 = ScrollKnob(app, radius=250, progress_color="#87ceeb", steps=10,
                 border_width=40, start_angle=90, inner_width=1, outer_width=1,
                 text_font="calibri 20", text_color="#87ceeb", bar_color="black")
knob1.grid(row=0, column=0)

knob2 = ScrollKnob(app, radius=200, progress_color="#7eff00",
                 border_width=40, start_angle=90, inner_width=1, outer_width=0,
                 text_font="calibri 20", text_color="#7eff00", integer=True,
                 fg="#212325")
knob2.grid(row=1, column=0)

knob3 = ScrollKnob(app, text=" ", radius=250, progress_color="white",
                   bar_color="#2937a6", border_width=30, start_angle=0, inner_width=5,
                   outer_width=0, text_font="calibri 20", steps=1, text_color="white", fg="#303ba1")
knob3.grid(row=0, column=1)

knob4 = ScrollKnob(app, text=" ", steps=10, radius=200, bar_color="#242424", 
                   progress_color="yellow", outer_color="yellow", outer_length=10, 
                   border_width=30, start_angle=270, inner_width=0, outer_width=5, text_font="calibri 20", 
                   text_color="white", fg="#212325")
knob4.grid(row=1, column=1)
                
app.mainloop() 
```
![Complex example](https://user-images.githubusercontent.com/89206401/204139428-c3c3c313-539f-4867-9d50-8876a19432ee.png)

## Arguments:
  | Parameters  | Description |
  | -------- | ----------- |
  | _master_ | The master parameter is the parent widget |
  | _bg_  | The default background color of the knob widget |
  | _width_ | Define width of the widget manually (optional) |
  | _height_ | Define height of the widget manually (optional) |
  | _start_ |  The start point of the range from where the bar will rotate |
  | _end_ |  The end point of the range |
  | _radius_ | Define the radius of the knob |
  | _border_width_ | Define the width of progress bar with respect to the outer and inner ring |
  | _start_angle_ | Determines the angle from where to rotate |
  | _text_ | A string that will be displayed on the knob with value |
  | _text_color_ | Specify the color of the text that will be displayed on the knob |
  | _text_font_ | Specify the font of the text that will be displayed on the knob |
  | _integer_ | A boolean (True/False), displays only the integer value in text if True (default=False) |
  | _fg_ | Specify the color of the inner circle |
  | _progress_color_ | Define the color of the progress bar |
  | _bar_color_ | Define the color of the progress bar's background |
  | _inner_width_ | Define the width of the inner ring |
  | _inner_color_ | Specify the color of the inner ring |
  | _outer_width_ | Define the width of the outer ring |
  | _outer_length_ | Define the distance between progress bar and outer ring |
  | _inner_color_ | Specify the color of the outer ring |
  | _steps_ | Number of steps per scroll |
  | _state_ | Specify the state of the needle |
  | _command_ | Call a function whenever the bar is moved |
  
### Methods:
  | Methods   | Description |
  |-----------|-------------|
  | _.get()_ | get the current value of the knob |
  | _.set()_ | set the value of the knob |
  | _.configure()_ | configure parameters of the knob | 
  
# Meter

## Usage
**Simple Example**
```python
import tkinter
from tkdial import Meter

root = tkinter.Tk()
dial = Meter(root)
dial.pack(padx=10, pady=10)

root.mainloop()
```
![simple_meter](https://user-images.githubusercontent.com/89206401/204718544-c8589399-7f13-44bb-a07d-77f328ce76b9.png)

### **Different Meter Styles:**
```python
import customtkinter
from tkdial import Meter

app = customtkinter.CTk()
app.geometry("950x350")

meter1 = Meter(app, radius=300, start=0, end=160, border_width=0,
               fg="black", text_color="white", start_angle=270, end_angle=-270,
               text_font="DS-Digital 30", scale_color="white", needle_color="red")
meter1.set_mark(140, 160) # set red marking from 140 to 160
meter1.grid(row=0, column=1, padx=20, pady=30)

meter2 = Meter(app, radius=260, start=0, end=200, border_width=5,
               fg="black", text_color="white", start_angle=270, end_angle=-360,
               text_font="DS-Digital 30", scale_color="black", axis_color="white",
               needle_color="white")
meter2.set_mark(1, 100, "#92d050")
meter2.set_mark(105, 150, "yellow")
meter2.set_mark(155, 196, "red")
meter2.set(80) # set value
meter2.grid(row=0, column=0, padx=20, pady=30)

meter3 = Meter(app, fg="#242424", radius=300, start=0, end=50,
               major_divisions=10, border_width=0, text_color="white",
               start_angle=0, end_angle=-360, scale_color="white", axis_color="cyan",
               needle_color="white",  scroll_steps=0.2)
meter3.set(15)
meter3.grid(row=0, column=2, pady=30)

app.mainloop()
```
![styles_meter](https://user-images.githubusercontent.com/89206401/204718389-d3195b3b-0f7a-41c3-85b8-ffc1d961db70.png)

## Arguments:
  | Parameters  | Description |
  | -------- | ----------- |
  | _master_ | The master parameter is the parent widget |
  | _bg_  | The default background color of the meter widget |
  | _fg_ | Specify the color of the meter face |
  | _width_ | Define width of the widget manually (optional) |
  | _height_ | Define height of the widget manually (optional) |
  | _start_ |  The start point of the range from where the needle will rotate |
  | _end_ |  The end point of the range |
  | _start_angle_ | Determines the starting angle of the arc |
  | _end_angle_ | Determines the final angle of the arc |
  | _radius_ | Determines the radius for the widget |
  | _major_divisions_ | Determines the number of major lines in the scale |
  | _minor_divisions_ | Determines the number of minor lines in the scale |
  | _scale_color_ |  Specify the color of the meter scale |
  | _border_width_ | Define the width of the border case (default=1) |
  | _border_color_ |  Specify the color of the border case |
  | _needle_color_ | Specify the color of the needle line |
  | _axis_color_ | Specify which color of the axis wheel |
  | _text_ | A string that will be displayed under the meter with value  |
  | _text_color_ | Specify the color of the text that will be displayed under the meter |
  | _text_font_ | Specify the font of the text that will be displayed under the meter |
  | _integer_ | A boolean (True/False), displays only the integer value in text if True (default=False) |
  | _scroll_ | A boolean (True/False), enables mouse scroll in meter (default=True) |
  | _scroll_steps_ | Number of steps per scroll |
  | _state_ | Unbind/Bind the mouse movement with the needle |
  | _command_ | Call a function whenever the needle is rotated |
  
### Methods:
  | Methods   | Description |
  |-----------|-------------|
  | _.get()_ | get the current value of the meter |
  | _.set()_ | set the value of the meter |
  | _.configure()_ | configure parameters of the meter| 
  | _.set_mark()_ | set markings for the scale. Eg: **meter.set_mark(from, to, color)** | 
  
# JogWheel

## Usage

```python
import tkinter
from tkdial import Jogwheel

app = tkinter.Tk()

knob = Jogwheel(app)
knob.grid()

app.mainloop()
```
![Jogwheel](https://user-images.githubusercontent.com/89206401/232750598-37f4f863-0aba-48c8-9a69-4cb1e15e1457.png)

### Styles: 
```python
import customtkinter
from tkdial import Jogwheel

app = customtkinter.CTk()

wheel_1 = Jogwheel(app, radius=200, fg="#045252", scale_color="white",
                text=None, button_radius=10)
wheel_1.set_mark(0,100, "green")

wheel_1.grid()

wheel_2 = Jogwheel(app, radius=200, fg="#045252", scale_color="white", start_angle=0,
                   end_angle=360, start=0, end=200, text="Volume: ", button_radius=10)
wheel_2.set_mark(0,50, "blue")
wheel_2.set_mark(50, 90, "green")
wheel_2.set_mark(90, 150, "orange")
wheel_2.set_mark(150, 200, "red")
wheel_2.grid()

app.mainloop()
```
![Jogwheel styles](https://user-images.githubusercontent.com/89206401/232751129-72d29a4e-d0ea-49b4-9051-e65cabd5fb55.png)


## Arguments:
  | Parameters  | Description |
  | -------- | ----------- |
  | _master_ | The master parameter is the parent widget |
  | _bg_  | The default background color of the widget |
  | _fg_ | Specify the color of the wheel face |
  | _width_ | Define width of the widget manually (optional) |
  | _height_ | Define height of the widget manually (optional) |
  | _start_ |  The start point of the range from where the knob will rotate |
  | _end_ |  The end point of the range |
  | _start_angle_ | Determines the starting angle of the arc |
  | _end_angle_ | Determines the final angle of the arc |
  | _radius_ | Determines the radius for the widget |
  | _divisions_ | Determines the number of scale lines in the scale |
  | _division_height_ | Determines the height of scale lines |
  | _scale_color_ |  Specify the color of the knob scale |
  | _border_width_ | Define the width of the border case (default=1) |
  | _border_color_ |  Specify the color of the border case |
  | _button_color_ | Specify the color of the knob |
  | _button_radius_ | Specify the radius the knob |
  | _text_ | A string that will be displayed with value |
  | _text_color_ | Specify the color of the text that will be displayed |
  | _text_font_ | Specify the font of the text that will be displayed |
  | _integer_ | A boolean (True/False), displays only the integer value in text if True (default=False) |
  | _scroll_ | A boolean (True/False), enables mouse scroll (default=True) |
  | _scroll_steps_ | Number of steps per scroll |
  | _state_ | Unbind/Bind the mouse movement with the widget |
  | _command_ | Call a function whenever the needle is rotated |
  
### Methods:
  | Methods   | Description |
  |-----------|-------------|
  | _.get()_ | get the current value of the knob |
  | _.set()_ | set the value of the knob |
  | _.configure()_ | configure parameters of the knob | 
  | _.set_mark()_ | set markings for the scale. Eg: **meter.set_mark(from, to, color)** | 
  
## ImageKnob
### Usage
```python
import tkinter
from tkdial import ImageKnob

app = tkinter.Tk()

customknob = ImageKnob(app, image="knob.png")
customknob.grid()

app.mainloop()
```

![customknob](https://user-images.githubusercontent.com/89206401/233058156-007f967e-796c-40f1-9c91-419d990fb725.png)

### Styles:
```python
# Note: images are not provided, only for reference
import customtkinter
from tkdial import ImageKnob

app = customtkinter.CTk()

customknob = ImageKnob(app, image="knob.png", text_color="white", text="Volume ")
customknob.grid(row=0, column=0)

customknob2 = ImageKnob(app, image="knob2.png", scale_image="scale1.png",text="", scale_width=120)
customknob2.grid(row=0, column=1, padx=20)

customknob3 = ImageKnob(app, image="knob3.png", scale_image="scale2.png",text="",
                        scale_width=50, start_angle=20, end_angle=-240,
                        progress_color="cyan", progress=True)
customknob3.grid(row=0, column=2)

app.mainloop()
```
![customknob styles](https://user-images.githubusercontent.com/89206401/233058217-34888954-89dd-4e30-80ac-98f2d4bba6eb.png)


## Arguments:
  | Parameters  | Description |
  | -------- | ----------- |
  | _master_ | The master parameter is the parent widget |
  | _bg_  | The default background color of the widget |
  | _width_ | Define width of the widget manually (optional) |
  | _height_ | Define height of the widget manually (optional) |
  | _start_ |  The start point of the range from where the knob will rotate |
  | _end_ |  The end point of the range |
  | _image_ | pass the knob image |
  | _scale_image_ | add a scale image (optional) |
  | _scale_width_ | specify relative distance between scale and knob image |
  | _start_angle_ | Determines the starting angle of the knob |
  | _end_angle_ | Determines the final angle of the knob |
  | _radius_ | Determines the radius for the widget |
  | _text_ | A string that will be displayed with value |
  | _text_color_ | Specify the color of the text that will be displayed |
  | _text_font_ | Specify the font of the text that will be displayed |
  | _integer_ | A boolean (True/False), displays only the integer value in text if True (default=False) |
  | _scroll_ | A boolean (True/False), enables mouse scroll (default=True) |
  | _scroll_steps_ | Number of steps per scroll |
  | _state_ | Unbind/Bind the mouse movement with the widget |
  | _command_ | Call a function whenever the needle is rotated |
  
### Methods:
  | Methods   | Description |
  |-----------|-------------|
  | _.get()_ | get the current value of the widget |
  | _.set()_ | set the value of the widget |
  | _.configure()_ | configure parameters of the widget | 

Note: Images should be cropped in fixed ratio (1:1) and saved with transparency(png).

## Conclusion
This library is focused to create some circular widgets that can be used with **Tkinter/Customtkinter** easily.
I hope it will be helpful in UI development with python.

[<img src="https://img.shields.io/badge/LICENSE-CC0_v0.1-informational?&color=blue&style=for-the-badge" width="200">](https://github.com/Akascape/TkDial/blob/main/LICENSE)
