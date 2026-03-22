# Introdução aos LLMs com LangChain - Aula 2

Este projeto faz parte dos estudos do curso **Formação em IA**, oferecido pelo Instituto ECOA PUC-Rio em parceria com o Serratec. O objetivo é explorar o uso de Large Language Models (LLMs) através da biblioteca LangChain para tarefas de tradução de texto.

## Descrição

O projeto demonstra como utilizar o LangChain para interagir com modelos de linguagem, especificamente para traduzir textos do inglês para outros idiomas. Utiliza a API do OpenRouter para acessar modelos como o GPT-4o-mini, permitindo uma integração flexível e acessível.

## Funcionalidades

- Tradução de texto usando LLMs
- Suporte a múltiplos idiomas de destino
- Uso de templates de prompt reutilizáveis com `ChatPromptTemplate`
- Configuração via variáveis de ambiente

## Pré-requisitos

- Python 3.11 ou superior
- Conta no OpenRouter (para obter chave da API)
- Ambiente virtual (Pipenv recomendado)

## Instalação

1. Clone o repositório:

   ```
   git clone https://github.com/Diogooliveira10/langchain-llm-translator
   cd langchain-llm-translator
   ```

2. Ative o ambiente virtual:

   ```
   pipenv shell
   ```

3. Instale as dependências:
   ```
   pip install langchain langchain-openai python-dotenv
   ```

## Configuração

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
OPENAI_API_KEY=sk-or-v1-sua-chave-aqui
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```

- `OPENAI_API_KEY`: Sua chave da API do OpenRouter
- `OPENROUTER_BASE_URL`: URL base para a API do OpenRouter

## Uso

Execute o script principal:

```
python main.py
```

O script irá carregar as variáveis do `.env` e executar uma tradução de exemplo.

Para personalizar traduções, modifique o código para usar diferentes idiomas e textos.

## Estrutura do Projeto

- `main.py`: Script principal com exemplo de tradução
- `.env`: Arquivo de configuração (não versionado)
- `README.md`: Este arquivo

## Contribuição

Este é um projeto educacional. Para sugestões ou melhorias, abra uma issue no repositório.
