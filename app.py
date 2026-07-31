from src.router import router_node
from src.state import NewsGenieState
from src.workflow import graph

state: NewsGenieState = {
    "query": "What is machine learning?",
    "query_type": "",
    "category": "",
    "response": "",
    "error": "",
}


updated_state = graph.invoke(state)


print(updated_state)
