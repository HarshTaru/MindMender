# Flask-Blenderbot Chat Application

This is a simple Flask web application and command-line interface for interacting with Blenderbot, a conversational AI model developed by Facebook. Users can interact with the chatbot either through a web interface or by using their voice via a microphone.

## Usage

### Web Interface

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/flask-blenderbot.git
    ```

2. Navigate to the project directory:

    ```bash
    cd flask-blenderbot
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask app:

    ```bash
    python app.py
    ```

5. Open your web browser and go to `http://localhost:5000` to access the chat interface.

### Command-Line Interface

1. Clone the repository and navigate to the project directory as mentioned in steps 1 and 2 above.

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Python script:

    ```bash
    python main.py
    ```

4. Follow the on-screen prompts to interact with the chatbot using your keyboard or microphone.

## Requirements

- Flask==2.0.2
- transformers==4.11.3
- speechrecognition==3.8.1
- pyttsx3==2.90

Install the dependencies using `pip install -r requirements.txt` before running the application.

## Additional Notes

- The `BlenderbotForConditionalGeneration` model is used for generating responses to user inputs.
- The web interface allows users to interact with the chatbot by entering text messages.
- The command-line interface offers two modes of interaction: text input and voice input (using a microphone).
- To terminate the application, simply enter 'bye', 'quit', or 'terminate' during the conversation.

