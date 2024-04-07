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


loader = TextLoader("data/erasethis.txt")
# loader = DirectoryLoader("data/")
index = VectorstoreIndexCreator().from_loaders([loader])


print(index.query(query, llm = ChatOpenAI()))
'''

loader = TextLoader("data/erasethis.txt")
# loader = DirectoryLoader("data/")
index = VectorstoreIndexCreator().from_loaders([loader])

product = ""
llm = ChatOpenAI()

if len(sys.argv) > 1:
    product = sys.argv[1]
    query0 = input("Are you satisfied with renting " + sys.argv[1] + "? (Y/N): ")
else:
    product = "YOLA COAT WOMEN'S, GALENA, SIZE XS"
    query0 = input("Are you satisfied with your rental? (Y/N): ")



while True:    
    if query0.strip().lower() == 'y':
        query1 = input("Would you like to purchase your product? (Y/N):")
        break
    elif query0.strip().lower() == 'n':
        print("We're sorry to hear! Here is some other recommendation:\n")
        query2 = "what are some other related items to " + product + "? Provide one related item with name, color, size, price and year (and those info only)."
        print(index.query(query2, llm))
        break
    else:
        query0 = input("Invalid input. Please answer in either 'Y' or 'N': ")





#print(index.query(query, llm = ChatOpenAI()))








'''

loader = DirectoryLoader("data/")
index = VectorstoreIndexCreator().from_loaders([loader])

while True:
    query = input("Hello! Enter prompt (or 'X' to exit): ")
    if query.strip().lower() == 'x':
        break
    print(index.query(query, llm=ChatOpenAI()))

print("Exiting the program.")\

'''






