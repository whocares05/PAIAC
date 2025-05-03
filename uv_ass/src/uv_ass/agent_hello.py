from agents import (
    AsyncOpenAI,
    set_default_openai_client,
    set_tracing_disabled,
    set_default_openai_api,
    Agent,
    Runner
)
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

customClient = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=GEMINI_API_KEY,
)

set_default_openai_client(customClient)
set_tracing_disabled(True)
set_default_openai_api("chat_completions")

def helloAgent() -> None:
    agent = Agent(
        name="Mike",
        instructions="You are a helpful assistant",
        model="gemini-2.0-flash"
    )
    result = Runner.run_sync(agent, input="Tell me about cats in 2 sentences.")
    print(result.final_output)