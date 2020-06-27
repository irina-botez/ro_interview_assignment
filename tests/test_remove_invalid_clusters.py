import json
import unittest
from data_structures.datacenter import Datacenter


INVALID_CLUSTERS = ['BER-4000', 'TEST-1', 'XPAR-2']


def get_data():
    with open('response.json') as json_file:
        data = json.load(json_file)
        return [
            Datacenter(key, value)
            for key, value in data.items()
        ]


class TestRemoveClusters(unittest.TestCase):
    data = get_data()

    def test_remove_invalid_clusters(self):
        print("Start Remove Invalid Clusters Test...\n")

        valid_clusters = []

        for dc in self.data:
            print('\nRemoving DataCenter {}\'s invalid clusters\n...'.format(
                dc.name
            ))
            dc.remove_invalid_clusters()

            # keeping valid cluster names for later comparison
            valid_clusters += [c.name for c in dc.clusters]

        cluster_intersection = set(valid_clusters).intersection(
            INVALID_CLUSTERS
        )
        self.assertEqual(len(cluster_intersection), 0)


if __name__ == '__main__':
    unittest.main()

