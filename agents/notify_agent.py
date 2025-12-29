from twilio.rest import Client
import os

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")

FROM_WHATSAPP = "whatsapp:+14155238886"
TO_WHATSAPP = os.getenv("TO_WHATSAPP")

def notify_agent(state):
    if not state["new_items"]:
        return state

    client = Client(TWILIO_SID, TWILIO_AUTH)

    for item in state["new_items"]:
        msg = f"""
            {item['type']} New Update

            Title: {item['title']}
            Source: {item['source']}

            Summary:
            {item.get('summary', 'N/A')}

            Link:
            {item['url']}
        """

        client.messages.create(
            body=msg,
            from_=FROM_WHATSAPP,
            to=TO_WHATSAPP
        )

    return state
