import tkinter as tk
from tkinter import messagebox
import paho.mqtt.client as mqtt

# MQTT broker configuration
BROKER = "test.mosquitto.org"  # Public MQTT broker
PORT = 1883                     # Default MQTT port
client = mqtt.Client()           # Create an MQTT client instance

# Function to connect to MQTT broker
def connect_mqtt():
    try:
        client.connect(BROKER, PORT)  # Connect to the broker
        client.loop_start()            # Start the MQTT network loop
    except Exception as e:
        messagebox.showerror("Connection Error", str(e))  # Show error if connection fails

# Function to publish a tweet
def publish_tweet():
    # Get user inputs from entry fields
    username = username_entry.get().strip()
    tweet = tweet_entry.get().strip()
    hashtag = hashtag_entry.get().strip()

    # Validate inputs
    if not username or not tweet or not hashtag:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    # Format topic and message
    topic = f"twitter/{hashtag}"       # MQTT topic based on hashtag
    message = f"{username}: {tweet}"   # Message format for publishing

    client.publish(topic, message)     # Publish message to broker
    messagebox.showinfo("Success", f"Tweet published to #{hashtag}")
    tweet_entry.delete(0, tk.END)      # Clear tweet field after sending

# GUI setup
root = tk.Tk()
root.title("Tweet Publisher")

# Username label and input
tk.Label(root, text="Username:").grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

# Tweet message label and input
tk.Label(root, text="Tweet Message:").grid(row=1, column=0, padx=5, pady=5)
tweet_entry = tk.Entry(root, width=40)
tweet_entry.grid(row=1, column=1, padx=5, pady=5)

# Hashtag label and input
tk.Label(root, text="Hashtag:").grid(row=2, column=0, padx=5, pady=5)
hashtag_entry = tk.Entry(root)
hashtag_entry.grid(row=2, column=1, padx=5, pady=5)

# Publish button
publish_btn = tk.Button(root, text="Publish Tweet", command=publish_tweet)
publish_btn.grid(row=3, column=0, columnspan=2, pady=10)

# Connect to MQTT broker and start the GUI
connect_mqtt()
root.mainloop()
