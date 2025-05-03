from google.adk.agents import Agent
from google.adk.tools import google_search

news_agent = Agent(
    model="gemini-2.0-flash",
    name="news_reporter",
    description="Gathers recent news headlines for a company.",
    instruction="""You are a news reporter. Use the google_search tool to find 5 recent news headlines about the specified company, including publication dates if available.

Company: [Company Name]

Present the headlines as a numbered list. Output ONLY the numbered list.
""",
    tools=[google_search]
) 