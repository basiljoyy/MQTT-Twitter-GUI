import tkinter as tk
from tkinter import messagebox, scrolledtext
import paho.mqtt.client as mqtt

# MQTT broker configuration
BROKER = "test.mosquitto.org"  # Public MQTT broker
PORT = 1883                     # Default MQTT port
client = mqtt.Client()           # Create MQTT client
subscribed_topics = []           # List to track subscribed hashtags

# Callback when connected to broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
    else:
        print("Connection failed")

# Callback when a message is received
def on_message(client, userdata, msg):
    # Display message in text area with hashtag
    tweet_area.insert(tk.END, f"[{msg.topic.split('/')[-1]}] {msg.payload.decode()}\n")
    tweet_area.yview(tk.END)  # Auto-scroll to newest message

# Assign callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to broker
client.connect(BROKER, PORT)
client.loop_start()  # Start background MQTT loop

# Function to subscribe to a hashtag
def subscribe_hashtag():
    hashtag = hashtag_entry.get().strip()  # Get input
    if not hashtag:
        messagebox.showwarning("Input Error", "Hashtag cannot be empty!")
        return

    topic = f"twitter/{hashtag}"  # Construct topic
    if topic not in subscribed_topics:
        client.subscribe(topic)          # Subscribe to broker topic
        subscribed_topics.append(topic)  # Track locally
        tweet_area.insert(tk.END, f"Subscribed to #{hashtag}\n")
    else:
        messagebox.showinfo("Info", f"Already subscribed to #{hashtag}")

# Function to unsubscribe from a hashtag
def unsubscribe_hashtag():
    hashtag = hashtag_entry.get().strip()
    topic = f"twitter/{hashtag}"
    if topic in subscribed_topics:
        client.unsubscribe(topic)        # Unsubscribe from broker topic
        subscribed_topics.remove(topic)  # Remove from local list
        tweet_area.insert(tk.END, f"Unsubscribed from #{hashtag}\n")
    else:
        messagebox.showinfo("Info", f"Not subscribed to #{hashtag}")

# GUI setup
root = tk.Tk()
root.title("Hashtag Subscriber")

# Hashtag input
tk.Label(root, text="Hashtag:").grid(row=0, column=0, padx=5, pady=5)
hashtag_entry = tk.Entry(root)
hashtag_entry.grid(row=0, column=1, padx=5, pady=5)

# Subscribe and unsubscribe buttons
sub_btn = tk.Button(root, text="Subscribe", command=subscribe_hashtag)
sub_btn.grid(row=0, column=2, padx=5, pady=5)

unsub_btn = tk.Button(root, text="Unsubscribe", command=unsubscribe_hashtag)
unsub_btn.grid(row=0, column=3, padx=5, pady=5)

# Text area to display received tweets
tweet_area = scrolledtext.ScrolledText(root, width=60, height=20)
tweet_area.grid(row=1, column=0, columnspan=4, pady=10, padx=5)

# Start GUI
root.mainloop()
