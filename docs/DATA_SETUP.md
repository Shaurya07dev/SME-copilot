# OpsPilot Demo Data Setup

Use this guide to populate your Google Sheet with specific data to trigger the actions you want to show in your video (Email, Task, Calendar Event).

## 1. Sheet Structure
Ensure your Google Sheet has these exact tab names:
*   `Sales`
*   `Inventory`
*   `Staff`
*   `DecisionLog` (Empty)
*   `Tasks` (Empty)

## 2. The "Crisis" Scenario (For the Video)
To demonstrate all features (Email, Task, Calendar), enter the following data. This will trigger all "Low" thresholds.

### Tab: Sales
(Triggers **Low Revenue** -> Sends Email)
| Date | OrderID | Item | Amount | Status |
|---|---|---|---|---|
| 2023-12-01 | 1001 | Coffee | 100 | Completed |

*Total Revenue: 100 (Threshold is 500)*

### Tab: Inventory
(Triggers **Low Inventory** -> Creates Task)
| ItemID | Name | Quantity | Unit |
|---|---|---|---|
| I001 | Coffee Beans | 10 | kg |

*Total Inventory: 10 (Threshold is 50)*

### Tab: Staff
(Triggers **Low Staff** -> Creates Calendar Event)
| ID | Name | Role | Shift |
|---|---|---|---|
| S01 | Alice | Barista | Morning |

*Total Staff: 1 (Threshold is 3)*

## 3. Running the Demo
1.  **Clear the Logs**: Delete everything in `DecisionLog` and `Tasks` tabs.
2.  **Run the Agent**:
    ```bash
    python -m src.main --business cafe_delight
    ```
3.  **Show the Results**:
    *   **Console**: Show the "Daily Briefing" output.
    *   **Sheet**: Show the new rows in `DecisionLog` and `Tasks`.
    *   **Email**: Show the "Alert: Low Revenue" email in your inbox.
    *   **Calendar**: Show the "Emergency Staff Meeting" event.

## 4. Resetting
To try again, just clear the `DecisionLog` and `Tasks` tabs. You can change the data values (e.g., increase Revenue to 600) to show a "Good Day" scenario where no alerts are generated.
