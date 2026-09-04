# Block 01 — Types & Data Structures
# Examples from backend / AI development context

# ==============================
# BUILT-IN TYPES
# ==============================

# int — количество токенов в запросе к модели
max_tokens: int = 1024
prompt_tokens: int = 312
completion_tokens: int = 188

# float — температура модели (влияет на "случайность" ответа)
temperature: float = 0.7

# bool — флаги конфигурации
is_streaming: bool = True  # стримить ответ модели чанками или нет
use_cache: bool = False     # использовать ли кэш для этого запроса

# str — промпт для модели
system_prompt: str = "You are a helpful medical assistant."

# None — модель ещё не ответила
last_response = None

# f-string — формируем лог
user_id = "u_123"
print(f"Request from user {user_id}: {prompt_tokens} prompt tokens")


# ==============================
# LIST — упорядоченный изменяемый
# ==============================

# История сообщений в чате с моделью
chat_history = [
    {"role": "user", "content": "What does my insurance cover?"},
    {"role": "assistant", "content": "Your plan covers..."},
    {"role": "user", "content": "What about dental?"},
]

# Добавляем новое сообщение
chat_history.append({"role": "assistant", "content": "Dental is covered up to $500/year."})

# Последнее сообщение
last_message = chat_history[-1]

# Только последние 10 сообщений (контекстное окно)
context_window = chat_history[-10:]


# ==============================
# TUPLE — упорядоченный неизменяемый
# ==============================

# Поддерживаемые модели — не меняются в рантайме
SUPPORTED_MODELS = ("gpt-4o", "claude-sonnet", "gemini-pro")

# Координаты в векторном пространстве (embedding)
vector_2d = (0.823, -0.412)

# Распаковка — получаем размерность эмбеддинга и имя модели
embedding_dim, model_name = (1536, "text-embedding-3-small")


# ==============================
# DICT — пары ключ-значение
# ==============================

# Метаданные документа в RAG системе
document = {
    "id": "doc_001",
    "source": "insurance_policy_2024.pdf",
    "chunk_index": 3,
    "content": "Dental coverage includes...",
    "embedding_model": "text-embedding-3-small",
}

# Безопасное получение — не упадёт если ключа нет
author = document.get("author")  # → None

# Конфигурация подключения к векторной БД
qdrant_config = {
    "host": "localhost",
    "port": 6333,
    "collection": "insurance_docs",
    "vector_size": 1536,
}


# ==============================
# SET — уникальные элементы
# ==============================

# Уникальные источники документов в результатах поиска
search_results = [
    {"source": "policy_2024.pdf", "score": 0.91},
    {"source": "faq.pdf", "score": 0.87},
    {"source": "policy_2024.pdf", "score": 0.85},  # дубль
]
unique_sources = {result["source"] for result in search_results}
# → {"policy_2024.pdf", "faq.pdf"}

# Быстрая проверка — поддерживается ли формат файла
SUPPORTED_FORMATS = {"pdf", "docx", "txt", "md"}
uploaded_file = "report.pdf"
if uploaded_file.split(".")[-1] in SUPPORTED_FORMATS:
    print("Format supported")


# ==============================
# COMPREHENSIONS
# ==============================

# List comprehension — достаём только content из истории чата
messages_text = [msg["content"] for msg in chat_history]

# С условием — только сообщения от пользователя
user_messages = [msg["content"] for msg in chat_history if msg["role"] == "user"]

# Название модели и максимальный размер её контекстного окна в токенах
model_limits = {
    "gpt-4o": 128000,
    "claude-sonnet": 200000,
    "gemini-pro": 1000000,
}
# Фильтруем — только модели с контекстом больше 100k
large_context_models = {
    name: tokens
    for name, tokens in model_limits.items()
    if tokens > 100000
}


# ==============================
# UNPACKING
# ==============================

# Первый и остальные чанки документа
first_chunk, *remaining_chunks = ["intro text", "chunk 2", "chunk 3", "chunk 4"]

# Получаем host и port из конфига
host, port = qdrant_config["host"], qdrant_config["port"]