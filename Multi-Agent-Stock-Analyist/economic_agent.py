from google.adk.agents import Agent
from google.adk.tools import google_search

economic_agent = Agent(
    model="gemini-2.0-flash",
    name="economic_analyst",
    description="Analyzes the macroeconomic environment relevant to a company.",
    instruction="""You are an economic analyst. Use the google_search tool to find information on the current economic factors relevant to the specified company (e.g., interest rates, inflation, GDP, supply chains, consumer spending, currency, industry indicators).

Company: [Company Name]

Present the findings as a concise summary report. Output ONLY the report content.
""",
    tools=[google_search]
) 