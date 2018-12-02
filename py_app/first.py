from pyrlang import Node, GeventEngine
from term import Atom

def main():
    eng = GeventEngine()
    node = Node(node_name="py@127.0.0.1", cookie="PYEX", engine=eng)

    pid = node.register_new_process()

    node.send(sender=pid,
              receiver=(Atom("ex@127.0.0.1"), Atom("iex")),
              message=Atom("Hello from Python!"))

    eng.run_forever()

if __name__ == "__main__":
    main()
