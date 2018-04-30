class WhatsappAnalyzer():

    def __init__(self, chat_file):
        self.chat_file = chat_file
        self.users = []
        self.messages = []                

    def parse(self):
        """
        Parse each line of chat_file and identify date, user and message content from each
        """
        import re

        # regex patters for finding each component
        date_regex = "^\[(.*)\]"
        user_regex = "^\[.*\] ([^:]*):"
        msg_regex = "^\[.*\] [^:]*: (.*)$"

        with open(self.chat_file) as f:
            for line in f:
                # search for components
                date_search = re.search(date_regex, line)
                user_search = re.search(user_regex, line)
                msg_search = re.search(msg_regex, line)

                # if found, save to memory
                if date_search:
                    date = date_search.group(1)
                if user_search:
                    user = user_search.group(1)
                if msg_search:
                    msg = msg_search.group(1)

                # if validly constructed message, save to object
                if date and user and msg:
                    post = (date, user, msg)
                    if user not in self.users:
                        self.users.append(user)
                    self.messages.append(post)

    def message_count(self):
        """
        Calculate number of messages sent by each user
        """
        for user in self.users:
            count = len([x for x in self.messages if x[1] == user])
            print("%s: %d" % (user, count))
