###################--------------TkDial-Meter--------------###################

import tkinter as tk
import tkinter.font as tkFont
import math, cmath

class Meter(tk.Canvas):
    
    def __init__(self,
                 master,
                 start: float = 0,
                 end: float = 100,
                 radius: int = 250,
                 width: int = None,
                 height: int = None,
                 text: str = " ",
                 text_color: str = "black",
                 text_font: str = None,
                 border_width: int = 1,
                 border_color: int = "grey40",
                 major_divisions: int = 10,
                 minor_divisions: int = 1,
                 start_angle: int = 240,
                 end_angle: int = -295,
                 axis_color: str = "grey80",
                 bg: str = None,
                 fg: str = "white",
                 scroll: bool = True,
                 scroll_steps: float = 1,
                 scale_color: str = "black",
                 needle_color: str = "grey30",
                 integer: bool = False,
                 state: str = "normal",
                 command=None):
        
        self.bg = bg
        self.fg = fg
        self.major_div = major_divisions
        self.min_div = minor_divisions
        self.radius = radius  
        self.border_width = border_width
        self.text = text
        self.start_angle = start_angle 
        self.end_angle = end_angle
        self.start = start
        self.max = end
        self.axis_color = axis_color
        self.end = self.start_angle + self.end_angle
        self.scale_color = scale_color
        self.bd_color = border_color
        self.bound = True
        self.integer = integer
        self.needle_color = needle_color
        self.text_color = text_color
        self.value = self.start  
        self.text_font = text_font
        self.scroll = scroll
        self.scroll_steps = scroll_steps
        self.command = command
        self.state = state
        self.__x = radius/2
        self.__y = radius/2
        
        if self.start > self.max:
            self.direction = -1
        else:
            self.direction = 1
            
        if width is None:
            self.width = self.radius + self.border_width
        else:
            self.width = width
        
        if height is None:
            self.height = self.radius + self.border_width
        else:
            self.height = height
        
        super().__init__(master, width=self.width, height=self.height, bg=self.bg, borderwidth=0, highlightthickness=0)
        
        self.create_oval(self.border_width, self.border_width, self.radius, self.radius,
                         width=self.border_width, fill=self.fg, outline=self.bd_color, tags="face")
        
        self.create_divisions()
        self.create_needle()
        
        if self.scroll==True:
            super().bind('<MouseWheel>', self.scroll_command)
        
    def scroll_command(self, event):
        """
        This function is used to change the value of the dial with mouse scroll
        """
        if event.delta > 0:        
            if self.value < self.max:
                self.set(self.value+self.scroll_steps)
            elif  self.value==self.max:
                self.set(self.max)
            else:
                self.set(self.value-self.scroll_steps)
        else:
            if self.value > self.start:
                self.set(self.value-self.scroll_steps)
            elif  self.value==self.start:
                self.set(self.start)
            else:
                self.set(self.value+self.scroll_steps)
                
    def create_divisions(self):
        """
        This function creates the division lines.
        """
        
        self.xn = self.yn = (self.radius + self.border_width) / 2
        self.radians = (self.radius - self.border_width) / 2  
        self.absolute = abs(self.max - self.start)
        self.arc_pos = self.radians / 3

        # minor scale
        if self.min_div != 0:
            lines = int(self.absolute / self.min_div) + 1
            angles = (self.start_angle + n * self.end_angle * self.min_div / self.absolute for n in range(lines))
            for angle in angles:
                x1 = self.xn + (self.radians - self.arc_pos) * math.cos(math.radians(angle))
                y1 = self.yn - (self.radians - self.arc_pos) * math.sin(math.radians(angle))
                x2 = x1 + self.arc_pos / 5 * math.cos(math.radians(angle))
                y2 = y1 - self.arc_pos / 5 * math.sin(math.radians(angle))
                self.create_line(x1, y1, x2, y2, fill=self.scale_color, tags='min_scale')

        # major scale 
        lines = int(self.absolute / self.major_div) + int(abs(self.end_angle) != 360)
        angles = (self.start_angle + n * self.end_angle * self.major_div / self.absolute for n in range(lines))
        textvals = (self.start + n * self.major_div * self.direction for n in range(lines))
        textpos = self.arc_pos / 2.5
        self.scalefont = tkFont.Font(size=int(self.arc_pos / 5), weight='bold')
        for angle, textval in zip(angles, textvals):
            x1 = self.xn + (self.radians - self.arc_pos) * math.cos(math.radians(angle))
            y1 = self.yn - (self.radians - self.arc_pos) * math.sin(math.radians(angle))
            x2 = x1 + self.arc_pos / 3 * math.cos(math.radians(angle))
            y2 = y1 - self.arc_pos / 3 * math.sin(math.radians(angle))
            self.create_line(x1, y1, x2, y2, width=3, tags='major_scale', fill=self.scale_color)
            x1 = self.xn + (self.radians - textpos) * math.cos(math.radians(angle))
            y1 = self.yn - (self.radians - textpos) * math.sin(math.radians(angle))
            self.create_text(x1, y1, text=textval, font=self.scalefont, fill=self.scale_color, tags='scale_text')

        # scale arc
        x1 = y1 = self.arc_pos + self.border_width
        x2 = y2 = self.radius - self.arc_pos
        if abs(self.end_angle) != 360:
            self.create_arc(x1, y1, x2, y2, start=self.start_angle, extent=self.end_angle, width=2,
                            outline=self.scale_color, style='arc', tags='arc')
        else:
            self.create_oval(x1, y1, x2, y2, width=2, tags='arc')
            
    def create_needle(self):
        """
        This function creates the needle and axis that can rotate.
        """
        x1 = self.xn
        y1 = self.yn + self.arc_pos * 4 / 3
        
        self.create_text(x1, y1, font=self.text_font, tags='text')
        self.axis_rad = self.radius / 25
        xy1 = (self.xn + 2.5 * self.arc_pos, self.yn)
        xy2 = (self.xn, self.yn + 0.75 * self.axis_rad)
        xy3 = (self.xn, self.yn - 0.75 * self.axis_rad)
        self.needle_coords = [xy1, xy2, xy3]
        self.needle = self.create_polygon(self.needle_coords, tags='needle', fill=self.needle_color)    
        self.create_oval(self.xn - self.axis_rad, self.yn - self.axis_rad, self.xn + self.axis_rad, self.yn + self.axis_rad,
                         outline=self.bd_color, fill=self.axis_color, tags='axis')
        self.needle_state()
        self.set(self.value)
        
    def needle_state(self):
        """
        This function binds/unbinds the mouse button with the needle
        """
        if self.state=="normal":
            self.tag_bind(
                tagOrId="needle",
                sequence="<ButtonPress-1>",
                func=lambda event: self.tag_bind(
                    tagOrId="needle",
                    sequence="<Motion>",
                    func=self.rotate_needle
                )
            )
            self.tag_bind(
                tagOrId="needle",
                sequence="<ButtonRelease-1>",
                func=lambda event: self.tag_unbind(
                    tagOrId="needle",
                    sequence="<Motion>"
                )
            )
        else:
            self.tag_unbind(
                tagOrId="needle",
                sequence="<ButtonPress-1>")
            self.tag_unbind(
                tagOrId="needle",
                sequence="<ButtonRelease-1>")
            
        self.previous_angle = 0
        
    def rotate_needle(self, event):
        
        angle = math.degrees(math.atan2(self.__y - event.y, event.x - self.__x))
        if self.previous_angle>angle:
            self.set(self.value+self.scroll_steps)
        else:
            self.set(self.value-self.scroll_steps)
        self.previous_angle=angle
        
    def set(self, value):
        """
        This function is used to set the position of the needle
        """
        
        self.value = value
        angle = (value - self.start) * (self.end - self.start_angle) / (self.max - self.start) + self.start_angle

        if self.start < self.max:  
            if value < self.start:
                angle = self.start_angle
                self.value = self.start
                value = self.start
            elif value > self.max:
                angle = self.end
                self.value = self.max
                value = self.max
        else:
            if value > self.start:
                angle = self.start_angle
                self.value = self.start
                value = self.start
            elif value < self.max:
                angle = self.end
                self.value = self.max
                value = self.max
                
        xy_pos = []
        offset = complex(self.xn, self.yn)
        for x, y in self.needle_coords:
            exp = cmath.exp(math.radians(-angle) * 1j) * (complex(x, y) - offset) + offset
            xy_pos.append(exp.real)
            xy_pos.append(exp.imag)
        self.coords(self.needle, *xy_pos)

        if self.integer==False:
            value = round(value, 2)
        else:
            value = int(value)
        self.itemconfig(tagOrId='text', text=str(value)+self.text, fill=self.text_color)
        
        if self.previous_angle!=0:
            if self.command is not None:
                self.command()
            
    def get(self):
        """
        This function returns the current value of the meter
        :return: float
        """
        return self.value
    
    def set_mark(self, from_, to, color="red"):
        colored_lines = self.find_withtag('min_scale')[from_:to]
        for line in colored_lines:
            self.itemconfig(line, fill=color, width=6)
            
    def configure(self, **kwargs):
        """
        This function contains some configurable options
        """
        
        if "text" in kwargs:
             self.itemconfigure(
                tagOrId="text",
                text=kwargs.pop("text"))
             
        if "start" in kwargs:
            self.start = kwargs.pop("start")
            
        if "end" in kwargs:
            self.end = kwargs.pop("end")
            
        if "bg" in kwargs:
            super().configure(bg=kwargs.pop("bg"))
            
        if "width" in kwargs:
            super().configure(width=kwargs.pop("width"))
            
        if "height" in kwargs:
            super().configure(height=kwargs.pop("height"))
            
        if "scale_color" in kwargs:
            self.itemconfigure(tagOrId="min_scale",
                    fill=kwargs['scale_color'])
            self.itemconfigure(
                tagOrId="major_scale",
                fill=kwargs['scale_color'])
            self.itemconfigure(
                tagOrId="arc",
                outline=kwargs.pop('scale_color'))
            
        if "fg" in kwargs:
            self.itemconfigure(
                tagOrId="face",
                fill=kwargs.pop('fg'))
            
        if "text_color" in kwargs:
            self.itemconfigure(
                tagOrId="text",
                fill=kwargs.pop("text_color"))
            
        if "needle_color" in kwargs:
            self.itemconfigure(
                tagOrId="needle",
                fill=kwargs.pop("needle_color"))
            
        if "border_color" in kwargs:
            self.itemconfigure(
                tagOrId="face",
                outline=kwargs.pop("border_color"))
            
        if "axis_color" in kwargs:
            self.itemconfigure(
                tagOrId="axis",
                fill=kwargs.pop("axis_color"))
            
        if "scroll_steps" in kwargs:
            self.scroll_steps = kwargs.pop("scroll_steps")
            
        if "scroll" in kwargs:
            if kwargs["scroll"]==False:
                super().unbind('<MouseWheel>')
            else:
                super().bind('<MouseWheel>', self.scroll_command)
            kwargs.pop("scroll")
            
        if "integer" in kwargs:
            self.set(self.value)
            self.integer = kwargs.pop("integer")
            
        if "state" in kwargs:
            self.state = kwargs.pop("state")
            self.needle_state()
            
        if len(kwargs)>0:
            raise ValueError("unknown option: " + list(kwargs.keys())[0])
