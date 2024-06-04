# main.py
import tkinter as tk
from PIL import Image, ImageTk
import requests
import json

try:
    # Create the main window
    root = tk.Tk()

    # Set the position of the window to the top left corner of the screen
    root.geometry("+0+0")

    # Load the GIF
    gif_path = r"C:\Users\colem\PycharmProjects\ai_chatbot\cute_girl.gif"  # replace with your GIF path
    gif_image = Image.open(gif_path)

    # Create a label to display the GIF
    gif_label = tk.Label(root)
    gif_label.pack()

    # Create a label to display the chatbot's responses
    response_label = tk.Label(root, width=50, height=10, wraplength=400, font=("TkDefaultFont", 20, "bold"))
    response_label.pack()

    # Create an entry box for typing messages
    entry_box = tk.Entry(root, width=50)
    entry_box.config(font=("TkDefaultFont", 20, "bold"))
    entry_box.pack(ipady=10)  # ipady parameter increases the height of the entry box

    # Set the chatbot's name
    chatbot_name = "Sasha"

    # Function to update the GIF frame
    def update(ind=0):
        frame = gif_image.seek(ind)
        photo = ImageTk.PhotoImage(gif_image)
        gif_label.configure(image=photo)
        gif_label.image = photo
        root.after(100, update, ind+1 if ind < gif_image.n_frames-1 else 0)

    # Function to handle chat messages
    def chat(event=None):
        # Get the message from the entry box
        message = entry_box.get()

        # Send the message to the chatbot and get the response
        try:
            response = requests.post('http://127.0.0.1:5000/chat', json={"message": message})
            response.raise_for_status()
            reply = response.json()["reply"]
        except requests.exceptions.RequestException as e:
            reply = "An error occurred: " + str(e)

        # Display the chatbot's response in the response label
        response_label.config(text=chatbot_name + ": " + reply)

        # Clear the entry box
        entry_box.delete(0, tk.END)

    # Bind the Enter key to the chat function
    entry_box.bind("<Return>", chat)

    # Start the GIF animation
    update()

    # Run the main loop
    root.mainloop()

except Exception as e:
    print("An error occurred: ", e)