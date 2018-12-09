from pyrlang import Node, GeventEngine, GenServer
from term import Atom
import pickle
import json


class PyGenServer(GenServer):
    def __init__(self, node):
        GenServer.__init__(self,
                           node_name=node.node_name_,
                           accepted_calls=["classify"])

        node.register_name(self, Atom("py_process"))

        self.model = pickle.load(open("./ML/iris_model.pickle", "rb"))

    def classify(self, encoded_params_to_classify):                  # 1
        params_to_classify = json.loads(encoded_params_to_classify)  # 2
        classification = self.model.predict([params_to_classify])[0] # 3
        encoded_classification = json.dumps(classification)          # 4
        return encoded_classification


def main():
    eng = GeventEngine()
    node = Node(node_name="py@127.0.0.1", cookie="PYEX", engine=eng)

    PyGenServer(node)

    eng.run_forever()


if __name__ == "__main__":
    main()
