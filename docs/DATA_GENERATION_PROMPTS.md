# AI Prompt for Demo Data (Indian Context)

Copy and paste this **entire block** into ChatGPT or Gemini. It will generate all 3 tables for you in one go.

***

**Prompt:**

> "I need to generate dummy data for a Cafe's Google Sheet to test an AI agent. Please generate **three separate Markdown tables** based on the following strict rules. Use **Indian names** and **Rupees (₹)**.
>
> **Table 1: Sales Data (Goal: Trigger Low Revenue Alert)**
> *   Columns: `Date`, `OrderID`, `Item`, `Amount`, `Status`
> *   Generate **50 rows**.
> *   **Date**: Use dates from the current month (e.g., 2023-12-01).
> *   **Item**: Masala Chai, Filter Coffee, Samosa, Vada Pav, Bun Maska.
> *   **Amount**: Randomly between ₹10 and ₹20.
> *   **Status**: Mostly 'Completed'.
> *   **CRITICAL**: The **TOTAL SUM** of the 'Amount' column must be **LESS THAN ₹1000**.
>
> **Table 2: Inventory Data (Goal: Trigger Low Inventory Task)**
> *   Columns: `ItemID`, `Name`, `Quantity`, `Unit`
> *   Generate **20 rows**.
> *   **ItemID**: I001 to I020.
> *   **Name**: Cafe ingredients (Milk, Tea Powder, Sugar, Maida, Potatoes, etc.).
> *   **Unit**: kg, liters, packets.
> *   **CRITICAL**: The **TOTAL SUM** of 'Quantity' must be **LESS THAN 50** (e.g., 1 or 2 per item).
>
> **Table 3: Staff Data (Goal: Trigger Staff Shortage Meeting)**
> *   Columns: `ID`, `Name`, `Role`, `Shift`
> *   Generate exactly **2 rows**.
> *   **Name**: Use Indian names (e.g., Rahul, Priya).
> *   **Role**: Manager, Barista.
> *   **Shift**: Morning, Evening.
> *   **CRITICAL**: Do NOT generate more than 2 rows."
