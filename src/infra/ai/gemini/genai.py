import os
from google import genai, auth

from ..agent import Agent

class GenAIAdapter(Agent):
  AGENT_MODEL = "gemini-2.5-flash"

  def __init__(self):
    api_key = os.getenv("GOOGLE_AI_API_KEY")
    self.client = genai.Client(api_key=api_key)

  def prompt(self, prompt: str, **kwargs) -> str | None:
    response = self.client.models.generate_content(
      model=self.__class__.AGENT_MODEL,
      contents=[prompt],
      config={
        'temperature': kwargs.get('temperature', 0.7),
        'system_instruction': kwargs.get('system_instruction', None)
      }
    )

    if not response: raise Exception("[GenAIAdapter] Failed to generate response")
    return response.text
