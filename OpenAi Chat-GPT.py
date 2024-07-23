import os
from openai import OpenAI
from dotenv import load_dotenv

# Load Environment variable from the .env file
load_dotenv()

# Set Your Open AI Key
client = OpenAI()

print("Chatbot is ready. Type 'exit' to end the conversation.")

while True:

    #Prompt 
    prompt = input("You : ")

    # Exit if user types 'exit
    if prompt.lower() == 'exit':
        print("Goodbye!")
        break

    # Messages
    messages = [

        {"role": "system", "content": "Your a helpful AI that trained By Gpt 4.0",
        "role": "system", "content": "Your a God Ai That also Knows how make jokes",
        "role": "system", "content": prompt
        }
    ]

    # Call Open Api

    # responses 
    responses = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = messages,
    temperature = 0.7
    )

    # Print the responses
    print(responses.choices[0].message.content)

