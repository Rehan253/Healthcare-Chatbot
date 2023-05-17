import os
import openai
import gradio as gr

# Get the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nAI:"
restart_sequence = "\nHuman:"

prompt = "Ask me anything..."

response_cache = {}

def openai_create(prompt):
    if prompt in response_cache:
        return response_cache[prompt]

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
    output = response.choices[0].text.strip()
    response_cache[prompt] = output
    return output

def chatgpt_clone(input_text, history=[]):
    history.append((input_text, ""))
    response = openai_create(input_text)
    history.append(("", response))
    return response, history

def main():
    if not openai.api_key:
        raise ValueError("Please provide your OpenAI API key.")

    iface = gr.Interface(
        fn=chatgpt_clone,
        inputs="text",
        outputs=["text", "textbox"],
        title="Healthcare Chatbot",
        description="Ask me anything!",
        allow_flagging="never",
        examples=[
            ["What are the symptoms of COVID-19?", "COVID-19 symptoms include fever, cough, and difficulty breathing."],
            ["How can I prevent heart disease?",
             "To prevent heart disease, you should maintain a healthy diet and exercise regularly."],
        ]
    )
    iface.launch()

if __name__ == "__main__":
    main()
