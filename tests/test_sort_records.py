import unittest
from .get_test_data import get_data
from data_structures.entry import Entry


ORDERED_RECORDS = ['192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.4']


class TestRemoveRecords(unittest.TestCase):
    data = get_data()

    def test_ip_decimal_value(self):
        print("Start ip_to_decimal Test...\n")
        entry = Entry('192.168.203.20', True, '30/01/20 17:00:00')
        self.assertEqual(entry.ip_to_decimal(), 3232287508)

    def test_remove_invalid_clusters(self):
        print("Start Remove Invalid Records Test...\n")

        berlin_dc = self.data[0]
        test_cluster = berlin_dc.clusters[0]
        test_network = test_cluster.networks[0]

        # Remove invalid records first
        test_network.remove_invalid_records()

        # Sort records
        test_network.sort_records()
        post_order_records = [e.address for e in test_network.entries]

        # Compare results
        self.assertEqual(post_order_records, ORDERED_RECORDS)
