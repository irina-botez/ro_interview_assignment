import re
from ipaddress import IPv4Address, IPv4Network
from .entry import Entry


class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """

        self.ipv4_network = IPv4Network(ipv4_network)
        self.entries = [
            Entry(
                address=entry['address'],
                available=entry['available'],
                last_used=entry['last_used']
            )
            for entry in raw_entry_list
        ]

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """
        to_remove = []
        nr_block = '[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]'
        re_string = r'^({0})\.({0})\.({0})\.({0})$'.format(nr_block)
        pattern = re.compile(re_string)

        for entry in self.entries:
            invalid = False

            if not pattern.match(entry.address) :
                invalid = True
            if not invalid and \
               IPv4Address(entry.address) not in self.ipv4_network:
                invalid = True

            if invalid:
                to_remove.append(entry.address)
                continue

        self.entries = list(filter(
            lambda x: x.address not in to_remove, self.entries
        ))


    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)
