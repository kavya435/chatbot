import json
from context_manager import ContextManager

class ChatBot:
    def __init__(self):
        with open("intents.json") as f:
            self.intents = json.load(f)

        self.context = ContextManager()

    def detect_intent(self, user_input):
        user_input = user_input.lower()
        for intent, data in self.intents.items():
            for keyword in data["keywords"]:
                if keyword in user_input:
                    return intent
        return "unknown"

    def generate_response(self, user_input):

        # 🔥 STEP 1: If input is number → use previous intent
        if user_input.isdigit():
            intent = self.context.get_intent()

            if intent == "track":
                self.context.set_intent(None)
                return f"Order {user_input} is out for delivery 🚚"

            elif intent == "cancel":
                self.context.set_intent(None)
                return f"Order {user_input} has been cancelled ❌"

            elif intent == "refund":
                self.context.set_intent(None)
                return f"Refund for order {user_input} initiated 💰"

            else:
                return "Please select option first (track/cancel/refund)"

        # 🔥 STEP 2: Detect intent
        intent = self.detect_intent(user_input)

        if intent != "unknown":
            self.context.set_intent(intent)

        # 🔥 STEP 3: Responses
        if intent == "greeting":
            return "Hello! How can I help you?"

        elif intent == "track":
            return "Please provide your order ID"

        elif intent == "cancel":
            return "Please provide your order ID to cancel"

        elif intent == "refund":
            return "Please provide your order ID for refund"

        elif intent == "goodbye":
            return "Thank you! Have a great day 😊"

        return "Sorry, I didn’t understand that. Please try again 😊"