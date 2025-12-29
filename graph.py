from langgraph.graph import StateGraph

from agents.fetch_agent import fetch_agent
from agents.diff_agent import diff_agent
from agents.classify_agent import classify_agent
from agents.notify_agent import notify_agent
from agents.summarizer_agent import summarizer_agent


def build_graph():
    workflow = StateGraph(dict)

    workflow.add_node("fetch", fetch_agent)
    workflow.add_node("diff", diff_agent)
    workflow.add_node("classify", classify_agent)
    workflow.add_node("summarize", summarizer_agent)
    workflow.add_node("notify", notify_agent)

    workflow.set_entry_point("fetch")
    workflow.add_edge("fetch", "diff")
    workflow.add_edge("diff", "classify")
    workflow.add_edge("classify", "summarize")
    workflow.add_edge("summarize", "notify")

    return workflow.compile()
