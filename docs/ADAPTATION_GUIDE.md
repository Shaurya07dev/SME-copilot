# Adapting OpsPilot for Different Businesses

OpsPilot is designed to be **industry-agnostic**. You can adapt it for a Gym, Clinic, Supermarket, or any other business by changing the **Configuration** (`profiles.json`) and the **Data Source** (Google Sheets). You do **not** need to rewrite the Python code for most use cases.

## The Core Concept
The agent logic is generic:
1.  **Read Data**: It reads tables you define.
2.  **Compute KPIs**: It sums/counts columns you specify.
3.  **Check Thresholds**: It compares KPIs against limits you set.
4.  **Act**: It generates tasks/emails based on issues.

## Step-by-Step Adaptation Guide

### 1. Define Your Data (Google Sheets)
Create tabs in your Google Sheet that match your business entities.

**Example: Gym**
-   **Memberships**: `| MemberID | Name | Type | Status | ExpiryDate |`
-   **Attendance**: `| Date | MemberID | Class |`
-   **Equipment**: `| ID | Name | LastServiceDate | Status |`

**Example: Clinic**
-   **Appointments**: `| Date | PatientID | Doctor | Status |`
-   **Inventory**: `| ItemID | Name | Quantity | ExpiryDate |`

### 2. Update Configuration (`data/profiles.json`)
You need to tell OpsPilot how to read this new data.

#### For a Gym
```json
"city_gym": {
    "name": "City Gym",
    "industry": "fitness",
    "spreadsheet_id": "YOUR_SHEET_ID",
    "tables": {
        "members": "Memberships!A:E",
        "attendance": "Attendance!A:C",
        "equipment": "Equipment!A:D"
    },
    "kpis": {
        "active_members": {"column": "Status", "op": "count_if_active"}, 
        "daily_checkins": {"column": "MemberID", "op": "count"}
    },
    "thresholds": {
        "min_daily_checkins": 50
    }
}
```

#### For a Supermarket
```json
"super_mart": {
    "name": "Super Mart",
    "industry": "retail",
    "spreadsheet_id": "YOUR_SHEET_ID",
    "tables": {
        "sales": "Sales!A:F",
        "inventory": "Inventory!A:E",
        "wastage": "Wastage!A:D"
    },
    "kpis": {
        "revenue": {"column": "TotalAmount", "op": "sum"},
        "wastage_cost": {"column": "Cost", "op": "sum"}
    },
    "thresholds": {
        "max_wastage_cost": 100
    }
}
```

### 3. Run with New Profile
Run the agent with the new business ID:
```bash
python -m src.main --business city_gym
```

## Advanced Customization (Code Changes)
If you need complex logic that isn't just "Sum" or "Count" (e.g., calculating "Retention Rate" or "Patient Wait Time"), you might need to add a small function in `src/tools/analytics_tools.py`.

**Example: Adding a Custom KPI**
In `src/tools/analytics_tools.py`:
```python
def compute_kpis(data, config):
    # ... existing code ...
    if op == "custom_retention":
        # Your custom python logic here
        results[kpi_name] = calculate_retention(data)
```
