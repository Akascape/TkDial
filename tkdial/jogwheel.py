###################--------------TkDial-Jogwheel--------------###################

import tkinter as tk
import tkinter.font as tkFont
import math

class Jogwheel(tk.Canvas):

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
                 border_width: int = 3,
                 border_color: str = "black",
                 divisions: int = 10,
                 division_height: int = 10,
                 start_angle: int = 240,
                 end_angle: int = -295,
                 button_color: str = "grey80",
                 button_radius: int = 20,
                 scale_color: str = "grey60",
                 bg: str = None,
                 fg: str = "white",
                 scroll: bool = True,
                 scroll_steps: float = 1,
                 integer: bool = False,
                 state: str = "normal",
                 progress: bool = True,
                 command=None):
        
        self.bg = bg
        self.fg = fg
        self.major_div = divisions
        self.radius = radius  
        self.border_width = border_width
        self.text = text
        self.start_angle = start_angle 
        self.end_angle = end_angle
        self.start = start
        self.max = end
        self.div_width = division_height
        self.end = self.start_angle + self.end_angle
        self.border_color = border_color
        self.scale_color = scale_color
        self.bound = True
        self.integer = integer
        self.text_color = text_color
        self.value = self.start  
        self.text_font = text_font
        self.scroll = scroll
        self.scroll_steps = scroll_steps
        self.bt_radius = button_radius
        self.command = command
        self.button_color = button_color
        self.state = state
        self.__x = radius/2
        self.__y = radius/2
        self.progress = progress

        if not self.bg:
            try:
                if master.winfo_name().startswith("!ctkframe"):
                    # get bg_color of customtkinter frames
                    self.bg = master._apply_appearance_mode(master.cget("fg_color"))
                else:
                    self.bg = master.cget("bg")
            except:  
                self.bg = "white"
                
        if self.end_angle==360:
            self.end_angle = 358
            
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
        
        self.create_divisions()
        self.create_needle()
        
        if self.scroll==True:
            super().bind('<MouseWheel>', self.scroll_command)
            super().bind("<Button-4>", lambda e: self.scroll_command(-1))
            super().bind("<Button-5>", lambda e: self.scroll_command(1))
            
    def scroll_command(self, event):
        """
        This function is used to change the value of the dial with mouse scroll
        """
        if type(event) is int:
            event_delta = event
        else:
            event_delta = event.delta
            
        if event_delta > 0:        
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
        
        self.xn = self.yn = (self.radius) / 2
        self.radians = (self.radius) / 2
        self.absolute = abs(self.max - self.start)
        self.arc_pos = (self.radians) / 4
        
        # major scale 

        lines = int(self.absolute) + 1
        angles = (self.start_angle + n * self.end_angle / self.absolute for n in range(lines))

        for angle in angles:
            x1 = self.xn + (self.radians - self.arc_pos) * math.cos(math.radians(angle))
            y1 = self.yn - (self.radians - self.arc_pos) * math.sin(math.radians(angle))
            x2 = x1 + (self.arc_pos + self.div_width) / 3 * math.cos(math.radians(angle))
            y2 = y1 - (self.arc_pos + self.div_width)/ 3 * math.sin(math.radians(angle))
            self.create_line(x1, y1, x2, y2, fill=self.scale_color, width=5, tags='min_scale')

        if self.progress:
            x5 = self.radius - self.arc_pos + (self.arc_pos + self.div_width)/ 6
            x6 = self.arc_pos - (self.arc_pos + self.div_width)/ 6
            
            self.arc_id = self.create_arc(x6, x6, x5, x5, extent=0, tag="progress",
                                            start=self.start_angle+self.end_angle, outline=self.scale_color,
                                            width=(self.arc_pos + self.div_width)/ 3, style='arc')
        
        lines = int(self.absolute / self.major_div) + int(abs(self.end_angle) != 360)
        angles = (self.start_angle + n * self.end_angle * self.major_div / self.absolute for n in range(lines))
        textvals = (self.start + n * self.major_div * self.direction for n in range(lines))
        
        for angle, textval in zip(angles, textvals):
            x1 = self.xn + (self.radians - self.arc_pos) * math.cos(math.radians(angle))
            y1 = self.yn - (self.radians - self.arc_pos) * math.sin(math.radians(angle))
            x2 = x1 + (self.arc_pos + self.div_width)/ 3 * math.cos(math.radians(angle))
            y2 = y1 - (self.arc_pos + self.div_width)/ 3 * math.sin(math.radians(angle))
            self.create_line(x1, y1, x2, y2, width=self.border_width, tags='major_scale', fill=self.border_color)
                        
        # scale arc
        x1 = y1 = self.arc_pos
        x2 = y2 = self.radius - self.arc_pos 
        x3 = y3 = self.radius - self.arc_pos + (self.arc_pos + self.div_width)/ 3
        x4 = y4 = self.arc_pos - (self.arc_pos + self.div_width)/3

        self.create_oval(x1, y1, x2, y2, width=2, tags='arc', outline=self.border_color, fill=self.fg)
        
        if abs(self.end_angle) != 360:
            self.create_arc(x3, y3, x4, y4, start=self.start_angle, extent=self.end_angle, width=self.border_width-1,
                            outline=self.border_color, style='arc', tags='arc')
        else:
            self.create_oval(x3, y3, x4, y4, width=self.border_width-1, tags='arc', outline=self.border_color)
            
    def create_needle(self):
        """
        This function creates the needle and axis that can rotate.
        """
        x1 = self.xn
        y1 = self.yn + self.arc_pos * 4 / 3
        if self.text:
            self.create_text(x1, y1, font=self.text_font, tags='text')

        x1 = y1 = self.arc_pos+(self.arc_pos/2)
        x2 = y2 = self.arc_pos*2.5
        
        self.knob = self.create_oval(x1,y1,x2,y2, width=self.border_width-1, tags='needle', fill=self.button_color, outline=self.border_color)
        
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
            if self.max>self.start and self.start_angle>self.end_angle:
                self.set(self.value+self.scroll_steps)
            elif self.max<self.start and self.start_angle<self.end_angle:
                self.set(self.value+self.scroll_steps)
            else:
                self.set(self.value-self.scroll_steps)
        else:
            if self.max>self.start and self.start_angle>self.end_angle:
                self.set(self.value-self.scroll_steps)
            elif self.max<self.start and self.start_angle<self.end_angle:
                self.set(self.value-self.scroll_steps)
            else:
               self.set(self.value+self.scroll_steps)
                
        self.previous_angle = angle         


    def line_coordinates(self, r1: float, r2: float, angle: float) -> tuple:
        
        return (
            self.xn + r2 * math.cos(math.radians(angle)) -self.bt_radius,
            self.yn - r2 * math.sin(math.radians(angle)) -self.bt_radius,
            self.xn + r2 * math.cos(math.radians(angle)) +self.bt_radius,
            self.yn - r2 * math.sin(math.radians(angle)) +self.bt_radius
        )
    
    def set(self, value):
        """
        This function is used to set the position of the needle
        """
        
        self.value = value
        angle = (value - self.start) * (self.end - self.start_angle) / (self.max - self.start) + self.start_angle

        if self.start < self.max:  
            if value < self.start:
                self.value = self.start
                value = self.start
            elif value > self.max:
                self.value = self.max
                value = self.max
        else:
            if value > self.start:
                self.value = self.start
                value = self.start
            elif value < self.max:
                self.value = self.max
                value = self.max

        if self.progress:
            extend_angle = angle-(self.start_angle+self.end_angle)
            self.itemconfigure(self.arc_id, extent=extend_angle)
            
        self.coords(
            self.knob,
            self.line_coordinates(
                r1=0,
                r2= self.radius/2 - self.arc_pos - self.bt_radius,
                angle=angle
            )
        )
        
        if self.integer==False:
            value = round(value, 2)
        else:
            value = int(value)
            
        if self.text:
            self.itemconfig(tagOrId='text', text=self.text+str(value), fill=self.text_color)
        
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
        if from_==0: from_=1
        colored_lines = self.find_withtag('min_scale')[from_:to]
        for line in colored_lines:
            self.itemconfig(line, fill=color, width=10)
            
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
                tagOrId="progress",
                outline=kwargs.pop("scale_color"))
            
        if "fg" in kwargs:
            self.itemconfigure(
                tagOrId="face",
                fill=kwargs.pop('fg'))
            
        if "text_color" in kwargs:
            self.itemconfigure(
                tagOrId="text",
                fill=kwargs.pop("text_color"))
            
        if "button_color" in kwargs:
            self.itemconfigure(
                tagOrId="needle",
                fill=kwargs.pop("button_color"))
            
        if "border_color" in kwargs:
            self.itemconfigure(
                tagOrId="face",
                outline=kwargs.pop("border_color"))
            
        if "scroll_steps" in kwargs:
            self.scroll_steps = kwargs.pop("scroll_steps")
            
        if "scroll" in kwargs:
            if kwargs["scroll"]==False:
                super().unbind('<MouseWheel>')
                super().unbind('<Button-4>')
                super().unbind('<Button-5>')
            else:
                super().bind('<MouseWheel>', self.scroll_command)
                super().bind("<Button-4>", lambda e: self.scroll_command(-1))
                super().bind("<Button-5>", lambda e: self.scroll_command(1))
            kwargs.pop("scroll")
            
        if "integer" in kwargs:
            self.set(self.value)
            self.integer = kwargs.pop("integer")
            
        if "state" in kwargs:
            self.state = kwargs.pop("state")
            self.needle_state()
            
        if len(kwargs)>0:
            raise ValueError("unknown option: " + list(kwargs.keys())[0])
