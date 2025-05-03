# Basic Stock Analyzer

> Part 1 of the Google ADK Blog Series: "Building Intelligent Agents with Google's Agent Development Kit"

A powerful stock analysis tool built with Google ADK that provides comprehensive investment recommendations by analyzing news, historical performance, economic factors, and political risks.

## About This Series

This project is the first installment in a blog series exploring Google's Agent Development Kit (ADK). Throughout this series, we'll:

1. **Start with this basic stock analyzer** - Introducing ADK fundamentals and core concepts
2. **Enhance and refine it** - Adding features like portfolio management, visualization, and more sophisticated analysis
3. **Deploy and productionize** - Making it accessible as a web service
4. **Explore other ADK applications** - Building different types of agents for various domains

Follow along as we explore the capabilities of Google ADK and develop increasingly sophisticated agent-based applications!

## Features

- **Real-time analysis** using Google Search to find the latest news about any company
- **Structured analysis framework** covering multiple aspects of stock evaluation
- **Clear investment recommendations** with Buy/Hold/Sell guidance
- **Risk assessment** on a scale of 1-5
- **Target price range** for 3-month outlook
- **Supporting factors and risks** for making informed decisions

## Demo

Check out the demo video to see the Stock Analyzer in action:

<video controls src="Assets/Demo-video-mp4.mp4" title="Stock Analyzer Demo"></video>

## Setup

1. Install required packages:
   ```
   pip install google-adk dotenv
   ```

2. Create a `.env` file in the root directory with your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

3. Make sure the Google Generative Language API is enabled for your project and API key.

## Usage

### Web Interface

To use the agent with the ADK Web UI:

1. Navigate to the parent directory and run:
   ```
   adk web
   ```

2. Access the web interface at http://localhost:8000

3. Enter queries like:
   - "Analyze Apple"
   - "Should I invest in Tesla?"
   - "What do you think about Netflix stock?"
   - "Give me an analysis of Amazon"

### Command Line

To run from the command line:

```
python cli.py [COMPANY_NAME]
```

Example:
```
python cli.py Microsoft
```

If no company is specified, the tool will analyze Microsoft by default.

## Example Output

The analysis output includes:

- Recent news headlines with publication dates
- Historical price trend analysis
- Economic impact assessment
- Political and regulatory risk evaluation
- Clear investment recommendation
- Risk level (1-5)
- Target price range for next 3 months
- Key positive and negative factors


## Notes

- Analysis takes approximately 1-3 minutes to complete depending on query complexity
- API rate limits may apply when performing multiple analyses in succession
- This tool is for informational purposes only and should not be considered professional financial advice