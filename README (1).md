
# Healthcare Chatbot 

A brief description of what this project does and who it's for


## Table of Content



* Overview
* Installation 

* Code

* Demo

* Deployment

* Documentation
* Usage
* Used By
* API References 



* FAQ
* Roadmap


* Appendix
## Overview

This is a simple chatbot application that uses OpenAI's GPT-3.5 language model to generate responses to user inputs. The model is trained on a large corpus of text and is capable of generating human-like responses to a wide variety of prompts.

This chatbot is specifically designed to address medical queries, where you can input your queries and receive corresponding answers.
## Installation

To run the code, you will need to install the following dependencies:


* openai module

* gradio module

You can install these modules using pip by running the following command:

* pip install openai gradio

Once the dependencies are installed, you can run the code using any Python environment or IDE.






## Code

import os
import openai
import gradio as gr

openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "Ask me anything..."

def openai_create(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    return response.choices[0].text

def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history

block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>Healthcare</center></h1>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug=True)

## Demo

To see the chatbot in action, visit this website and enter a prompt in the text box. The chatbot will generate a response based on the input prompt using the OpenAI API. The response will appear in the chatbot window.




## Deployment

* To deploy the chatbot on your own server, follow these steps:

* To deploy this chatbot, you need to run the code in a Python environment. You can use a Python Integrated Development Environment (IDE) such as VS Code, PyCharm, or Spyder to run the code on your local machin

* Install the required dependencies.


* Configure the chatbot parameters as desired.

* Launch the chatbot application.

## Documentation



* The chatbot uses a prompt-based approach, where the user's input is combined with previous inputs to create a larger prompt for the model. This allows the model to generate more contextually relevant responses.

* The chatbot is currently trained on the "text-davinci-003" model and uses a number of parameters to control the output, including temperature, max tokens, top p, frequency penalty, and presence penalty.
## Usage/Examples

 use this chatbot, follow these steps:

* Clone the repository containing the code for the chatbot.

* Set up an OpenAI API key and enter it into the openai.api_key variable in the code.

* Run the code to launch the chatbot application.

* Once the chatbot is running, you can type your message into the text box and click "SEND" to receive a response from the chatbot.

## Used By

This chatbot can be used by healthcare providers and patients to ask and receive answers to healthcare-related questions. It can also be used by developers as an example of how to integrate OpenAI's GPT-3 language model into a chatbot application.





## API Reference


## Acknowledgements

 - `openai_create(prompt)`

This function sends a prompt to the OpenAI API and retrieves a response.

* ### Parameters

prompt: A string containing the user's input prompt.
Returns

A string containing the chatbot's response to the user input.

* ### Example Usage


response = openai_create("What is the best way to treat a cold?")

print(response) 



`chatgpt_clone(input, history)`

This function generates a response to the user's input using the openai_create() function and maintains a history of the conversation.


* ### Parameters

input: A string containing the user's input.

history: A list of tuples containing previous user inputs and chatbot responses.
Returns

A tuple containing the updated history and the chatbot's response to the user input.

* ### Example Usage

history = []
input = "What are the symptoms of COVID-19?"
history, response = chatgpt_clone(input, history)
print(response)


`block.launch()`

This function launches the chatbot application.




## FAQ

#### Question 1
Q: What model is the chatbot trained on?

#### Answer 1
A: The chatbot is currently trained on the "text-davinci-003" model.

#### Question 2
: What parameters does the chatbot use to control the output?

#### Answer 2

 The chatbot uses temperature, max tokens, top p, frequency penalty, and presence penalty to control the output.


## Roadmap

The current version of the code provides a basic chatbot that uses OpenAI's GPT-3 model to generate responses to user input.

 However, there are several potential areas for improvement and expansion. Here are some ideas for future development:

* ### Improved user experience: 
The chatbot interface could be improved to provide a more intuitive and user-friendly experience. For example, the input box could be resized automatically based on the length of the user's message, or the chat history could be displayed in a more visually appealing format.


* ### Multi-turn conversation support: 

Currently, the chatbot only responds to a single user input at a time. Adding support for multi-turn conversations would allow for more complex and engaging interactions with the user.


* ### Integration with external APIs:
 The chatbot could be expanded to integrate with external APIs that provide relevant information or services based on user input. For example, the chatbot could provide information about local healthcare providers or appointment availability based on the user's location.


* ### Customization and personalization:

The chatbot could be enhanced to allow for customization and personalization based on user preferences or previous interactions. For example, the chatbot could remember a user's name and tailor responses accordingly, or provide recommendations based on the user's previous search history.


* ### Expansion to other languages: 

Currently, the chatbot only supports English input and output. Expanding to other languages could broaden the reach and impact of the chatbot.
## Appendix

Any additional information goes here


* OpenAI API Documentation

* GitHub Repository

* License

* Code of Conduct

* Contributing Guidelines

* Bug Report Template

* Feature Request Template

* Pull Request Template