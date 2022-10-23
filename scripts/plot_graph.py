from IPython.display import Image
from causalnex.plots import plot_structure, NODE_STYLE, EDGE_STYLE

def plot_sm_graph(sm):
    viz = plot_structure(
            sm,
            graph_attributes={"scale": "2.0", "size": 3.5},
            all_node_attributes=NODE_STYLE.WEAK,
            all_edge_attributes=EDGE_STYLE.WEAK,
        )
    return Image(viz.draw(format="png"))