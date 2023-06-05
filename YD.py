from pytube import YouTube
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def download_video():
    video_url = url_entry.get()

    try:
        # Create a YouTube object with the video URL
        video = YouTube(video_url)

        # Get the highest resolution available
        stream = video.streams.get_highest_resolution()

        # Prompt the user to select the download location
        save_path = filedialog.asksaveasfilename(defaultextension=".mp4")

        # Download the video to the selected location
        stream.download(output_path=save_path)
        messagebox.showinfo("Download Complete", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
window = tk.Tk()
window.title("YouTube Video Downloader")

# Create a label and an entry field for the video URL
url_label = tk.Label(window, text="YouTube Video URL:")
url_label.pack()
url_entry = tk.Entry(window, width=50)
url_entry.pack()

# Create a button to start the download
download_button = tk.Button(window, text="Download", command=download_video)
download_button.pack()

# Run the GUI event loop
window.mainloop()
