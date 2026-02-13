#!/usr/bin/env python3
"""
Calculator - A simple GUI calculator built with tkinter
Author: 凯总
"""

import tkinter as tk
from tkinter import ttk
import math


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("计算器")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Current expression
        self.current = ""
        self.display_text = tk.StringVar()
        self.display_text.set("0")
        
        # Create UI
        self.create_display()
        self.create_buttons()
        
        # Bind keyboard events
        self.root.bind('<Key>', self.on_key_press)
        self.root.bind('<Return>', lambda e: self.calculate())
        self.root.bind('<Escape>', lambda e: self.clear())
        
    def create_display(self):
        """Create the display area"""
        display_frame = ttk.Frame(self.root, padding="10")
        display_frame.pack(fill=tk.X)
        
        display = ttk.Entry(
            display_frame,
            textvariable=self.display_text,
            font=('Arial', 24),
            justify='right',
            state='readonly'
        )
        display.pack(fill=tk.X)
        
    def create_buttons(self):
        """Create calculator buttons"""
        button_frame = ttk.Frame(self.root, padding="10")
        button_frame.pack(fill=tk.BOTH, expand=True)
        
        # Button layout
        buttons = [
            ['C', '±', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]
        
        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                if btn_text == '0':
                    # Zero button spans two columns
                    btn = ttk.Button(
                        button_frame,
                        text=btn_text,
                        command=lambda t=btn_text: self.on_button_click(t)
                    )
                    btn.grid(row=i, column=j, columnspan=2, sticky='nsew', padx=2, pady=2)
                elif btn_text == '=':
                    btn = ttk.Button(
                        button_frame,
                        text=btn_text,
                        command=self.calculate
                    )
                    btn.grid(row=i, column=j+1, sticky='nsew', padx=2, pady=2)
                elif btn_text == '.':
                    btn = ttk.Button(
                        button_frame,
                        text=btn_text,
                        command=lambda t=btn_text: self.on_button_click(t)
                    )
                    btn.grid(row=i, column=j, sticky='nsew', padx=2, pady=2)
                else:
                    btn = ttk.Button(
                        button_frame,
                        text=btn_text,
                        command=lambda t=btn_text: self.on_button_click(t)
                    )
                    btn.grid(row=i, column=j, sticky='nsew', padx=2, pady=2)
                    
        # Configure grid weights
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.grid_columnconfigure(j, weight=1)
            
    def on_button_click(self, char):
        """Handle button clicks"""
        if char == 'C':
            self.clear()
        elif char == '±':
            self.toggle_sign()
        elif char == '%':
            self.percentage()
        elif char in ['÷', '×']:
            # Convert display symbols to Python operators
            op = '/' if char == '÷' else '*'
            self.current += op
            self.update_display()
        else:
            self.current += char
            self.update_display()
            
    def on_key_press(self, event):
        """Handle keyboard input"""
        key = event.char
        if key.isdigit() or key in '+-*/.':
            self.current += key
            self.update_display()
        elif key == '\r':  # Enter key
            self.calculate()
        elif key == '\x08':  # Backspace
            self.current = self.current[:-1]
            self.update_display()
            
    def calculate(self):
        """Calculate the result"""
        try:
            if self.current:
                result = eval(self.current)
                self.current = str(result)
                self.update_display()
        except Exception as e:
            self.display_text.set("错误")
            self.current = ""
            
    def clear(self):
        """Clear the display"""
        self.current = ""
        self.display_text.set("0")
        
    def toggle_sign(self):
        """Toggle positive/negative sign"""
        try:
            if self.current:
                value = float(self.current)
                value = -value
                self.current = str(value)
                # Remove trailing .0 if it's an integer
                if self.current.endswith('.0'):
                    self.current = self.current[:-2]
                self.update_display()
        except:
            pass
            
    def percentage(self):
        """Convert to percentage"""
        try:
            if self.current:
                value = float(self.current)
                value = value / 100
                self.current = str(value)
                if self.current.endswith('.0'):
                    self.current = self.current[:-2]
                self.update_display()
        except:
            pass
            
    def update_display(self):
        """Update the display"""
        if self.current:
            # Show current expression
            display = self.current
            # Replace operators with display symbols
            display = display.replace('*', '×').replace('/', '÷')
            self.display_text.set(display)
        else:
            self.display_text.set("0")


def main():
    root = tk.Tk()
    
    # Set style
    style = ttk.Style()
    style.configure('TButton', font=('Arial', 14), padding=10)
    
    app = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
