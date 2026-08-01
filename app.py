from src.router import router_node
import json

# from src.state import NewsGenieState
# from src.workflow import graph
import src.news_api

# state: NewsGenieState = {
#     "query": "What is machine learning?",
#     "query_type": "",
#     "category": "",
#     "response": "",
#     "error": "",
# }


# updated_state = graph.invoke(state)


# print(updated_state)
from src.news_api import fetch_news

# fetch news articles about technology
technology_news = fetch_news("technology")


with open("news_response.json", "w") as file:
    json.dump(technology_news, file, indent=4)

print("Saved news_response.json")
