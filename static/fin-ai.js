// Function to send a user message to the server and display the response
function sendUserMessage() {
    // Get the user's message from the input field
    var userMessage = document.getElementById('user-chat').value;

    // Check if the user's message is empty
    if (!userMessage) {
        return;
    }

    // Create an object with the user's message
    var requestData = {
        user_message: userMessage
    };
    displayMessage('You', userMessage);
    // Send the user's message to the server using a POST request
    fetch('/get_response', {
        method: 'POST',
        body: JSON.stringify(requestData), // Include user message
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        // Display the response from the server in the chat interface
        var botResponse = data.bot_response;

        displayMessage('Fin-AI', botResponse);
    })
    .catch(error => console.error(error));

    // Clear the input field
    document.getElementById('user-chat').value = '';
}

// Function to display messages in the chat interface
function displayMessage(sender, message) {
    var chatBox = document.getElementById('chat-box');
    var messageElement = document.createElement('div');
    messageElement.className = 'message';
    messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatBox.appendChild(messageElement);
}


// Add event listener for the "Send" button or another trigger to send messages
document.getElementById('send-button').addEventListener('click', sendUserMessage);

// Add event listener for the "Enter" key to send messages
document.getElementById('user-chat').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        sendUserMessage();
    }
});
