import requests
import time
from data_structures.datacenter import Datacenter


URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.
​
    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """
    while max_retries > 0:
        try:
            req = requests.get(url=url)
            req.raise_for_status()
            return req.json()
        except requests.exceptions.RequestException as e:
            print("\nAttempt {} of 5 FAILED: {}\n".format(6-max_retries, e))
            time.sleep(delay_between_retries)
            max_retries -= 1

    return None


def main():
    """
    Main entry to our program.
    """

    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')

    datacenters = (
        Datacenter(key, value)
        for key, value in data.items()
    )

    for dc in datacenters:
        dc.remove_invalid_clusters()


if __name__ == '__main__':
    main()
