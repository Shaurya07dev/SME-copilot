# OpsPilot Video Demo Script

**Goal**: Show the agent analyzing data, finding an issue, and taking action.

## Scene 1: The Setup (0:00 - 0:30)
-   **Visual**: Show the "Cafe Delight" Google Sheet.
-   **Action**: Point out the "Sales" tab (normal data) and "Inventory" tab (set one item to very low quantity to trigger an alert).
-   **Voiceover**: "This is OpsPilot. It connects directly to this Google Sheet where our cafe tracks sales and inventory."

## Scene 2: The Run (0:30 - 1:00)
-   **Visual**: Split screen with Terminal and Google Sheet.
-   **Action**: Run `python -m src.main --business cafe_delight`.
-   **Visual**: Watch the terminal logs show "Loading data...", "Detecting Issues...", "Generating Briefing...".
-   **Voiceover**: "I run the daily review. The agent uses Gemini 2.0 Flash to analyze the data against our business profile."

## Scene 3: The Result (1:00 - 1:30)
-   **Visual**: Show the terminal output (The Briefing).
-   **Visual**: Switch to the Google Sheet "DecisionLog" tab to show the new entry.
-   **Visual**: Switch to the "Tasks" tab to show the new task: "Restock Inventory".
-   **Voiceover**: "It detected low inventory, logged the decision, and automatically created a task for the manager."

## Scene 4: MCP Bonus (1:30 - 2:00)
-   **Visual**: (Optional) Show an MCP client (like Claude Desktop) asking "What is the revenue for Cafe Delight?" and getting an answer via OpsPilot.
-   **Voiceover**: "And because it's built on MCP, I can query my business data from any compatible AI assistant."
