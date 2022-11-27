###################--------------TkDial--------------###################

import tkinter as tk
from math import cos, sin, atan2, radians, degrees
from colour import Color

class Dial(tk.Canvas):

    def __init__(
            self,
            master,
            start: float = 0,
            end: float = 100,
            width: int = None,
            height: int = None,
            x: int = None,
            y: int = None,
            unit_length: float = 10,
            unit_width: float = 5,
            radius: float = 50.0,
            bg: str = "#f0f0f0",
            text: str = "Value: ",
            unit_color: str = "grey",
            text_color: str = "black",
            text_font: str = None,
            needle_color: str = "grey",
            color_gradient: tuple = None,
            integer: bool = False,
            scroll: bool = True,
            scroll_steps: int = 1,
            state: str = "normal",
            command=None
        ):
        
        self.__master = master
        
        if color_gradient is None:
            self.__color_gradient = ("white", "black")
        else:
            self.__color_gradient = color_gradient
            
        if width is None:
            self.__width = (unit_length + radius)*2
        else:
            self.__width = width
        
        if height is None:
            self.__height = (unit_length + radius)*2 + 20
        else:
            self.__height = height

        if x is None:
            self.__x = unit_length + radius
        else:
            self.__x = x
            
        if y is None:        
            self.__y =  unit_length + radius
        else:
            self.__y = y
                   
        if text=="":
            self.__height = self.__height - 20
        
        self.__bg = bg
        self.__needle_color = needle_color
        self.__text_title = text
        self.__unit_color = unit_color
        self.__text_color = text_color
        self.__radius = radius
        self.__unit_length = unit_length
        self.__unit_width = unit_width
        self.__start = start
        self.__text_font = text_font
        self.__end = end
        self.__integer = integer
        self.__command = command
        self.value = self.__start
        self.__status = True
        self.__state = state
        self.__scroll_steps = scroll_steps
        #Some standard color combinations
        self.__color_map = {
            ("yellow", "red"): (255, 1, 0, False),
            ("yellow", "green"): (1, 255, 0, False),
            ("pink", "blue"): (1, 0, 255, False),
            ("pink", "red"): (255, 0, 1, False),        
            ("cyan", "green"): (0, 255, 1, False),
            ("cyan", "blue"): (0, 1, 255, False),        
            ("red", "yellow"): (255, 1, 0, True),
            ("red", "pink"): (255, 0, 1, True),          
            ("blue", "cyan"): (0, 1, 255, True),
            ("blue", "pink"): (1, 0, 255, True),          
            ("green", "yellow"): (1, 255, 0, True),
            ("green", "cyan"): (0, 255, 1, True),
            
            ("white", "white"): (255, 255, 255, False),
            ("white", "red"): (255, 1, 1, False),
            ("white", "green"): (1, 255, 1, False),
            ("white", "blue"): (1, 1, 255, False),
            ("red", "white"): (255, 1, 1, True),
            ("green", "white"): (1, 255, 1, True),
            ("blue", "white"): (1, 1, 255, True),
            ("yellow", "white"): (255, 255, 1, True),
            ("pink", "white"): (255, 1, 255, True),
            ("cyan", "white"): (1, 255, 255, True),
            ("white", "yellow"): (255, 255, 1, False),
            ("white", "pink"): (255, 1, 255, False),
            ("white", "cyan"): (1, 255, 255, False),
            
            ("black","black"): (0, 0, 0, False),
            ("black", "red"): (1, 0, 0, True),
            ("black", "green"): (0, 1, 0, True),
            ("black", "blue"): (0, 0, 1, True),
            ("red", "black"): (1, 0, 0, False),
            ("green", "black"): (0, 1, 0, False),
            ("blue", "black"): (0, 0, 1, False),
            ("yellow", "black"): (1, 1, 0, False),
            ("pink", "black"): (1, 0, 1, False),
            ("cyan", "black"): (0, 1, 1, False),
            ("black", "yellow"): (1, 1, 0, True),
            ("black", "pink"): (1, 0, 1, True),
            ("black", "cyan"): (0, 1, 1, True),

            ("white", "black"): (1,1,1, False),
            ("black", "white"): (1,1,1, True),
            ("red", "red"):(255, 0, 0, True),
            ("green", "green"): (0, 255, 0, False),
            ("blue", "blue"): (0, 0, 255, False),
            ("cyan", "cyan"):(0, 255, 255, True),
            ("pink", "pink"): (255, 0, 255, False),
            ("yellow", "yellow"): (255, 255, 0, False)
        }
        
        super().__init__(self.__master, bg=self.__bg, width=self.__width, height=self.__height, bd=0, highlightthickness=0)
        self.__palette = self.__create_palette()
        self.__create_needle()
        self.__create_units()
        self.__create_text()
        
        if scroll==True:
            super().bind('<MouseWheel>', self.scroll_command)
        
    def scroll_command(self, event):
        """
        This function is used to change the value of the dial with mouse scroll
        """
        if event.delta > 0:        
            if self.value < self.__end:
                self.set(self.value+self.__scroll_steps)
        else:
            if self.value > self.__start:
                self.set(self.value-self.__scroll_steps)
            elif  self.value==self.__start:
                self.set(self.__start+0.1)
                self.set(self.__start)
                
    def __line_coordinates(self, r1: float, r2: float, angle: float) -> tuple:
        """
        This function is used for placing the lines around a circle.
        :return: A tuple that contains 4 coordinates
        """
        return (
            self.__x + r1 * cos(radians(angle)),
            self.__y - r1 * sin(radians(angle)),
            self.__x + r2 * cos(radians(angle)),
            self.__y - r2 * sin(radians(angle))
        )
    
    @staticmethod
    def __rgb(r: int, g: int, b: int) -> str:
        """
        This function is used to create different colors.
        :return: A string that contains the rgb color code
        """
        return "#" + "".join(hex(i)[2:].zfill(2) for i in (r, g, b))

    @staticmethod
    def __select_color(color: int, index: int, reverse: bool = False) -> int:
        """
        This function is for determining which colors will be selected
        according to the color gradient.
        :return: An integer for the color number of a single unit line.
        """
        color_number = index * 255 // 36
        if not reverse:
            color_number = 255 - color_number
        return color if color in [0, 255] else color_number
    
    def __create_palette(self) -> dict:
        """
        This function creates the color palette for
        each unit line. There are totally 36 unit lines
        and each unit line has a special tag and color.
        :return: A dictionary that contains the unit line tags and colors
        """
        unit_color = {}
        
        if self.__color_gradient in self.__color_map:
            r, g, b, reverse = self.__color_map[self.__color_gradient]

            for index, i in enumerate(range(360, -1, -10)):
                unit_color[f"unit{i}"] = self.__rgb(
                    r=self.__select_color(
                        color=r,
                        index=index,
                        reverse=reverse
                    ),
                    g=self.__select_color(
                        color=g,
                        index=index,
                        reverse=reverse
                    ),
                    b=self.__select_color(
                        color=b,
                        index=index,
                        reverse=reverse
                    )
                )
        else:
            colors = list(Color(self.__color_gradient[0]).range_to(Color(self.__color_gradient[1]),37))
            x=0
            
            for index, i in enumerate(range(360, -1, -10)):
                unit_color[f"unit{i}"] = colors[x]
                x+=1

        return unit_color
    
    def __create_units(self) -> None:
        """
        This function creates the unit lines.
        """
        for i in range(0, 360, 10):
            self.unit1=self.create_line(
                self.__line_coordinates(
                    r1=self.__radius,
                    r2=(self.__radius + self.__unit_length),
                    angle=i
                ),
                width=self.__unit_width,
                tag=f"unit{i}",
                fill=self.__unit_color
            )

    def __create_needle(self) -> None:
        """
        This function creates the needle that can rotate.
        """
        self.create_line(
            self.__line_coordinates(
                r1=0,
                r2=self.__radius,
                angle=0
            ),
            fill=self.__needle_color,
            width=self.__unit_width,
            state=self.__state,
            tag="needle"
        )
        self.tag_bind(
            tagOrId="needle",
            sequence="<ButtonPress-1>",
            func=lambda event: self.tag_bind(
                tagOrId="needle",
                sequence="<Motion>",
                func=self.__rotate_needle
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

    def __colorize(
            self,
            angle: float,
            start: int,
            end: int,
            color=""
    ) -> None:
        """
        This function changes the colors of the unit lines. The function
        is called first to change the colors of unit lines according to the
        selected color gradient, and second to change the colors of unit
        lines back to their original states.
        """
        if int(angle) == 0:
            pass
        elif int(angle) == 1:
            if color != self.__unit_color:
                color = self.__palette["unit0"]
            self.itemconfig(tagOrId="unit0", fill=color)
        else:
            for i in range(start, end):
                if i != 0 and i % 10 == 0:
                    if color != self.__unit_color:
                        color = self.__palette[f"unit{i}"]
                    self.itemconfig(tagOrId=f"unit{i}", fill=color)

    def __rotate_needle(self, event, angle=None) -> None:
        """
        This function rotates the needle, calls the colorizing function and
        changes the value of the text.
        """
        if angle==None:        
            angle = degrees(atan2(self.__y - event.y, event.x - self.__x))
            if angle < 0:
                angle += 360
            
            if (
                angle < 90 and self.__status
                or
                angle > 270 and not self.__status
                ):
                angle = 0
        else:
            angle = angle
            if angle < 0:
                angle += 360
                
        if 0 < angle < 180:
            self.__status = False
            
        elif 180 < angle < 360:
            self.__status = True
            
        if self.__integer==False:
            self.value = round(
                (self.__end - self.__start) / 360 * (360 - angle) + self.__start,
                2
            )
        else:
            self.value = int(round(
                (self.__end - self.__start) / 360 * (360 - angle) + self.__start,
                0
            ))
        if self.value == self.__end and self.__status:
            self.value = self.__start
        self.coords(
            "needle",
            self.__line_coordinates(
                r1=0,
                r2=self.__radius,
                angle=angle
            )
        )
        self.__colorize(angle=angle, start=int(angle), end=360)
        self.__colorize(
            angle=angle,
            start=0,
            end=int(angle),
            color=self.__unit_color
        )
        if self.__integer==False:
            self.itemconfigure(
                tagOrId="value",
                text=f"{self.__text_title}{self.value}"
            )
        else:
            self.itemconfigure(
                tagOrId="value",
                text=f"{self.__text_title}{int(self.value)}"
            )
        if self.__command is not None:
            self.__command()
            
    def __create_text(self) -> None:
        """
        A function that creates a text object to show what
        the value of the position of needle is.
        """
        self.create_text(
            self.__x,
            self.__y + self.__unit_length + self.__radius + 10, fill=self.__text_color,
            text=f"{self.__text_title}{int(self.value)}",
            font=self.__text_font,
            tag="value"
        )
        
    def get(self):
        """
        This function returns the current value of the dial
        :return: float
        """
        return self.value
    
    def set(self, value):
        """
        This function is used to set the position of the needle
        """
        if value<self.__start:
            value = self.__start
            
        if value>=self.__end:
            value = self.__end
            self.__rotate_needle(self, angle=-350)
            
        angle = float(-(360/(self.__end - self.__start))*(value - self.__start))
        self.__rotate_needle(self, angle=angle)

    def configure(self, **kwargs):
        """
        This function contains some configurable options
        """
        if "state" in kwargs:
            self.itemconfigure(
                tagOrId="needle",
                state=kwargs.pop("state"))
            
        if "text" in kwargs:
             self.itemconfigure(
                tagOrId="value",
                text=kwargs.pop("text"))
             
        if "start" in kwargs:
            self.__start = kwargs.pop("start")
            
        if "end" in kwargs:
            self.__end = kwargs.pop("end")
            
        if "bg" in kwargs:
            super().configure(bg=kwargs.pop("bg"))
            
        if "width" in kwargs:
            super().configure(width=kwargs.pop("width"))
            
        if "height" in kwargs:
            super().configure(height=kwargs.pop("height"))
            
        if "unit_color" in kwargs:
            self.__unit_color = kwargs.pop("unit_color")
            self.set(self.value+0.1)
            self.set(self.value)
            
        if "color_gradient" in kwargs:
            self.__color_gradient = kwargs.pop("color_gradient")
            self.__palette = self.__create_palette()
            self.set(self.value)
            
        if "text_color" in kwargs:
            self.itemconfigure(
                tagOrId="value",
                fill=kwargs.pop("text_color"))
            
        if "needle_color" in kwargs:
            self.itemconfigure(
                tagOrId="needle",
                fill=kwargs.pop("needle_color"))
            
        if "scroll_steps" in kwargs:
            self.__scroll_steps = kwargs.pop("scroll_steps")
            
        if "scroll" in kwargs:
            if kwargs["scroll"]==False:
                super().unbind('<MouseWheel>')
            else:
                super().bind('<MouseWheel>', self.scroll_command)
            kwargs.pop("scroll")
            
        if "integer" in kwargs:
            self.set(self.value)
            self.__integer = kwargs.pop("integer")
            
        if len(kwargs)>0:
            raise ValueError("unknown option: " + list(kwargs.keys())[0])
