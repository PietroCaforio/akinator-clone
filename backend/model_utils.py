import json
import joblib
import numpy as np

# Load model components
clf = joblib.load("./data/clf.pkl")
label_encoder = joblib.load("./data/label_encoder.pkl")

with open("./processed_characters.json") as f:
    characters = json.load(f)

X_columns = list(characters[0]["traits"].keys())

def get_question(node_id):
    """Return the question at a given node"""
    tree = clf.tree_
    if tree.feature[node_id] == -2:  # leaf node
        return None
    feature = X_columns[tree.feature[node_id]]
    return feature.replace("_", " ")

def go_to_next_node(node_id, answer_yes):
    """Traverse tree one step based on answer"""
    tree = clf.tree_
    return tree.children_right[node_id] if answer_yes else tree.children_left[node_id]

def get_prediction(node_id):
    """Return predicted class at leaf"""
    tree = clf.tree_
    class_id = np.argmax(tree.value[node_id])
    return label_encoder.inverse_transform([class_id])[0]
