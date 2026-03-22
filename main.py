from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import getpass
import os

load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

model = ChatOpenAI(model="gpt-4o-mini", base_url=os.environ.get("OPENROUTER_BASE_URL"))

# Template de prompt reutilizável
system_template = "Translate the following text from English to {language}."
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{text}")
])

# Exemplos para testar
examples = [
    {"language": "Português", "text": "Hello, how are you?"},
    {"language": "Italiano", "text": "What is your name?"},
    {"language": "Francês", "text": "Thank you very much."},
    {"language": "Espanhol", "text": "Good morning!"}
]

# Gerar prompts e enviar ao modelo
for example in examples:
    formatted_messages = prompt_template.format_messages(
        language=example["language"],
        text=example["text"]
    )
    response = model.invoke(formatted_messages)
    print(f"Idioma: {example['language']}")
    print(f"Texto original: {example['text']}")
    print(f"Tradução: {response.content}")
    print("-" * 40)