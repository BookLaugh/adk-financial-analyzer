import asyncio
import os
import sys
import time

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from .agent import root_agent

# Import specialized agents for the runner

load_dotenv()

# Verify API key
google_api_key = os.environ.get('GOOGLE_API_KEY', '')
if not google_api_key:
    print("❌ GOOGLE_API_KEY is not set! Please set it in your .env file.")
    sys.exit(1)

print("✅ API key is configured.")


async def analyze_stock(company_name, runner, session_service):
    """Analyze a stock using the Basic Stock Analyzer agent."""
    # Set up session using the provided service
    session = await session_service.create_session(
        app_name="multi_agent_stock_analyzer", user_id="cli_user"
    )

    # Create query
    query = (
        f"Analyze stock with the following symbol: {company_name}. Should I invest in it? Provide a"
        " comprehensive analysis."
    )
    content = types.Content(role="user", parts=[types.Part(text=query)])

    print(f"\n📊 Analyzing {company_name}...")
    print("This may take a few minutes as we gather and analyze data.")

    # Process events and collect final response
    result = ""
    search_count = 0

    async for event in runner.run_async(
            session_id=session.id,
            user_id="cli_user",
            new_message=content
    ):
        # Track search operations
        if hasattr(event, 'content') and hasattr(event.content, 'parts'):
            for part in event.content.parts:
                if hasattr(part, 'function_call') and hasattr(part.function_call, 'name'):
                    if part.function_call.name == 'google_search':
                        search_count += 1
                        print(f"🔍 Search #{search_count}: Finding information...")
                    elif part.function_call.name == 'company_overview':
                        print(f"Checking AlphaVantage API")
                elif hasattr(part, 'function_response'):
                    if hasattr(part.function_call, 'name'):
                        if part.function_call.name == 'google_search':
                            print(f"✅ Search result received")
                        elif part.function_call.name == 'company_overview_tool':
                            print(f"AlphaVantage API call returned")
                        else:
                            print(f"Received function response: {part.function_call}")
                    else:
                        print(f"Received function response: {part.function_call}")

        # Get final response
        if hasattr(event, 'is_final_response') and event.is_final_response:
            if hasattr(event, 'content') and hasattr(event.content, 'parts'):
                for part in event.content.parts:
                    if hasattr(part, 'text') and part.text:
                        result += part.text

    return result


async def main():
    print("\n============================================")
    print("🚀 MULTI-AGENT STOCK ANALYZER - CLI INTERFACE")
    print("============================================")

    # Initialize SessionService and Runner once
    session_service = InMemorySessionService()
    runner = Runner(
        agent=root_agent,  # The main orchestrator
        session_service=session_service,
        app_name="multi_agent_stock_analyzer",
    )

    # Get company name from args or prompt user
    if len(sys.argv) > 1:
        company = sys.argv[1]
    else:
        company = input("\nEnter a company ticker to analyze (or press Enter for MSFT): ").strip().upper()
        if not company:
            company = "MSFT"

    try:
        start_time = time.time()
        # Pass runner and session_service to the analysis function
        result = await analyze_stock(company, runner, session_service)
        end_time = time.time()

        print("\n============================================")
        print(f"ANALYSIS COMPLETED IN {round(end_time - start_time, 1)} SECONDS")
        print("============================================")

        print(result)

    except Exception as e:
        print(f"\n❌ Error during analysis: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
