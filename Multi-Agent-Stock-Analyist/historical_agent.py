from google.adk.agents import Agent
from google.adk.tools import google_search

historical_agent = Agent(
    model="gemini-2.0-flash",
    name="historical_stock_analyst",
    description="Analyzes the historical stock performance of a company.",
    instruction="""You are a historical stock analyst. Use the google_search tool to find information on the company's stock performance over the past 2 years (e.g., price trends, volatility, index comparison, technical indicators, major events impact, valuation metrics).

Company: [Company Name]

Present the findings as a concise summary report. Output ONLY the report content.
""",
    tools=[google_search]
) 