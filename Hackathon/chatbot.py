from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a ChatBot instance
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on an English corpus
trainer.train('chatterbot.corpus.english')

# Start the conversation loop
while True:
    user_input = input("You: ")

    # Get a response from the chatbot
    response = chatbot.get_response(user_input)

    print("ChatBot:", response)
