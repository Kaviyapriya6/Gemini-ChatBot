# Gemini-ChatBot

A powerful chatbot powered by Google's Gemini-Pro API, designed to provide intelligent and interactive conversations. Built with Python and Streamlit, this application is easy to set up and use for both developers and end-users.

## Features

- **Interactive Chat Interface**: Engage in real-time conversations with the Gemini-Pro model.
- **Streamed Responses**: Responses are streamed dynamically, providing a smooth user experience.
- **Customizable Configuration**: Adjust parameters like temperature, top-p, and max output tokens to fine-tune the chatbot's behavior.
- **Secure API Key Management**: Safely load API keys using environment variables.
- **Error Handling**: Gracefully handles missing API keys or unsupported models.

## Why `google.genai`?

This project uses the `google.genai` library instead of the older `google.generativeai` library. The latter has been deprecated and is no longer functional. The `google.genai` library provides updated and improved functionality for interacting with Google's generative AI models.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Kaviyapriya6/Gemini-ChatBot.git
   cd Gemini-ChatBot
   ```

2. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory of the project.
   - Add your Google Gemini API key to the `.env` file:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

3. **Install Dependencies**:
   Install the required Python packages using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   Start the Streamlit app locally:
   ```bash
   streamlit run main.py
   ```

   The app will launch in your default web browser.

## Usage

- Enter your query in the chat input box at the bottom of the page.
- The chatbot will respond dynamically, displaying its response as it is generated.
- Your conversation history is preserved during the session.

## Configuration

The chatbot supports the following configuration options:

- **Temperature**: Controls the randomness of the model's responses (default: 1).
- **Top-P**: Limits the model's sampling pool to the most probable tokens (default: 0.95).
- **Top-K**: Limits the number of tokens considered for sampling (default: 40).
- **Max Output Tokens**: Sets the maximum length of the generated response (default: 8192).

These parameters can be adjusted in the `generate_response_stream` function within `main.py`.

## Requirements

- Python 3.8 or higher
- Streamlit
- Google GenAI Python SDK (`google.genai`)
- A valid Google Gemini API key

Refer to the `requirements.txt` file for the full list of dependencies.

## Contributing

Contributions are welcome! If you'd like to improve this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m "Add some feature"`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

For questions, bug reports, or feature requests, please open an issue in the repository.
