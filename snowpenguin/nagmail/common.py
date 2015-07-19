from abc import ABCMeta, abstractmethod

class MailQueueParsingError(Exception):
    def __init__(self, msg):
        super(MailQueueParsingError, self).__init__(msg)

class MailQueueInterface(metaclass=ABCMeta):

    def __init__(self, data_generator):
        self.data_generator = data_generator

    @abstractmethod
    def get_deferred_counter(self):
        pass

    @abstractmethod
    def get_active_counter(self):
        pass

    @abstractmethod
    def get_total_counter(self):
        pass

    @abstractmethod
    def update(self):
        pass
