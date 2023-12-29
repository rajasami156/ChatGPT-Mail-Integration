# GPTMail Connect 📧🤖

GPTMail Connect is a powerful integration of OpenAI's GPT-3.5 language model and Gmail, designed to streamline and enhance your email composition experience. This intelligent assistant seamlessly blends natural language processing with efficient email workflows.

## Features

- **Effortless Email Drafting:** Leverage the capabilities of GPT-3.5 to compose emails effortlessly with natural language.
  
- **Intelligent Draft Creation:** Create Gmail drafts for editing with creative prompts, expanding your email composition possibilities.
  
- **Smart Draft Searching:** Easily search through your drafts using intuitive natural language queries to find the latest email.

## Getting Started

1. **Installation:**
   - Clone the repository: `git clone https://github.com/rajasami156/GPTMail-Integrator.git`
   - Install dependencies: `pip install -r requirements.txt`

2. **Configuration:**
   - Set your OpenAI API key in the environment variable `OPENAI_API_KEY`.
   - Customize Gmail credentials as needed.

3. **Usage:**
   - Run the script: `python gptmail_connect.py`
   - Follow the prompts to compose, create drafts, and search emails.

## Example Usage

```python
# Compose an email
agent.run({
    "input": {
        "message": "This is the email body...",
        "to": ["recipient@example.com"],
        "subject": "Subject of the email",
        "cc": ["cc@example.com"],
        "bcc": ["bcc@example.com"]
    }
})

# Create a Gmail draft for editing
agent.run({
    "input": "Create a gmail draft for me to edit of a letter...",
    "to": ["recipient@example.com"],
    "subject": "Subject of the draft"
})

# Search drafts for the latest email
agent.run({
    "input": "Could you search in my drafts for the latest email?"
})
