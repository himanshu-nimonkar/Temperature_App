
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
from functools import partial

# Global Variable Declaration
temperature = "Celsius"


# Setting the Drop Down Menu
def store_temp(temperature_setting):
    global temperature
    temperature = temperature_setting


# Temperature Conversion
def convert(label_1, label_2, label_3, label_4, inputting):
    temperature_main = inputting.get()

    if temperature == 'Celsius':

        # Converting Celsius Temperature
        fahrenheit = float((float(temperature_main) * 9.0 / 5.0) + 32.0)
        kelvin = float((float(temperature_main) + 273.15))
        rankine = float((float(temperature_main)*1.8)+32.0+459.67)
        remaur = float(float(temperature_main)*0.8)

        # Setting up the Primary Temperature Labels
        label_1.config(text="%.1f Fahrenheit" % fahrenheit)
        label_2.config(text="%f Kelvin" % kelvin)
        label_3.config(text="%f Rankine" % rankine)
        label_4.config(text="%f Rèmaur" % remaur)

        # Message Box indicating the Success of the Conversion
        messagebox.showinfo("Temperature Converter Himanshu", "Successfully Converted Celsius to Other Units")

    if temperature == 'Fahrenheit':

        # Converting Fahrenheit Temperature
        celsius = float((float(temperature_main) - 32.0) * 5.0 / 9.0)
        kelvin = float((float(temperature_main) + 459.67)/1.8)
        rankine = float(float(temperature_main)+459.67)
        remaur = float((float(temperature_main)-32.0)/2.25)

        # Setting up the Primary Temperature Labels
        label_1.config(text="%.1f Celsius" % celsius)
        label_2.config(text="%f Kelvin" % kelvin)
        label_3.config(text="%f Rankine" % rankine)
        label_4.config(text="%f Rèmaur" % remaur)

        # Message Box indicating the Success of the Conversion
        messagebox.showinfo("Temperature Converter Himanshu", "Successfully Converted Fahrenheit to Other Units")

    if temperature == 'Kelvin':

        # Converting Kelvin Temperature
        celsius = float((float(temperature_main) - 273.15))
        fahrenheit = float((float(temperature_main) - 273.15) * 1.8 + 32.0)
        rankine = float(float(temperature_main)*1.8)
        remaur = float((float(temperature_main)-273.15)*0.8)

        # Setting up the Primary Temperature Labels
        label_1.config(text="%f Celsius" % celsius)
        label_2.config(text="%f Fahrenheit" % fahrenheit)
        label_3.config(text="%f Rankine" % rankine)
        label_4.config(text="%f Rèmaur" % remaur)

        # Message Box indicating the Success of the Conversion
        messagebox.showinfo("Temperature Converter Himanshu", "Successfully Converted Kelvin to Other Units")

    if temperature == 'Rankine':

        # Converting Rankine Temperature
        celsius = float((float(temperature_main)-32-459.67)/1.8)
        fahrenheit = float((float(temperature_main)-459.67))
        kelvin = float(float(temperature_main)/1.8)
        remaur = float((float(temperature_main)-32-459.67)/2.25)

        # Setting up the Primary Temperature Labels
        label_1.config(text="%f Celsius" % celsius)
        label_2.config(text="%f Fahrenheit" % fahrenheit)
        label_3.config(text="%f Kelvin" % kelvin)
        label_4.config(text="%f Rèmaur" % remaur)

        # Message Box indicating the Success of the Conversion
        messagebox.showinfo("Temperature Converter Himanshu", "Successfully Converted Rankine to Other Units")

    if temperature == 'Rèmaur':

        # Converting Rèmaur Temperature
        celsius = float(float(temperature_main)*1.25)
        fahrenheit = float((float(temperature_main)*2.25)+32)
        kelvin = float((float(temperature_main)*1.25)+273.15)
        rankine = float((float(temperature_main)*2.25)+32+459.67)

        # Setting up the Primary Temperature Labels
        label_1.config(text="%f Celsius" % celsius)
        label_2.config(text="%f Fahrenheit" % fahrenheit)
        label_3.config(text="%f Kelvin" % kelvin)
        label_4.config(text="%f Rankine" % rankine)

        # Message Box indicating the Success of the Conversion
        messagebox.showinfo("Temperature Converter Himanshu", "Successfully Converted Rèmaur to Other Units ")

    return


# tk Window Creation
window = tk.Tk()

# Geometry of tk Window Setting
window.geometry('600x300+600+200')
window.resizable(width=True, height=True)

# Setting the Title
window.title('Temperature Converter Himanshu')

# Setting the window colour
window.configure(bg='powder blue')

# Laying out the widgets
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(1, weight=1)

get_Number = tk.StringVar()
variable = tk.StringVar()

# Setting the Font
Font = font.Font(family='Helvetica', weight='bold', slant='italic')


# The Labels and the Entry Field

# Setting the Information Label
label_get = tk.Label(window, text="Enter the Temperature:")

# Setting the Input Box
entry_get = tk.Entry(window, textvariable=get_Number)

# Enhancing the Input Box
label_get.grid(row=1)
entry_get.grid(row=1, column=1)

# Setting the First Label Temperature Value
label_final_1 = tk.Label(window)
label_final_1.grid(row=3, columnspan=10)

# Setting the Second Label Temperature Value
label_final_2 = tk.Label(window)
label_final_2.grid(row=4, columnspan=10)

# Setting the Third Label Temperature Value
label_final_3 = tk.Label(window)
label_final_3.grid(row=5, columnspan=10)

# Setting the Forth Label Temperature Value
label_final_4 = tk.Label(window)
label_final_4.grid(row=6, columnspan=10)

# Setting the colour of the Information Label
label_get.configure(fg='steel blue', bg='sky blue')

# Setting the Colour of the First, Second, Third, Forth Label giving the Temperature Value
label_final_1.configure(fg='steel blue', bg='powder blue')
label_final_2.configure(fg='steel blue', bg='powder blue')
label_final_3.configure(fg='steel blue', bg='powder blue')
label_final_4.configure(fg='steel blue', bg='powder blue')

# Setting the Colour of the Input Box
entry_get.configure(bg='sky blue', fg='steel blue')

# Setting up the Font of the Information Label
label_get['font'] = Font

# Setting the Font of the First, Second, Third, Forth Label giving the Temperature Value
label_final_1['font'] = Font
label_final_2['font'] = Font
label_final_3['font'] = Font
label_final_4['font'] = Font

# Setting the Font of the Input Box
entry_get['font'] = Font


# Setting Up the Drop down Menu

# Drop Down List of Units
list_drop_down = ["Celsius", "Fahrenheit", "Kelvin", "Rankine", "Rèmaur"]
actual_Drop_Down = tk.OptionMenu(window, variable, *list_drop_down, command=store_temp)
variable.set(list_drop_down[0])
actual_Drop_Down.grid(row=1, column=5)

# Setting the Colour of the Drop Down Menu
actual_Drop_Down.configure(fg='steel blue', bg='sky blue')

# Setting the Font of the Drop Down Menu
actual_Drop_Down['font'] = Font


# Setting Up the Final Convert Button Widget
conversion_calling = partial(convert, label_final_1, label_final_2, label_final_3, label_final_4, get_Number)
final_button_for_result = tk.Button(window, text="Convert", command=conversion_calling)
final_button_for_result.grid(row=2, columnspan=10)

# Setting the Colour of the Final Convert Button Widget
final_button_for_result.configure(fg='steel blue')

# Setting the Font of the of the Final Convert Button Widget
final_button_for_result['font'] = Font


# Setting up the Infinite Loop
window.mainloop()

# Making a Window
window_1 = tk.Tk()

# Hiding the Window
window_1.withdraw()

# Credits of the Code
messagebox.showinfo("Temperature Converter Himanshu", '''Thank You for Running my Code
Code written by : Himanshu Nimonkar
Roll Number : 16010420139
''')


# Printing the Credits of the Code
print('''Thank You for Running our Code
Code written by : Himanshu Nimonkar
Roll Number : 16010420139''')
