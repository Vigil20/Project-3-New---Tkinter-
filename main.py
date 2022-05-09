import tkinter as tk

#functionality
def convert():
  meter = measurementMenu.get()
  Enter = entry.get()
  Ent = float(Enter)
  if meter == "Inches":
      conversionNumber=Ent *0.0833333
  elif meter =="Meters" :
    conversionNumber = Ent *0.3048
  elif meter =="Kilometers":
    conversionNumber = Ent * 127.660
  meterLabel.configure(text="{} Feet is equivalent to {} {}".format(Ent, conversionNumber,meter))
# Layout 
window = tk.Tk()
window.title("Measurement Converter")
window.geometry("400x200")

feetLabel = tk.Label(text="Feet")
feetLabel.pack()
feetLabel.place(x=250, y=60)

meterLabel = tk.Label(text="feet is equivalent to ")
meterLabel.pack()
meterLabel.place(x=50, y= 100)


entry = tk.Entry(window)
entry.pack()
entry.place(x = 145, y = 50, height = 30, width = 100)

calculateButton = tk.Button(text ="calculate", command = convert)
calculateButton.pack()
calculateButton.place(x=250, y=150)
 #dropdown menu 
measurementList = ["Inches","Meters","Kilometers"]
measurementMenu = tk.StringVar(window)
measurementMenu.set(measurementList[0])

options = tk.OptionMenu(window, measurementMenu, *measurementList)
options.pack()
options.place(x= 295, y=50)