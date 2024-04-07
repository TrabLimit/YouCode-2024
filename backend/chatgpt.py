from flask import Flask, request, jsonify
from flask_cors import CORS


import os
import sys

import constants

from langchain_openai import ChatOpenAI
# from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator


os.environ["OPENAI_API_KEY"] = constants.APIKEY

app = Flask(__name__)
CORS(app)

@app.route('/query', methods=['POST'])

def query():
    try:
        data = request.json
        query = data['query']
        
        loader = TextLoader("data/erasethis.txt")
        # loader = DirectoryLoader("data/")
        index = VectorstoreIndexCreator().from_loaders([loader])
        
        response = index.query(query, llm=ChatOpenAI())
        
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


# loader = TextLoader("data/erasethis.txt")
# # loader = DirectoryLoader("data/")
# index = VectorstoreIndexCreator().from_loaders([loader])

# product = ""
# llm = ChatOpenAI()

# if len(sys.argv) > 1:
#     product = sys.argv[1]
#     query0 = input("Are you satisfied with renting " + sys.argv[1] + "? (Y/N): ")
# else:
#     product = "YOLA COAT WOMEN'S, GALENA, SIZE XS"
#     query0 = input("Are you satisfied with your rental? (Y/N): ")



# while True:    
#     if query0.strip().lower() == 'y':
#         query1 = input("Would you like to purchase your product? (Y/N):")
#         break
#     elif query0.strip().lower() == 'n':
#         print("We're sorry to hear! Here is some other recommendation:\n")
#         query2 = "what are some other related items to " + product + "? Provide one related item with name, color, size, price and year (and those info only)."
#         print(index.query(query2, llm))
#         break
#     else:
#         query0 = input("Invalid input. Please answer in either 'Y' or 'N': ")


# #print(index.query(query, llm = ChatOpenAI()))

