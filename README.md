# AI Email Response Agent

An intelligent email response generator that uses AI to create professional, context-aware email replies for businesses.

## 🚀 Features

- **AI-Powered Responses**: Uses Mistral 7B model via OpenRouter API to generate intelligent email replies
- **Professional Tone**: Automatically creates polite and professional business email responses
- **Context-Aware**: Analyzes email subject, body, and sender information to provide relevant replies
- **Easy Integration**: Simple Python function that can be integrated into existing email workflows
- **Secure**: API keys are safely stored in environment variables

## 📋 Prerequisites

- Python 3.7 or higher
- OpenRouter API account and API key
- Required Python packages (see Installation section)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/IBATMANSINGH/email-agent.git
   cd email-agent
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install required packages**
   ```bash
   pip install requests python-dotenv
   ```

4. **Set up environment variables**
   - Create a `.env` file in the project root
   - Add your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```

## 🔑 Getting an OpenRouter API Key

1. Visit [OpenRouter.ai](https://openrouter.ai/)
2. Sign up for an account
3. Navigate to the API section
4. Generate your API key
5. Add it to your `.env` file

## 💻 Usage

### Basic Usage

```python
from email_response_agent import generate_reply

# Generate a reply
subject = "Need help with my order #12345"
body = "Hi, I placed an order 5 days ago but haven't received it yet. Can you please check?"
sender = "John Doe"

reply = generate_reply(subject, body, sender)
print(reply)
```

### Running the Example

```bash
python email_response_agent.py
```

This will run a test example and display a generated email response.

## 📁 Project Structure

```
email-agent/
├── email_response_agent.py    # Main application code
├── .env                       # Environment variables (not tracked)
├── .gitignore                # Git ignore rules
├── LICENSE                   # Project license
├── README.md                 # This file
└── venv/                     # Virtual environment (not tracked)
```

## 🔧 Configuration

The agent uses the Mistral 7B Instruct model by default. You can modify the model in `email_response_agent.py`:

```python
data = {
    "model": "mistralai/mistral-7b-instruct",  # Change this to use different models
    "messages": [
        {"role": "user", "content": prompt}
    ]
}
```

## 🛡️ Security

- **API Keys**: Never commit your `.env` file to version control
- **Environment Variables**: All sensitive data is stored in environment variables
- **Gitignore**: The `.gitignore` file ensures sensitive files are not tracked

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**: Make sure your `.env` file contains the correct OpenRouter API key
2. **Module Not Found**: Ensure you've installed all required packages with `pip install requests python-dotenv`
3. **Network Issues**: Check your internet connection and OpenRouter API status

### Debug Mode

The application includes debug output to help troubleshoot API responses. Check the console output for detailed error messages.

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

### 🤖 AI-Assisted Development Process

This project was built using a "prompt-first" approach, where I leveraged an LLM as a coding co-pilot to translate a concept into a functional application.

*   **The Core Prompt:** I began by architecting the project with a high-level prompt to generate the core logic:
    > *"Write a Python script that can read unread emails from a Gmail account using the Gmail API. For each unread email, use Google's Gemini Pro LLM to analyze its content and classify it into a category like 'Interested', 'Not Interested', or 'More Information'."*

*   **Iteration and Refinement:** The AI generated the initial API connection code. I then used follow-up prompts to build out the full workflow:
    *   "Based on the AI's classification, write a function to automatically draft a reply email."
    *   "Implement logic to send the drafted reply using the Gmail API."
    *   "Add a feature to automatically mark the processed email as 'read' to avoid re-processing."

*   **My Role as the Developer:** My primary role was not just to code, but to act as the architect. This involved designing the prompts for email classification and response drafting, critically evaluating and debugging the AI-generated code, managing the complex authentication and API interactions with Google Cloud, and testing the end-to-end automation pipeline.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Made with ❤️ & Vibes by Ankit Singh
