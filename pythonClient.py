import json
import ssl
import time
from nostr.event import Event
from nostr.relay_manager import RelayManager
from nostr.key import PrivateKey

# Initialize the RelayManager and add your relay(s)
relay_manager = RelayManager()
relay_manager.add_relay("ws://localhost:7000")  # Your local relay
relay_manager.add_relay("wss://nostr-pub.wellorder.net")  # Example public relay
relay_manager.add_relay("wss://relay.damus.io")  # Example public relay

# Open connections with SSL certificate verification disabled (only for testing)
relay_manager.open_connections({"cert_reqs": ssl.CERT_NONE})  # NOTE: Disable SSL verification for testing only
time.sleep(1.25)  # Allow the connections to open

# Generate a private key (for signing events)
private_key = PrivateKey()

# Create and sign an event
public_key = private_key.public_key.hex()  # Generate the associated public key
event_content = "Hello Nostr - From My Relay!"
event = Event(public_key, event_content)  # Provide both public key and content
private_key.sign_event(event)  # Sign the event with the private key

# Publish the event to all connected relays
relay_manager.publish_event(event)
time.sleep(1)  # Allow time for the messages to send

# Close all relay connections
relay_manager.close_connections()
