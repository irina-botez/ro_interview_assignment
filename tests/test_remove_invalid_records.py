import unittest
from .get_test_data import get_data
from datetime import datetime
from data_structures.network_collection import NetworkCollection
from data_structures.entry import Entry
from ipaddress import IPv4Network


# The addresses here are either invalid OR
# do not belong to the IPv4 network of the parent NetworkCollection object
INVALID_ADDRESSES = {
    '192.168.0.0/24': [
        '255.255.255.0',
        '192.168.0',
        '192.168..0.3',
        '192.168.0.288',
        'invalid',
    ],
    '10.0.8.0/22': [
        '10.0.12.1',
        '10.0.10.a',
    ],
    '192.168.11.0/24': [
        '192.168.2.1',
        '192.168.11.522',
    ],
    '192.168.203.0/24': [
        '192.168.0.0'
    ]
}


class TestRemoveRecords(unittest.TestCase):
    data = get_data()

    def check_entries(self, entries):
        print('\nChecking entries...\n')
        for entry in entries:
            self.assertIsInstance(entry, Entry)
            self.assertIs(type(entry.address), str)
            self.assertIs(type(entry.last_used), datetime)
            self.assertIs(type(entry.available), bool)

    def check_networks(self, networks):
        print('\nChecking networks...\n')
        for network in networks:
            self.assertIsInstance(network, NetworkCollection)
            self.assertIs(type(network.ipv4_network), IPv4Network)

    def test_remove_invalid_clusters(self):
        print("Start Remove Invalid Records Test...\n")

        for dc in self.data:
            print('\nLooking into DataCenter "{}"\n...'.format(
                dc.name
            ))
            dc.remove_invalid_clusters()

            for cluster in dc.clusters:
                print('\n\n\nDataCenter "{}" ---> Cluster "{}"\n'.format(
                    dc.name, cluster.name
                ))
                self.check_networks(cluster.networks)

                for network in cluster.networks:
                    print(
                        '\nRemoving invalid records for network {}...'
                        '\n'.format(network.ipv4_network)
                    )
                    network.remove_invalid_records()
                    net_address_str = str(network.ipv4_network)

                    self.check_entries(network.entries)

                    if net_address_str in INVALID_ADDRESSES.keys():
                        net_valid_addresses = [
                            e.address for e in network.entries
                        ]

                        address_intersection = set(
                            net_valid_addresses
                        ).intersection(INVALID_ADDRESSES[net_address_str])

                        self.assertEqual(len(address_intersection), 0)

            print('...\n\n')


if __name__ == '__main__':
    unittest.main()
