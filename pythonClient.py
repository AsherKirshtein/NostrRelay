import json
import ssl
import time
import random
from nostr.event import Event
from nostr.relay_manager import RelayManager
from nostr.key import PrivateKey

# Predefined array of workout messages
WORKOUT_MESSAGES = [
    "Push-ups: 3 sets of 15 reps",
    "Run 5k at a steady pace",
    "20-minute yoga session",
    "Burpees: 3 sets of 10 reps",
    "Squats: 3 sets of 20 reps",
    "Bench press: 3 sets of 12 reps",
    "Deadlifts: 4 sets of 8 reps",
    "Stretching: 15 minutes full body",
    "Plank hold: 3 sets of 1 minute each",
    "Pull-ups: 3 sets of 10 reps",
    "Bicycle crunches: 3 sets of 20 reps",
    "HIIT workout: 20 minutes (30 seconds work, 30 seconds rest)",
    "Jumping jacks: 4 sets of 25 reps",
    "Mountain climbers: 3 sets of 30 seconds",
    "Jogging: 30 minutes",
]

# Function to pick a random workout message
def generate_random_message():
    return random.choice(WORKOUT_MESSAGES)

# Function to generate multiple private keys for different senders
def generate_private_keys(num_senders):
    return [PrivateKey() for _ in range(num_senders)]

# Initialize the RelayManager and add your relay(s)
relay_manager = RelayManager()
relay_manager.add_relay("ws://localhost:7000")  # Your local relay

# Open connections with SSL certificate verification disabled (only for testing)
relay_manager.open_connections({"cert_reqs": ssl.CERT_NONE})  # NOTE: Disable SSL verification for testing only
time.sleep(1.25)  # Allow the connections to open

# Generate private keys for multiple senders
num_senders = 5  # Number of unique senders
senders = generate_private_keys(num_senders)

# Loop to send 10 random messages
for i in range(10):
    # Select a random sender
    sender = random.choice(senders)
    public_key = sender.public_key.hex()  # Get the public key of the sender
    
    # Pick a random workout message
    event_content = f"Workout {i+1}: {generate_random_message()}"
    
    # Create and sign an event
    event = Event(public_key, event_content)  # Provide both public key and content
    sender.sign_event(event)  # Sign the event with the sender's private key
    
    # Publish the event to all connected relays
    relay_manager.publish_event(event)
    print(f"Published from sender {public_key[:8]}...: {event_content}")
    
    # Sleep for a short period to simulate intervals between messages
    time.sleep(1)

# Allow some time for the last messages to send
time.sleep(1)

# Close all relay connections
relay_manager.close_connections()
