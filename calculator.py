from tkinter import Tk, Entry, Button, StringVar

class CalculatorApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Calculator")
        self.window.geometry("357x420+0+0")
        self.window.config(bg="gray")
        self.window.resizable(False, False)

        self.display_text = StringVar()
        self.current_expression = ""
        
        self.create_widgets()

    def create_widgets(self):
        screen = Entry(
            self.window, 
            width=17, 
            bg="#ffffff", 
            font=("Arial Bold", 28), 
            textvariable=self.display_text,
            justify="right"
        )
        screen.place(x=0, y=0)

        buttons = [
            ('(', 0, 50),  (')', 90, 50),  ('%', 180, 50),  ('/', 270, 50),
            ('1', 0, 125), ('2', 90, 125), ('3', 180, 125), ('*', 270, 125),
            ('4', 0, 200), ('5', 90, 200), ('6', 180, 200), ('-', 270, 200),
            ('7', 0, 275), ('8', 90, 275), ('9', 180, 275), ('+', 270, 275),
            ('C', 0, 350), ('0', 90, 350), ('.', 180, 350), ('=', 270, 350)
        ]

        for char, x, y in buttons:
            if char == 'C':
                btn = Button(self.window, text=char, width=11, height=4, relief="flat", command=self.clear_screen)
            elif char == '=':
                btn = Button(self.window, text=char, width=11, height=4, relief="flat", bg="orange", command=self.calculate_result)
            else:
                display_char = 'x' if char == '*' else char
                btn = Button(
                    self.window, 
                    text=display_char, 
                    width=11, 
                    height=4, 
                    relief="flat", 
                    bg="white", 
                    command=lambda val=char: self.append_character(val)
                )
            btn.place(x=x, y=y)

    def append_character(self, character):
        self.current_expression += str(character)
        self.display_text.set(self.current_expression)

    def clear_screen(self):
        self.current_expression = ""
        self.display_text.set("")

    def calculate_result(self):
        try:
            result = str(eval(self.current_expression))
            self.display_text.set(result)
            self.current_expression = result
        except Exception:
            self.display_text.set("Error")
            self.current_expression = ""

if __name__ == "__main__":
    main_window = Tk()
    app = CalculatorApp(main_window)
    main_window.mainloop()
