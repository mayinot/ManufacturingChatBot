import openai
from app.config import Config
from app.utils.logging import get_logger

logger = get_logger(__name__)

openai.api_key = Config.OPENAI_API_KEY

def chat(history):
    try:
        # Prepare the messages
        messages = [{"role": "system", "content": "You are a helpful manufacturing control assistant."}] + history

        # Make the API call to OpenAI
        response = openai.ChatCompletion.create(
            model=Config.MODEL,
            messages=messages,
            max_tokens=150,
            temperature=0.7
        )

        # Extract the response content
        reply = response.choices[0].message["content"]
        history.append({"role": "assistant", "content": reply})

        logger.info(f"Chat response: {reply}")
        return history

    except Exception as e:
        logger.error(f"Error in chat_service: {e}")
        return history + [{"role": "assistant", "content": "Sorry, I encountered an error processing your request."}]
