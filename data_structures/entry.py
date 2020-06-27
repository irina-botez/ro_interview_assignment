from datetime import datetime


class Entry:
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """

        self.address = address
        self.available = available
        self.last_used = datetime.strptime(last_used, "%d/%m/%y %H:%M:%S")

    def ip_to_decimal(self):
        '''
        The formula looks like this:
        a:b:c:d = a(256)^3 + b(256)^2 + c(256)^1 + d.

        Ref: itstillworks.com/convert-ip-addresses-decimal-format-7611714.html
        '''

        blocks = self.address.split('.')
        decimal = 0
        for idx, block in enumerate(blocks):
            decimal += 256**(3-idx) * int(block)

        return decimal

    def __lt__(self, other):
        """Custom decimal value comparator"""
        return self.ip_to_decimal() < other.ip_to_decimal()
