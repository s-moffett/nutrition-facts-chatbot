from abc import ABC, abstractmethod

class LLMClient(ABC):

    @abstractmethod
    def message(self, prompt: str) -> str:
        return ''
