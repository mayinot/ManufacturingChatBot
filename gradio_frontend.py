import gradio as gr
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

def chat_with_bot(history):
    response = requests.post(f"{BACKEND_URL}/chat", json=history)
    response.raise_for_status()
    return response.json()["history"]

with gr.Blocks() as app:
    chatbot = gr.Chatbot()
    textbox = gr.Textbox(placeholder="Ask something...", label="Chat")

    textbox.submit(fn=lambda message, history: chat_with_bot(history + [{"role": "user", "content": message}]),
                   inputs=[textbox, chatbot], outputs=chatbot)

app.launch()
