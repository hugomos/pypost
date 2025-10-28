from .ai.agent import Agent
from .ai.gemini.genai import GenAIAdapter

class AdapterFactory:
  def ai_agent(self) -> Agent:
    return GenAIAdapter()
