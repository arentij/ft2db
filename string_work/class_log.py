import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, p_object):
        super(LoggableList, self).append(p_object)
        self.log(p_object)

ll = LoggableList()
ll.append(1)
