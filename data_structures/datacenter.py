import re
from .cluster import Cluster


class Datacenter:
    def __init__(self, name, cluster_dict):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """

        self.name = name

        self.clusters = [
            Cluster(
                name=key,
                security_level=value['security_level'],
                network_dict=value['networks']
            )
            for key, value in cluster_dict.items()
        ]

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """
        valid_cluster_start = self.name[:3].upper()
        re_string = r'^{}-\d{{1,3}}$'.format(valid_cluster_start)
        pattern = re.compile(re_string)

        clusters = self.clusters
        to_remove = []

        for cluster in clusters:
            if not pattern.match(cluster.name):
                to_remove.append(cluster.name)

        self.clusters = list(
            filter(lambda x: x.name not in to_remove, clusters)
        )
