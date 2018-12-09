from pyrlang import Node, GeventEngine, GenServer
from term import Atom


class PyGenServer(GenServer):
    def __init__(self, node):
        GenServer.__init__(self,
                           node_name=node.node_name_,
                           accepted_calls=["upperise"])

        node.register_name(self, Atom("py_process"))

    def upperise(self, string):
        return string.upper()


def main():
    eng = GeventEngine()
    node = Node(node_name="py@127.0.0.1", cookie="PYEX", engine=eng)

    PyGenServer(node)

    eng.run_forever()


if __name__ == "__main__":
    main()
