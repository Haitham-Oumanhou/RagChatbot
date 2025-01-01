## How Does it work :

### The vector Database :

We use a Chroma vector database (stored in `vector_db` directory), created using the script `create_vector_db.py`, where chunks are stored as Embeddings (vectors). For that purpose we use HuggingFace embeddings, which are easy to access and use. vector databases enable us to use similarity search to find relevant knowledge to our prompts.

We indexed several pdf files in the `documents` directory using a langchain integration of BeautifulSoup and Unstructured libraries.

## How to run the files

### Preparations

This project uses poetry for dependency management, please refer to their [website](https://python-poetry.org/docs/) in order to install it.

Once poetry is installed, from the root directory of the project ,use the following command to prepare and activate a virtual environment :

```
poetry install
poetry shell
```

Before being able to run the code, you need to either have an [OPENAI API KEY](https://platform.openai.com/api-keys) or a [HUGGINGFACE API TOKEN](https://huggingface.co/settings/tokens).

You can either add these in your environment variables, using the names `OPENAI_KEY` or `HUGGINFACEHUB_API_TOKEN`
or you can put them in config.py in the designated place :

```
OPENAI_KEY = os.getenv("OPENAI_KEY", "your key")
HUGGINFACEHUB_API_TOKEN = os.getenv("HUGGINFACEHUB_API_TOKEN", "your token")
```

For each provider, you need to change `LLM_PROVIDER` in `config.py` accordinly

```
providers = ["openai","huggingface"]
LLM_PROVIDER = "your provider from the list"
```

### run the streamlit app

in a terminal where the poetry env is activated, make sure that you are in the root directory of the project, some directory names variables won't work otherwise, then :

```
streamlit run  .\chatbot\front.py
```

to stop the app you need to press `ctrl+c` in the used terminal

### run a console chatbot

in a terminal where the poetry env is activated, make sure that you are in the root directory of the project, some directory names variables won't work otherwise, then :

```
python  .\chatbot\chatbot.py
```

to stop the app you can either input `q` or `quit`.
