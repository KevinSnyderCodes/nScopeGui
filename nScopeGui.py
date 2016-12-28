from Tkinter import *

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createPanels()

	def createPanels(self):
		self.INPUT_TEXT = Entry(self)
		self.INPUT_TEXT.bind("<Return>", self.updateInputSlider)
		self.INPUT_TEXT.grid(row=0, column=0, rowspan=4)

		self.INPUT_SLIDER = Scale(self)
		self.INPUT_SLIDER["from_"] = 100.0
		self.INPUT_SLIDER["to"] = 0.0
		self.INPUT_SLIDER.bind("<ButtonRelease-1>", self.updateInputText)
		self.INPUT_SLIDER.grid(row=0, column=1, rowspan=4)

		self.BUTTON_P1 = Button(self)
		self.BUTTON_P1["text"] = "P1"
		self.BUTTON_P1.bind("<Button-1>", self.togglePulse)
		self.BUTTON_P1.grid(row=0, column=2)

		self.BUTTON_P1_INDICATOR = Canvas(self, width=10, height=10, bg="white")
		self.BUTTON_P1_INDICATOR["highlightbackground"] = "#bdc3c7"
		self.BUTTON_P1_INDICATOR["highlightthickness"] = 1
		self.BUTTON_P1_INDICATOR.grid(row=0, column=3)

		self.BUTTON_P2 = Button(self)
		self.BUTTON_P2["text"] = "P2"
		self.BUTTON_P2.bind("<Button-1>", self.togglePulse)
		self.BUTTON_P2.grid(row=1, column=2)

		self.BUTTON_P2_INDICATOR = Canvas(self, width=10, height=10, bg="white")
		self.BUTTON_P2_INDICATOR["highlightbackground"] = "#bdc3c7"
		self.BUTTON_P2_INDICATOR["highlightthickness"] = 1
		self.BUTTON_P2_INDICATOR.grid(row=1, column=3)

		self.BUTTON_P3 = Button(self)
		self.BUTTON_P3["text"] = "P3"
		self.BUTTON_P3.bind("<Button-1>", self.togglePulse)
		self.BUTTON_P3.grid(row=2, column=2)

		self.BUTTON_P3_INDICATOR = Canvas(self, width=10, height=10, bg="white")
		self.BUTTON_P3_INDICATOR["highlightbackground"] = "#bdc3c7"
		self.BUTTON_P3_INDICATOR["highlightthickness"] = 1
		self.BUTTON_P3_INDICATOR.grid(row=2, column=3)

		self.BUTTON_P4 = Button(self)
		self.BUTTON_P4["text"] = "P4"
		self.BUTTON_P4.bind("<Button-1>", self.togglePulse)
		self.BUTTON_P4.grid(row=3, column=2)

		self.BUTTON_P4_INDICATOR = Canvas(self, width=10, height=10, bg="white")
		self.BUTTON_P4_INDICATOR["highlightbackground"] = "#bdc3c7"
		self.BUTTON_P4_INDICATOR["highlightthickness"] = 1
		self.BUTTON_P4_INDICATOR.grid(row=3, column=3)


	def updateInputText(self, event):
		value = self.INPUT_SLIDER.get()
		self.INPUT_TEXT.delete(0, END)
		self.INPUT_TEXT.insert(0, value)

	def updateInputSlider(self, event):
		value = self.INPUT_TEXT.get()
		self.INPUT_SLIDER.set(value)

	def togglePulse(self, event):
		origin = event.widget
		if origin == self.BUTTON_P1:
			indicator = self.BUTTON_P1_INDICATOR
		if origin == self.BUTTON_P2:
			indicator = self.BUTTON_P2_INDICATOR
		if origin == self.BUTTON_P3:
			indicator = self.BUTTON_P3_INDICATOR
		if origin == self.BUTTON_P4:
			indicator = self.BUTTON_P4_INDICATOR
		if indicator["bg"] == "white":
			indicator["bg"] = "#f1c40f"
		else:
			indicator["bg"] = "white"

	def say_hi(self):
		window = Toplevel(bg="red")

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()