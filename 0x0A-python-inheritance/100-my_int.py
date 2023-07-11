#!/usr/bin/python3
"""
MyInt Class
"""


class MyInt(int):
    """MyInt syb-class"""
    
    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        if isinstance(other, MyInt):
            if self.num == other.num:
                return False
        return True

    def __ne__(self, other):
        if isinstance(other, MyInt):
            if self.num != self.num:
                return False
        return True
