import tkinter as tk

# Create the window
window = tk.Tk()
window.title('Window with Background Image')
window.geometry('400x300')

# Add a background image
background_image = tk.PhotoImage(file='back.png')
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Run the window
window.mainloop()




# Load the background image
background_image = tk.PhotoImage(file='back2.png')

# Tile the image to cover the canvas
for x in range(0, root.winfo_screenwidth(), background_image.width()):
    for y in range(0, root.winfo_screenheight(), background_image.height()):
        canvas.create_image(x, y, anchor='nw', image=background_image)