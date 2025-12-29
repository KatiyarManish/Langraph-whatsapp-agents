from dotenv import load_dotenv
load_dotenv()

from graph import build_graph
from db import init_db


print("🔥 main.py started")

if __name__ == "__main__":
    init_db()
    print("✅ DB initialized")

    app = build_graph()
    print("🧠 Graph built")

    app.invoke({})
    print("🚀 Graph execution finished")
