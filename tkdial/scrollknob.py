###################--------------TkDial-ScrollKnob--------------###################

import tkinter as tk

class ScrollKnob(tk.Canvas):
    
    def __init__(self,
                 master,
                 start: float = 0,
                 end: float = 100,
                 radius: int = 200,
                 width: int = None,
                 height: int = None,
                 start_angle: int = 0,
                 text: str = "%",
                 border_width: int = 40, 
                 text_color: str = "black",
                 text_font: str = None,
                 progress_color: str = "grey60",
                 inner_color: str = "grey80",
                 outer_color: str = "grey80",
                 inner_width: int = 10,
                 outer_width: int = 10,
                 outer_length: int = 0,
                 bg: str = "#f0f0f0",
                 fg: str = "#f0f0f0",
                 bar_color: str = "#f0f0f0",
                 integer: bool = False,
                 steps: int = 5,
                 state: str = "normal",
                 command = None
                 ):
        
        self.__master = master
        
        if width is None:
            width = radius 
        else:
            width = width
        
        if height is None:
            height = radius 
        else:
            height = height
            
        self.disable_text = False
        self.x0 = border_width 
        self.y0 = border_width 
        self.x1 = width-border_width 
        self.start = end
        self.bg = bg
        self.fg = fg
        self.bar_color = bar_color
        self.end = start
        self.y1 = height-border_width
        self.tx, self.ty = width / 2, height / 2
        self.width = border_width - outer_length
        self.inner = inner_width
        self.outer_length = outer_length
        self.outer = outer_width
        self.incolor = inner_color
        self.outcolor = outer_color
        self.text = text
        self.text_color = text_color
        self.text_font = text_font
        self.start_ang, self.full_extent = start_angle, 360
        self.steps = (steps/self.start-self.end)*360
        self.progress_color = progress_color
        self.delta = 0
        w2 = self.width / 2
        self.value = self.start
        self.state = state
        self.integer = integer
        self.command = command
        
        super().__init__(self.__master, bg=self.bg, width=width, height=height, bd=0, highlightthickness=0)
        
        if self.inner > self.x0:
            self.inner = self.x0
        if self.outer > self.y0:
            self.outer = self.y0
        if text=="":
            self.disable_text = True          
        if self.steps > (self.start-self.end):
            self.steps = self.start - self.end
            
        self.arc_back = self.create_arc(self.x0, self.y0, self.x1, self.y1, extent=359,
                                             start=self.start_ang, outline=self.bar_color,
                                             width=self.width, style='arc')
        
        self.arc_id = self.create_arc(self.x0, self.y0, self.x1, self.y1, extent=0,
                                        start=self.start_ang, outline=self.progress_color,
                                        width=self.width, style='arc')
        
        self.oval_id1 = self.create_oval(self.x0-w2-self.outer_length, self.y0-w2-self.outer_length, self.x1+w2+self.outer_length, self.y1+w2+self.outer_length, outline=self.outcolor,width=self.outer)
        
        self.oval_id2 = self.create_oval(self.x0+w2, self.y0+w2, self.x1-w2, self.y1-w2, width=self.inner, outline=self.incolor, fill=self.fg)
        
        self.label_id = self.create_text(self.tx, self.ty, fill=self.text_color, font=self.text_font)        
        self.set_text()
        
        if state=="normal":
            self.bind('<MouseWheel>', self.scroll_command)
        
    def scroll_command(self, event):
        """
        This function is used to change the value of the knob with mouse scroll
        """
        if event.delta > 0:
            if self.delta>=(360-self.steps):
                self.itemconfigure(self.arc_id, extent=359)
                self.delta=360
            else:
                self.delta+=self.steps
                self.itemconfigure(self.arc_id, extent=self.delta)
        else:
            if self.delta<=(0+self.steps):
                self.itemconfigure(self.arc_id, extent=0)
                self.delta = 0
            else:
                self.delta-=self.steps
                self.itemconfigure(self.arc_id, extent=self.delta)

        self.set_text()
        
        if self.command is not None:
            self.command()
            
    def set_text(self):
        """
        This function is to set text for the knob
        """
        if self.disable_text==False:
            if self.integer==True:
                self.value = int(round((self.end - self.start) / 360 * (360 - self.delta) + self.start, 2))
            else:
                self.value = round((self.end - self.start) / 360 * (360 - self.delta) + self.start, 2)
            self.itemconfigure(self.label_id, text=str(self.value) + self.text)
        else:
            self.itemconfigure(self.label_id, text="")
            
    def get(self):
        """
        This function returns the current value of the dial
        :return: float/int
        """
        return self.value
    
    def set(self, value):
        """
        This function is used to set the position of the needle
        """
        
        if value<self.end:
            value = self.end
            
        if value>=self.start:
            value = self.start

        self.delta = 360-(360/(self.end - self.start))*(value - self.start)
        self.itemconfigure(self.arc_id, extent=self.delta)
        self.set_text()
        
        if self.command is not None:
            self.command()
            
    def configure(self, **kwargs):
        """
        This function contains some configurable options
        """
        if "state" in kwargs:
            if kwargs["scroll"]!="normal":
                super().unbind('<MouseWheel>')
            else:
                super().bind('<MouseWheel>', self.scroll_command)
            
        if "text" in kwargs:
             self.itemconfigure(self.label_id,
                text=kwargs.pop("text"))
             
        if "start" in kwargs:
            self.end = kwargs.pop("start")
            
        if "end" in kwargs:
            self.start = kwargs.pop("end")
            
        if "bg" in kwargs:
            super().configure(bg=kwargs.pop("bg"))
            
        if "width" in kwargs:
            super().configure(width=kwargs.pop("width"))
            
        if "height" in kwargs:
            super().configure(height=kwargs.pop("height"))
            
        if "bar_color" in kwargs:
            self.itemconfigure(self.arc_back,
                outline=kwargs.pop("bar_color"))
            
        if "progress_color" in kwargs:
            self.itemconfigure(self.arc_id,
                outline=kwargs.pop("progress_color"))
            
        if "fg" in kwargs:
            self.itemconfigure(
                self.oval_id2,
                fill=kwargs.pop("fg"))
            
        if "inner_color" in kwargs:
            self.itemconfigure(
                self.oval_id2,
                outline=kwargs.pop("inner_color"))
            
        if "outer_color" in kwargs:
            self.itemconfigure(
                self.oval_id1,
                outline=kwargs.pop("outer_color"))
            
        if "steps" in kwargs:
            self.steps = (int(kwargs.pop("steps"))/self.start-self.end)*360

        if "text_color" in kwargs:
            self.itemconfigure(
                self.label_id,
                fill=kwargs.pop("text_color"))
            
        if "integer" in kwargs:
            
            self.integer = kwargs.pop("integer")
            self.set_text()
            
        if len(kwargs)>0:
            raise ValueError("unknown option: " + list(kwargs.keys())[0])
