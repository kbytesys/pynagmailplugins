from .common import MailQueueInterface, MailQueueParsingError

class PostfixMailQueue(MailQueueInterface):

    def __init__(self, data_generator):
        super(PostfixMailQueue, self).__init__(data_generator)
        self.deferred = 0
        self.active = 0
        self.total = 0

    def get_deferred_counter(self):
        return self.deferred

    def get_active_counter(self):
        return self.active

    def get_total_counter(self):
        return self.total

    def update(self):

        mailq_output = self.data_generator()

        self.deferred = 0
        self.active = 0
        self.total = 0

        for line in mailq_output.split('\n'):
            if line is None or len(line) == 0 or line[0] not in "0123456789ABCDEF":
                continue

            queue_item = line.split(' ')
            queue_item_id = queue_item[0]

            self.total += 1

            if queue_item_id.endswith('*'):
                self.active += 1
            elif queue_item_id.endswith('!'):
                pass
            else:
                self.deferred += 1


