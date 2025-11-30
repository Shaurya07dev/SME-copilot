# OpsPilot - Hackathon Submission

**Track**: Enterprise Agents

## Problem Statement
Small business owners (supermarkets, restaurants, retail shops, clinics & medical stores, salons, etc.) struggle to keep up with daily operations. Data is scattered across POS systems, spreadsheets, and emails. They often miss critical trends (like low inventory or declining revenue) until it's too late, and spend hours manually coordinating tasks and updates.

## Solution: OpsPilot
OpsPilot is a **Multi-Business AI Operations Co-Pilot** that transforms passive data into active business intelligence. Instead of forcing owners to dig through spreadsheets, OpsPilot brings the insights to them.

-   **Unifies Operations**: Bridges the gap between scattered data (Sheets) and action (Email/Calendar), creating a single source of truth.
-   **Automates Decision Making**: Turns raw numbers into concrete next steps, eliminating analysis paralysis.
-   **Empowers Action**: Doesn't just report problems; schedules the meetings and creates the tasks to fix them immediately.
-   **Adapts Instantly**: One brain that learns the specific context of any business—from cafes to retail stores—without custom code.

## Technical Architecture
Built with **Python** and **Google Gemini 2.0 Flash**, OpsPilot features:
1.  **Multi-Agent System**:
    -   **Planner**: Orchestrates the daily workflow.
    -   **Analytics Agent**: Crunches numbers and detects issues.
    -   **Advisor Agent**: Uses LLMs to generate human-readable insights and recommend actions.
2.  **Model Context Protocol (MCP)**: Exposes all tools as an MCP server, allowing other AI clients (like Claude Desktop) to interact with the business data.
3.  **Real Integrations**: Google Sheets, Gmail, and Google Calendar APIs.

## Value Proposition
-   **Reclaim Your Time**: Frees up 5+ hours per week by automating the daily "checking the numbers" grind, allowing owners to focus on growth.
-   **Prevent Revenue Leakage**: Proactively identifies stockouts and sales dips *before* they hurt the bottom line.
-   **Operational Resilience**: Ensures no critical metric is ever overlooked, providing 24/7 monitoring that human managers can't match.
-   **Future-Proof**: Built on the Model Context Protocol (MCP), making your business data accessible to the next generation of AI tools.

## How to Run
1.  Clone the repo.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Add credentials (`credentials.json` and `.env`).
4.  Run the daily review: `python -m src.main --business cafe_delight`

## Video Demo
[Link to your video here]
