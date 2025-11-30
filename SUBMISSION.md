# OpsPilot - Hackathon Submission

**Track**: Enterprise Agents

## Problem Statement
Small business owners (restaurants, salons, retail) struggle to stay on top of daily operations. Data is scattered across POS systems, spreadsheets, and emails. They often miss critical trends (like low inventory or declining revenue) until it's too late, and spend hours manually coordinating tasks and updates.

## Solution: OpsPilot
OpsPilot is a **Multi-Business AI Operations Co-Pilot** that acts as an intelligent layer on top of existing business data.

-   **Connects**: Directly to Google Sheets (where many SMEs live).
-   **Analyzes**: Runs a daily "Operations Review" to compute KPIs and detect anomalies using a multi-agent architecture.
-   **Acts**: Automatically generates tasks, schedules meetings, and sends briefings via Email/Calendar/MCP.
-   **Scales**: Configurable via "Business Profiles" to work for any industry.

## Technical Architecture
Built with **Python** and **Google Gemini 2.0 Flash**, OpsPilot features:
1.  **Multi-Agent System**:
    -   **Planner**: Orchestrates the daily workflow.
    -   **Analytics Agent**: Crunches numbers and detects issues.
    -   **Advisor Agent**: Uses LLMs to generate human-readable insights and recommend actions.
2.  **Model Context Protocol (MCP)**: Exposes all tools as an MCP server, allowing other AI clients (like Claude Desktop) to interact with the business data.
3.  **Real Integrations**: Google Sheets, Gmail, and Google Calendar APIs.

## Value Proposition
-   **Time Saved**: Automates the daily 1-hour manual review process (~5 hours/week saved per manager).
-   **Proactive**: Catches issues (e.g., "Low Inventory") *before* they impact sales.
-   **Interoperable**: The MCP layer means this agent can live inside your IDE or other AI tools.

## How to Run
1.  Clone the repo.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Add credentials (`credentials.json` and `.env`).
4.  Run the daily review: `python -m src.main --business cafe_delight`

## Video Demo
[Link to your video here]
