"""Review aggregate workplace signals and suggest supportive human follow-up."""
from __future__ import annotations


def review_retention(signals: dict) -> dict:
    engagement = signals.get("engagement_score")
    overtime = signals.get("average_overtime_hours")
    absence = signals.get("absence_days")
    issues, evidence = [], {}
    if engagement is not None:
        engagement = min(max(float(engagement), 0), 100); evidence["engagement_score"] = engagement
        if engagement < 50: issues.append("low-aggregate-engagement")
    if overtime is not None:
        overtime = max(float(overtime), 0); evidence["average_overtime_hours"] = overtime
        if overtime > 10: issues.append("high-aggregate-overtime")
    if absence is not None:
        absence = max(float(absence), 0); evidence["absence_days"] = absence
        if absence > 5: issues.append("elevated-aggregate-absence")
    actions = ["Review workload and support options with the team."] if issues else ["Continue voluntary check-ins and monitor aggregate trends."]
    return {"issues": issues, "evidence": evidence, "supportive_actions": actions, "uncertainty": "Aggregate signals do not predict an individual's decision.", "adverse_action_permitted": False, "hr_review_required": True}
