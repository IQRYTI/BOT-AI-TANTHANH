from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Khởi tạo ChatBot với tên là "TanThanhBot"
bot = ChatBot(
    'TanThanhBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri=None,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Xin lỗi, tôi không hiểu câu hỏi của bạn.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ]
)

# Sử dụng ChatterBotCorpusTrainer để train bot với các bộ dữ liệu sẵn có
trainer = ChatterBotCorpusTrainer(bot)

# Train bot với các bộ dữ liệu mẫu tiếng Anh và tiếng Việt
trainer.train(
    'chatterbot.corpus.vietnamese',
    'chatterbot.corpus.english'
)

# Hàm để bot có thể giao tiếp với người dùng
def chat():
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = bot.get_response(user_input)
        print('TanThanhBot:', response)

# Gọi hàm chat để bot bắt đầu giao tiếp
if __name__ == "__main__":
    chat()