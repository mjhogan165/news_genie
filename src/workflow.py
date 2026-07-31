from langgraph.graph import StateGraph, START, END

from src.router import router_node
from src.state import NewsGenieState

# Define the workflow graph Because every node will receive that state.
graph_builder = StateGraph(NewsGenieState)
# register the router node
graph_builder.add_node("router", router_node)
graph_builder.add_edge(START, "router")
graph_builder.add_edge("router", END)
graph = graph_builder.compile()
