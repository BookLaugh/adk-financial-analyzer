from google.adk.agents import Agent

from multi_agent_stock_analyst.company_overview_tool import company_overview_tool

financial_agent = Agent(
    model="gemini-2.0-flash",
    name="financial_stock_analyst",
    description="Analyzes the financial figures from the stock market reports of the company.",
    instruction="""You are a financial and stock market analyst. 
Use the company_overview_tool to find current stock market overview  for the company like its profit margin, revenue, P/E ratio etc.
The company_overview_tool needs a stock ticker as the only argument and returns a dict with descriptive string keys and string values.
 
Company stock market symbol: [Company Name]

Focus on the following aspects:
*   **Financial figures:** Take into account EPS, EBITDA, P/E ratio, profit margin, Beta and similar numbers to reason about the current valuation and most likely changes in upcoming weeks and months.
*   **Volatility:** Look at beta value and what it means for recent stock price volatility.
*   **Key Changes:** Compare trailing with forward indicators, 50 and 200 day moving averages to reason about possible future volatility.

Present the findings as a concise summary report. Output ONLY the report content.
""",
    tools=[company_overview_tool]
)
