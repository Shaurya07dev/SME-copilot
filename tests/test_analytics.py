import pytest
from src.tools.analytics_tools import compute_kpis, detect_issues, generate_actions

def test_compute_kpis():
    data = [
        {"Amount": "100", "OrderID": "1"},
        {"Amount": "200", "OrderID": "2"},
        {"Amount": "50", "OrderID": "3"}
    ]
    config = {
        "revenue": {"column": "Amount", "op": "sum"},
        "orders": {"column": "OrderID", "op": "count"}
    }
    
    results = compute_kpis(data, config)
    assert results["revenue"] == 350.0
    assert results["orders"] == 3

def test_detect_issues():
    kpis = {"revenue": 350.0}
    thresholds = {"min_revenue": 500}
    
    issues = detect_issues(kpis, thresholds)
    assert len(issues) == 1
    assert "Low revenue" in issues[0]

def test_generate_actions():
    issues = ["Low revenue: 350 (Target: >500)"]
    actions = generate_actions(issues)
    
    assert len(actions) > 0
    assert actions[0]["type"] == "create_task"
