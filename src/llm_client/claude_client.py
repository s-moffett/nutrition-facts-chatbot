import anthropic
from llm_client.llm_client import LLMClient

HAIKU = "claude-haiku-4-5"
SONNET = "claude-sonnet-4-5"

class ClaudeClient(LLMClient):
    def __init__(self) -> None:
        self.client = anthropic.Anthropic()
        self.model = SONNET

    def message(self, prompt: str) -> str:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        text = ' '.join([content.text for content in response.content if content.type == 'text'])
        return text
