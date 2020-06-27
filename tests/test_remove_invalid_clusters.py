import unittest
from .get_test_data import get_data
from data_structures.cluster import Cluster
from data_structures.datacenter import Datacenter


INVALID_CLUSTERS = ['BER-4000', 'TEST-1', 'XPAR-2']


class TestRemoveClusters(unittest.TestCase):
    data = get_data()

    def check_datacenter(self, datacenter):
        print('\nChecking DataCenter type...\n')
        self.assertIsInstance(datacenter, Datacenter)

    def check_clusters(self, clusters):
        print('\nChecking clusters...\n')
        for cluster in clusters:
            self.assertIsInstance(cluster, Cluster)
            self.assertIs(type(cluster.security_level), int)
            self.assertIs(type(cluster.name), str)

    def test_remove_invalid_clusters(self):
        print("Start Remove Invalid Clusters Test...\n")

        valid_clusters = []

        for dc in self.data:
            print('\nRemoving DataCenter {}\'s invalid clusters...\n'.format(
                dc.name
            ))
            self.check_datacenter(dc)
            self.check_clusters(dc.clusters)

            dc.remove_invalid_clusters()
            # keeping valid cluster names for later comparison
            valid_clusters += [c.name for c in dc.clusters]

        cluster_intersection = set(valid_clusters).intersection(
            INVALID_CLUSTERS
        )
        self.assertEqual(len(cluster_intersection), 0)


if __name__ == '__main__':
    unittest.main()
