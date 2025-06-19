from model_loader import load_chat_model
from chat_memory import ChatMemory
import accelerate

def main():
    print("Welcome to the Local Chatbot! Type /exit to quit.\n")
    
    generator = load_chat_model()
    memory = ChatMemory(window_size=3)

    while True:
        user_input = input("User: ")
        if user_input.lower() == "/exit":
            print("Bot: Exiting chatbot. Goodbye!")
            break

        prompt = memory.get_context() + f"User: {user_input}\nAssistant:"
        response = generator(
            prompt,
            max_new_tokens=128,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7
        )

        bot_output = response[0]['generated_text'][len(prompt):].strip().split("\n")[0]

        print(f"Bot: {bot_output}")
        memory.add_turn(user_input, bot_output)

if __name__ == "__main__":
    main()