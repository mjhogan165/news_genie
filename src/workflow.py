from langgraph.graph import END, START, StateGraph

from src.router import router_node
from src.state import NewsGenieState
from src.chatbot import chatbot_node

# Create the workflow graph.
# Every node in this graph will receive a NewsGenieState object.
# This does NOT create a graph with nodes, its an empty graph
graph_builder = StateGraph(NewsGenieState)

# Register the router node with the graph.
graph_builder.add_node("router", router_node)
graph_builder.add_node("chatbot", chatbot_node)
# Define the execution flow.
graph_builder.add_edge(START, "router")
graph_builder.add_edge("router", "chatbot")
graph_builder.add_edge("chatbot", END)

# Build the finished graph.
graph = graph_builder.compile()
