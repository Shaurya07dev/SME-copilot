from mcp.server.fastmcp import FastMCP
from src.tools.data_tools import load_sheet_table, save_decision_log, get_recent_history, get_business_profile
from src.tools.analytics_tools import compute_kpis, detect_issues, generate_actions

mcp = FastMCP("OpsPilot")

@mcp.tool()
def get_profile(business_id: str):
    """Get the business profile configuration."""
    return get_business_profile(business_id=business_id)

@mcp.tool()
def load_table(spreadsheet_id: str, range_name: str):
    """Load data from a Google Sheet table."""
    return load_sheet_table(spreadsheet_id, range_name)

@mcp.tool()
def save_log(spreadsheet_id: str, log_entry: list):
    """Save a decision log entry."""
    return save_decision_log(spreadsheet_id, log_entry)

@mcp.tool()
def compute_business_kpis(data: list, kpi_config: dict):
    """Compute KPIs from data."""
    return compute_kpis(data, kpi_config)

@mcp.tool()
def detect_business_issues(kpis: dict, thresholds: dict):
    """Detect issues based on KPIs."""
    return detect_issues(kpis, thresholds)

if __name__ == "__main__":
    mcp.run()
