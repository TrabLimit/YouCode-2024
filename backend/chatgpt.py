import os
import sys

import constants

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator


os.environ["OPENAI_API_KEY"] = constants.APIKEY

'''

if len(sys.argv) > 1:
    query = sys.argv[1]
else:
    query = input("Enter your query: ")


# loader = TextLoader("data.txt")
loader = DirectoryLoader("data/")
index = VectorstoreIndexCreator().from_loaders([loader])


print(index.query(query, llm = ChatOpenAI()))

'''



loader = DirectoryLoader("data/")
index = VectorstoreIndexCreator().from_loaders([loader])

while True:
    query = input("Hello! Enter prompt (or 'X' to exit): ")
    if query.strip().lower() == 'x':
        break
    print(index.query(query, llm=ChatOpenAI()))

print("Exiting the program.")






