import os
import sys

import constants

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator


os.environ["OPENAI_API_KEY"] = constants.APIKEY

if len(sys.argv) > 1:
    query = sys.argv[1]
else:
    query = input("Enter your query: ")


loader = TextLoader("/Users/Lemon/Desktop/Coding/YouCode-2024/backend/data/product_textfiles/Acrux_AR_Mountaineering_Boot.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

while True:
    query = input("You: ")

    if query.lower() == "stop":
        print("Goodbye!")
        break

print(index.query(query))



