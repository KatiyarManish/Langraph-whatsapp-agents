def classify_agent(state):
    for item in state["new_items"]:
        if "release" in item["source"].lower():
            item["type"] = "🚀 Release"
        elif "blog" in item["source"].lower():
            item["type"] = "📝 Blog"
        else:
            item["type"] = "📄 Update"

    return state
