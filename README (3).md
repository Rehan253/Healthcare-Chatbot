
# Healthcare Chatbot 

A brief description of what this project does and who it's for


## Table of Content



* Overview
* Solution approach
* Documentation
* Installation 

* Code
* Domo 
* Deployment 

* API References 
* Environment Variables
* Features 

* Running Tests
* Run Locally
* Screenshot
* Used By
* Usage
* Roadmap
* Authors
* Lessons Learned
* Acknowledgements
* FAQ
* Feedback
 
## Overview

This is a simple chatbot application that uses OpenAI's GPT-3.5 language model to generate responses to user inputs. The model is trained on a large corpus of text and is capable of generating human-like responses to a wide variety of prompts.

This chatbot is specifically designed to address medical queries, where you can input your queries and receive corresponding answers.
## Solution approach

We will solve the problem of building a healthcare chatbot using the OpenAI API. Specifically, we will use the GPT-3 language model offered by the OpenAI API, which can generate high-quality text, answer questions, and perform other language tasks. This language model will be fine-tuned on specific healthcare datasets to improve its accuracy and relevance to patient queries
## Documentation



* The chatbot uses a prompt-based approach, where the user's input is combined with previous inputs to create a larger prompt for the model. This allows the model to generate more contextually relevant responses.

* The chatbot is currently trained on the "text-davinci-003" model and uses a number of parameters to control the output, including temperature, max tokens, top p, frequency penalty, and presence penalty.
## Installation

To run the code, you will need to install the following dependencies:


* openai module

* gradio module

You can install these modules using pip by running the following command:

* pip install openai gradio

Once the dependencies are installed, you can run the code using any Python environment or IDE.






## Demo

To see the chatbot in action, run the APP.PY file  and enter a prompt in the text box. The chatbot will generate a response based on the input prompt using the OpenAI API. The response will appear in the chatbot window.




## Deployment

* To deploy the chatbot on your own server, follow these steps:

* To deploy this chatbot, you need to run the code in a Python environment. You can use a Python Integrated Development Environment (IDE) such as VS Code, PyCharm, or Spyder to run the code on your local machin

* Install the required dependencies.


* Configure the chatbot parameters as desired.

* Launch the chatbot application.

## Data Availability 

[ Available  on Request ]

To enhance the performance of the chatbot and make it more personalized, we will use relevant datasets such as medical textbooks, research articles, medical chat logs, and patient feedback.


## Code availability

Here below is code link:

https://github.com/Rehan253/Healthcare-Chatbot#healthcare-chatbot
## API References



The healthcare chatbot project utilizes the ChatGPT API from OpenAI. Below are some references and resources related to the API:

- OpenAI API Documentation
This official documentation provides detailed information on how to use the ChatGPT API, including authentication, API endpoints, request/response formats, and example code snippets.
- OpenAI API Developer Guide
This guide specifically focuses on the ChatGPT API and provides instructions, best practices, and examples for building applications using the API.
- OpenAI API Python Library
The official Python library provided by OpenAI enables easier integration with the ChatGPT API in Python projects. The repository contains installation instructions and code examples.
- OpenAI API Community Forum
The community forum is a valuable resource for developers to ask questions, share feedback, and learn from the experiences of other users working with the OpenAI API.



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY = 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`

* Another API KEY
`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`


## Features

- Intelligent responses to patient queries
- Personalized recommendations based on medical history
- Access to reliable health information
- Quick response times
- Expansion to other languages: 




## Running Tests

To run tests, run the following command

```bash
  npm run test
```


## Run Locally

#### 1  Clone the project repository from GitHub:

             https://github.com/Rehan253/Healthcare-Chatbot#healthcare-chatbot

#### 2  Install the required dependencies.
        
          pip install openai
          pip install gradio

        
#### 3 API KEY
                  API_KEY= sk-qA***********************22jbp1

#### 4 Run Application

                   python app.py








## Screenshots

- Screenshots 

* https://github.com/Rehan253/Healthcare-Chatbot/blob/main/Screenshot%20(509).png

* https://github.com/Rehan253/Healthcare-Chatbot/blob/main/Screenshot%20(510).png

*  https://github.com/Rehan253/Healthcare-Chatbot/blob/main/Screenshot%20(511).png

## Used By

This chatbot can be used by healthcare providers and patients to ask and receive answers to healthcare-related questions. It can also be used by developers as an example of how to integrate OpenAI's GPT-3 language model into a chatbot application.





## Usage/Examples

 use this chatbot, follow these steps:

* Clone the repository containing the code for the chatbot.

* Set up an OpenAI API key and enter it into the openai.api_key variable in the code.

* Run the code to launch the chatbot application.

* Once the chatbot is running, you can type your message into the text box and click "SEND" to receive a response from the chatbot.

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



## Authors

- Rehan Shafique (20L-1175)
- Waseef Khalid Khan Niazi (20L-1342)


## Lessons Learned 

- We learned the importance of fine-tuning models and leveraging relevant datasets to improve accuracy and relevance.
- We have learned how to explore the API and, despite facing numerous challenges, we have gained valuable experience. This project has been a great learning experience, pushing us to overcome obstacles and expand our knowledge in dealing with API integration.

# Acknowledgements

We would like to express our sincere gratitude to the following individuals  for their valuable contributions and support throughout the development of this healthcare chatbot project:

- Liam Ottley

https://www.youtube.com/watch?v=3EdEw4gyr-s

- Platform openAI

https://platform.openai.com/docs/guides/fine-tuning


We would like to express our sincere gratitude to our brother Rana Muhammad waqas for his invaluable assistance in dealing with all kinds of financial issues related to this project. His support in managing the financial aspects has been crucial and greatly appreciated throughout the development process.


## FAQ

#### Question 1
Q: What model is the chatbot trained on?

#### Answer 1
A: The chatbot is currently trained on the "text-davinci-003" model.

#### Question 2
: What parameters does the chatbot use to control the output?

#### Answer 2

 The chatbot uses temperature, max tokens, top p, frequency penalty, and presence penalty to control the output.


## Feedback

If you have any feedback, please reach out to us at waseefkhalid481@gmail.com & rehan.shafiue.253@gmail.com

