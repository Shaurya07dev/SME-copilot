1.  Ensure you have Python 3.9+ installed.
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### B. Google Cloud Project Setup
1.  Go to the [Google Cloud Console](https://console.cloud.google.com/).
2.  Create a **New Project** (e.g., "OpsPilot-Demo").
3.  **Enable APIs**:
    -   Go to "APIs & Services" > "Library".
    -   Search for and enable the following APIs:
        -   **Google Sheets API**
        -   **Google Drive API**
        -   **Gmail API**
        -   **Google Calendar API**
4.  **Create Service Account**:
    -   Go to "APIs & Services" > "Credentials".
    -   Click "Create Credentials" > "Service Account".
    -   Name it (e.g., "opspilot-bot").
    -   Grant it the **Editor** role (Project > Editor) for simplicity, or specific roles for Sheets/Gmail/Calendar.
    -   Click "Done".
5.  **Download Key**:
    -   Click on the newly created Service Account email.
    -   Go to the "Keys" tab.
    -   Click "Add Key" > "Create new key" > **JSON**.
    -   Save the downloaded file as `credentials.json` in the `sme-copilot` folder (where this README is).

### C. AI Model Setup
1.  Get an API Key for Google Gemini (or OpenAI if you modify the code).
2.  Create a `.env` file in the root folder (copy `.env.example`):
    ```bash
    cp .env.example .env
    ```
3.  Open `.env` and paste your key:
    ```
    GEMINI_API_KEY=your_actual_api_key_here
    ```

## 2. Google Sheet Setup

You need a Google Sheet to act as the database.

1.  Create a new Google Sheet (e.g., "Cafe Delight Operations").
2.  **Share the Sheet**:
    -   Copy the **Service Account Email** (from step B.4 or inside `credentials.json`).
    -   Click "Share" in your Google Sheet and paste the email. Give it **Editor** access.
3.  **Create Tabs**:
    Create the following tabs (worksheets) with these exact headers (row 1):

    **Tab: Sales**
    | Date | OrderID | Item | Amount | Status |
    |---|---|---|---|---|
    | 2023-10-27 | 1001 | Coffee | 5.00 | Completed |

    **Tab: Inventory**
    | ItemID | Name | Quantity | Unit |
    |---|---|---|---|
    | I001 | Coffee Beans | 20 | kg |

    **Tab: Staff**
    | ID | Name | Role | Shift |
    |---|---|---|---|
    | S01 | Alice | Barista | Morning |

    **Tab: DecisionLog** (Leave empty, the agent will write here)
    | Date | KPI_Summary | Issues | Actions |
    |---|---|---|---|

    **Tab: Tasks** (Leave empty, the agent will write here)
    | Title | Description | Status | CreatedAt |
    |---|---|---|---|

4.  **Get Spreadsheet ID**:
    -   The ID is in the URL: `https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit`
    -   Copy this ID.

## 3. Configuration

1.  Open `data/profiles.json`.
2.  Update the `spreadsheet_id` with your copied ID.
3.  (Optional) Adjust thresholds or KPI definitions.

## 4. Running OpsPilot

### Run Daily Review (CLI)
To run a manual daily review:
```bash
python -m src.main --business cafe_delight
```
This will:
1.  Read data from your Sheet.
2.  Calculate KPIs and detect issues.
3.  Generate a briefing using Gemini.
4.  Log the decision to the `DecisionLog` tab.
5.  Create tasks in the `Tasks` tab if issues are found.

### Run MCP Server
To expose these tools to an MCP client (like Claude Desktop or another agent):
```bash
python src/mcp/server.py
```

## Troubleshooting
-   **Authentication Error**: Ensure `credentials.json` is in the root and the Service Account has "Editor" access to the Sheet.
-   **API Not Enabled**: Check Google Cloud Console to ensure all 4 APIs are enabled.
