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
    query0 = input( '\033[96m'+ "Are you satisfied with renting " + sys.argv[1] + "? (Y/N): " + '\033[0m')
else:
    product = "YOLA COAT WOMEN'S, GALENA, SIZE XS"
    query0 = input("Are you satisfied with your rental? (Y/N): ")



while True:    
    if query0.strip().lower() == 'y':
        query1 = input("Would you like to purchase your product? (Y/N): ")
        break
    elif query0.strip().lower() == 'n':
        print("We're sorry to hear! Here is some other recommendation:\n")
        query1 = "what are some other related items to " + product + "? Provide one related item with name, color, size, price and year (and those info only)."
        print(index.query(query1, llm))
        break
    else:
        query0 = input("Invalid input. Please answer in either 'Y' or 'N': ")


while True:
    if query1.strip().lower() == 'y':
        print("Thank you! Your product has been added to the cart.\n View cart: https://www.regear.arcteryx.com/cart")
        break
    elif query1.strip().lower() == 'n':
        query2 = input("We're sorry. Mind if we know what could be changed or improved?: Select 1 for COST, 2 for FIT and 3 for COLOR. \n")
        break
    else:
        query1 = input("Invalid input. Please answer in either 'Y' or 'N': ")


while True:
    if query2.strip().lower() == '2':
        print("Let's see if we have something that you like:\n")
        query3 = "check if there is other related clothing as" + product.split(",")[0] + "but in smaller size. It does NOT have to be EXACT match. Provide its name, size, color, price, and link (and those only)." 
        print(index.query(query3, llm))
        break
    elif query2.strip().lower() == '1':
        print("Let's see if we have something that you like:\n")
        query3 = "check if there is other related clothing as" + product.split(",")[0] + "but cheaper. It does NOT have to be EXACT match. provide its name, size, color, price, and link (and those only).'"
        print(index.query(query3, llm))
        break
    elif query2.strip().lower() == '3':
        print("Let's see if we have something that you like:\n")
        query3 = "check if there is other related clothing as " + product.split(",")[0] + product.split(",")[2] + ", but NOT in " + product.split(",")[1] + ". It does NOT have to be EXACT match. Provide its name, size, color, price, and link (and those only).'"
        print(index.query(query3, llm))
        break
    else:
        query2 = input("Invalid input. Please answer in either '1' or '2' or '3': ")









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






