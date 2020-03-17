from algorithm.aldous_broder import AldousBroder
from algorithm.binary_tree import BinaryTree
from algorithm.sidewinder import Sidewinder
from algorithm.wilsons import Wilsons


class AlgorithmFactory(object):
    names_to_algorithms = {"Aldous Broder": AldousBroder(),
                           "Binary Tree": BinaryTree(),
                           "Sidewinder": Sidewinder(),
                           "Wilsons": Wilsons()}
    default = AldousBroder()

    @property
    def options(self):
        return self.names_to_algorithms.keys()

    def get(self, algo_name):
        return self.names_to_algorithms.get(algo_name, self.default)
