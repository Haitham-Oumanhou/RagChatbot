
## How Does it work :


### The vector Database :


We use a Chroma vector database , created using the script `create_vector_db.py`, where chunks are stored as Embeddings (vectors). For that purpose we use HuggingFace embeddings, which are easy to access and use. vector databases enable us to use similarity search to find relevant knowledge to our prompts.

We indexed several pdf files in the `documents` directory using a langchain integration of BeautifulSoup and Unstructured libraries.


## How to run the files


This project uses poetry for dependency management.Once poetry is installed, from the root directory of the project ,use the following command to prepare and activate a virtual environment  :

```
poetry install
poetry shell

```

### run the streamlit app 

```
streamlit run  .\chatbot\front.py
```

### run a console chatbot

```
python  .\chatbot\chatbot.py
```



