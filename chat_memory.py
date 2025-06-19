class ChatMemory:
    def __init__(self, window_size=3):
        self.window_size = window_size
        self.history = []

    def add_turn(self, user_input, bot_response):
        self.history.append((user_input, bot_response))
        if len(self.history) > self.window_size:
            self.history.pop(0)

    def get_context(self):
        context = ""
        for user, bot in self.history:
            context += f"User: {user}\nBot: {bot}\n"
        return context