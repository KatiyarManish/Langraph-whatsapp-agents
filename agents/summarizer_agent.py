import ollama

def summarizer_agent(state):
    for item in state["new_items"]:
        try:
            # Fetch content (GitHub release body or blog page)
            content = ""
            if "github.com" in item["url"]:
                # GitHub release body already in title usually
                content = item["title"]
            else:
                content = item["title"]

            prompt = f"""
Summarize the following update in 3 bullet points.
Be concise and technical.

Content:
{content}
"""

            response = ollama.chat(
                model="llama3",
                messages=[{"role": "user", "content": prompt}]
            )

            summary = response["message"]["content"]
            item["summary"] = summary

        except Exception as e:
            item["summary"] = "Summary unavailable"

    return state
