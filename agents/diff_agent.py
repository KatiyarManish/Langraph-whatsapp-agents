from db import is_new

def diff_agent(state):
    new_items = []

    for item in state["items"]:
        if is_new(item["url"], item["title"], item["source"]):
            new_items.append(item)

    state["new_items"] = new_items
    return state
