from .network_collection import NetworkCollection


class Cluster:
    def __init__(self, name, network_dict, security_level):
        """
        Constructor for Cluster data structure.

        self.name -> str
        self.security_level -> int
        self.networks -> list(NetworkCollection)
        """

        self.name = name
        self.security_level = security_level

        self.networks = [
            NetworkCollection(
                ipv4_network=key,
                raw_entry_list=value
            )
            for key, value in network_dict.items()
        ]