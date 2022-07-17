import sys

class Log():
    def __init__(self,name):
        self.name = name
        self.log = open(self.name + ".txt", "w+")

    def append(self, data_stream):
        self.log.write(data_stream)
    def end_test(self):
        self.log.close()