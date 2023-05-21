###################--------------TkDial-ImageKnob--------------###################

import tkinter as tk
import math
from PIL import Image, ImageTk

class ImageKnob(tk.Canvas):

    def __init__(self,
                 master,
                 image: str = None,
                 scale_image: str = None,
                 scale_width: int = 0,
                 start: float = 0,
                 end: float = 100,
                 radius: int = 250,
                 width: int = None,
                 height: int = None,
                 text: str = " ",
                 text_color: str = "black",
                 text_font: str = None,
                 start_angle: int = 0,
                 end_angle: int = 360,
                 bg: str = None,
                 scroll: bool = True,
                 scroll_steps: float = 5,
                 integer: bool = False,
                 progress: bool = False,
                 progress_color: str = "white",
                 command=None):
        
        self.bg = bg
        self.radius = radius
        self.master = master
        self.text = text
        self.start_angle = start_angle 
        self.end_angle = end_angle
        self.start = start
        self.max = end
        self.end = self.start_angle + self.end_angle
        self.integer = integer
        self.text_color = text_color
        self.value = self.start  
        self.text_font = text_font
        self.scroll = scroll
        self.scroll_steps = scroll_steps
        self.command = command
        self.__x = radius/2
        self.__y = radius/2
        self.scale_width = scale_width
        self.knob_image = image
        self.scale_image = scale_image
        self.progress = progress
        self.progress_color = progress_color
        
        if not self.bg:
            try:
                if master.winfo_name().startswith("!ctkframe"):
                    # get bg_color of customtkinter frames
                    self.bg = master._apply_appearance_mode(master.cget("fg_color"))
                else:
                    self.bg = master.cget("bg")
            except:  
                self.bg = "white"
            
        if width is None:
            self.width = self.radius
        else:
            self.width = width
        
        if height is None:
            self.height = self.radius
        else:
            self.height = height
        
        super().__init__(master, width=self.width, height=self.height, bg=self.bg, borderwidth=0, highlightthickness=0)
        
        self.angle = self.start_angle
        
        if self.progress:
                self.arc()
                
        if scale_image:
            self.image2 = Image.open(self.scale_image).resize((self.radius, self.radius))
            self.update2 = self.draw_scale().__next__
            self.update2()
        else:
            if not self.scale_width:
                self.scale_width = 0

        if image:
            self.image = Image.open(self.knob_image).resize((self.radius-self.scale_width, self.radius-self.scale_width))
        else:
            raise AttributeError("Please pass a knob image using image='path_to_the_image.png' ")
            return
        
        self.draw_scale()
        self.update = self.draw().__next__
        self.update()
                
        if self.text:
            self.create_text(self.__x, self.radius-10, font=self.text_font, tags='text', text=self.text+str(self.start), fill=self.text_color)
            
        if self.scroll==True:
            super().bind('<MouseWheel>', self.scroll_command)
            super().bind("<Button-4>", lambda e: self.scroll_command(-1))
            super().bind("<Button-5>", lambda e: self.scroll_command(1))
            
    def draw(self):
        while True:
            tkimage = ImageTk.PhotoImage(self.image.rotate(self.angle))
            canvas_obj = self.create_image(
                self.__x, self.__y, image=tkimage)
            yield
            self.delete(canvas_obj)

    def draw_scale(self):
        tkimage2 = ImageTk.PhotoImage(self.image2)
        self.create_image(self.__x, self.__y, image=tkimage2)
        yield

    def arc(self):
        if self.start_angle>self.end_angle:
            add = 180+self.start_angle
        else:
            if self.end_angle-self.start_angle==360:
                add = 90+self.start_angle+self.end_angle
            else:
                add = self.start_angle+self.end_angle
                
        self.arc_id = self.create_arc((self.__x+self.radius/2.5), (self.__x+self.radius/2.5),
                                      (self.__x-self.radius/2.5), (self.__y-self.radius/2.5), extent=0,
                                        start=add, outline=self.progress_color,
                                        width=50, style='arc')
        
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

    def set(self, value):
        """
        This function is used to set the position of the needle
        """
        
        self.value = value
        self.angle = (value - self.start) * (self.end - self.start_angle) / (self.max - self.start) + self.start_angle

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

        self.master.after_idle(self.update)
        
        if self.integer==False:
            value = round(value, 2)
        else:
            value = int(value)

        if self.progress:
            if self.angle==360:
                extent = 358
            else:
                extent = self.angle
                
            self.itemconfigure(self.arc_id, extent=extent)
            
        if self.text:
            self.itemconfig(tagOrId='text', text=self.text+str(value), fill=self.text_color)
        
        if self.command is not None:
            self.command()
        
    def get(self):
        """
        This function returns the current value of the meter
        :return: float
        """
        return self.value
            
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
            
        if "text_color" in kwargs:
            self.itemconfigure(
                tagOrId="text",
                fill=kwargs.pop("text_color"))
            
        if "progress_color" in kwargs:
            self.itemconfigure(self.arc_id, outline=kwargs.pop("progress_color"))
            
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
        
        if len(kwargs)>0:
            raise ValueError("unknown option: " + list(kwargs.keys())[0])
