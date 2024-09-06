import tkinter as tk
from PIL import Image, ImageTk
import time
import threading

class RainbowCursorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rainbow Mouse Cursor Settings")
        self.root.geometry("400x300")

        # Default values
        self.is_rainbow_active = False
        self.speed = 200  # milliseconds
        self.cursor_images = []
        self.load_images()

        # Creating the GUI components
        self.create_gui()

        # Thread to update the cursor
        self.cursor_thread = threading.Thread(target=self.change_cursor)
        self.cursor_thread.daemon = True
        self.cursor_thread.start()

    def load_images(self):
        """Load your rainbow cursor images."""
        for i in range(7):
            img = Image.open(f"rainbow_cursor_{i}.png")  # Create images like rainbow_cursor_0.png, etc.
            self.cursor_images.append(ImageTk.PhotoImage(img))

    def create_gui(self):
        """Create GUI components to control settings."""
        # Speed label and slider
        speed_label = tk.Label(self.root, text="Rainbow Speed (ms)")
        speed_label.pack(pady=10)
        
        self.speed_slider = tk.Scale(self.root, from_=50, to=1000, orient=tk.HORIZONTAL)
        self.speed_slider.set(self.speed)
        self.speed_slider.pack(pady=5)

        # Toggle rainbow effect button
        self.toggle_button = tk.Button(self.root, text="Start Rainbow Effect", command=self.toggle_rainbow)
        self.toggle_button.pack(pady=10)

        # Reset button
        reset_button = tk.Button(self.root, text="Reset to Default", command=self.reset_settings)
        reset_button.pack(pady=10)

    def toggle_rainbow(self):
        """Toggle the rainbow cursor effect on and off."""
        self.is_rainbow_active = not self.is_rainbow_active
        if self.is_rainbow_active:
            self.toggle_button.config(text="Stop Rainbow Effect")
        else:
            self.toggle_button.config(text="Start Rainbow Effect")

    def reset_settings(self):
        """Reset speed and rainbow effect to default values."""
        self.speed_slider.set(200)  # Reset speed to default
        self.is_rainbow_active = False
        self.toggle_button.config(text="Start Rainbow Effect")

    def change_cursor(self):
        """Change the cursor periodically based on the settings."""
        while True:
            if self.is_rainbow_active:
                for img in self.cursor_images:
                    self.root.config(cursor=f"@{img}")
                    time.sleep(self.speed_slider.get() / 1000)
            else:
                self.root.config(cursor="")  # Set cursor to default when rainbow is off
            time.sleep(0.1)

# Create the main application window
root = tk.Tk()
app = RainbowCursorApp(root)
root.mainloop()
