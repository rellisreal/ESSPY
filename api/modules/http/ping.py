from pythonping import ping
from api.model.target import Target


class Ping:
    def __init__(self, target: Target, count: int = 4):
        self.target = target
        self.count  = count
    
    def ping_ipv4(self):
        return self.__ping_target(self.target.ipv4, self.count)

    def ping_ipv6(self):
        return self.__ping_target(self.target.ipv6, self.count)
    
    def ping_host_name(self):
        return self.__ping_target(self.target.hostName, self.count)
    
    def __ping_target(self, target, count):
        pingOutput = ping(target, verbose=True, count=count)
        return pingOutput
        