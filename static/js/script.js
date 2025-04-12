const socket = io();

// Connection events
socket.on('connect', () => {
    console.log('Connected to server');
});

socket.on('disconnect', () => {
    console.log('Disconnected from server');
});

// Listen for messages
socket.on('message', (data) => {
    console.log('Message received:', data);
    // Handle the message as needed
});

// Function to send messages
function sendMessage(message) {
    socket.emit('message', message);
}