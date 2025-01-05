const WebSocket = require("ws");

const relayUrl = "ws://18.221.154.194:7000";
const ws = new WebSocket(relayUrl);

ws.on("open", () => {
  console.log("Connected to Nostr relay!");

  // Subscribe to events
  const subscriptionId = "example-subscription";
  ws.send(JSON.stringify(["REQ", subscriptionId, {}]));
});

ws.on("message", (data) => {
  // Decode and log the message
  const decodedMessage = data.toString();
  console.log("Received from relay:", decodedMessage);

  // Parse JSON if it's a valid JSON string
  try {
    const parsedMessage = JSON.parse(decodedMessage);
    console.log("Parsed message:", parsedMessage);
  } catch (err) {
    console.log("Unable to parse message as JSON:", decodedMessage);
  }
});

ws.on("error", (error) => {
  console.error("WebSocket error:", error);
});

ws.on("close", () => {
  console.log("Disconnected from Nostr relay.");
});
