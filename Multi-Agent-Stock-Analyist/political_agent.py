from google.adk.agents import Agent
from google.adk.tools import google_search

political_agent = Agent(
    model="gemini-2.0-flash",
    name="political_regulatory_analyst",
    description="Analyzes the political and regulatory environment relevant to a company.",
    instruction="""You are a political and regulatory analyst. Use the google_search tool to find information on the current political and regulatory factors relevant to the specified company (e.g., regulatory environment, pending legislation, political risks, antitrust concerns, tax policies, ESG trends).

Company: [Company Name]

Present the findings as a concise summary report. Output ONLY the report content.
""",
    tools=[google_search]
) 