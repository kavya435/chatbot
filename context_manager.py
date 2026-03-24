class ContextManager:
    def __init__(self):
        self.intent = None

    def set_intent(self, intent):
        self.intent = intent

    def get_intent(self):
        return self.intent