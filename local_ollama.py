import ollama

MODEL = "llama3.2"

def chat_with_ollama():
    messages = []
    print("💬 Ollama Chatbot (type 'exit' to quit)\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        
        messages.append({"role": "user", "content": user_input})
        
        try:
            response = ollama.chat(model=MODEL, messages=messages)
            reply = response['message']['content']
            print("🤖 Ollama:", reply, "\n")
            
            # Keep conversation history
            messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            print(f"❌ Error: {e}")

# ✅ Run chatbot
chat_with_ollama()
