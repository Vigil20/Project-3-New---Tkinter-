import tkinter as tk

#functionality
# Layout 
window = tk.Tk()
window.title("Feet to Meters")
window.geometry("400x200")

feetLabel = tk.Label(text="Feet")
feetLabel.pack()
feetLabel.place(x=250, y=60)

meterLabel = tk.Label(text="distance")
meterLabel.pack()
meterLabel.place(x=250, y= 100)

sumLabel = tk.Label(text="is equivalent to")
sumLabel.pack()
sumLabel.place(x=100, y = 100)

entry = tk.Entry(window)
entry.pack()
entry.place(x = 145, y = 50, height = 30, width = 100)

calculateButton = tk.Button(text ="calculate")
calculateButton.pack()
calculateButton.place(x=250, y=150)
 #dropdown menu 
measurementList = ["inches", "Feet","meters","Kilometers"]
measurementMenu = tk.StringVar(window)
measurementMenu.set(measurementList[0])

options = tk.OptionMenu(window, measurementMenu, *measurementList)
options.pack()
options.place(x= 275, y=65)