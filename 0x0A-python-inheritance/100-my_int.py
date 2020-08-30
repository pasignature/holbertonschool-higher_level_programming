#!/usr/bin/python3
"""My Integer Module"""


class MyInt(int):
    """MyInt custom int class"""

    def __eq__(self, other):
        """Equality comparison"""

        return not super().__eq__(other)

    def __ne__(self, other):
        """Equality comparison"""

        return not super().__ne__(other)
