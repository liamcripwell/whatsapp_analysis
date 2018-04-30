class WhatsappAnalyzer():

    def __init__(self, chat_file):
        self.chat_file = chat_file
        self.users = []
        self.messages = []                

    def parse(self):
        import re

        date_regex = "^\[(.*)\]"
        user_regex = "^\[.*\] (.*):"
        msg_regex = "^\[.*\] .*: (.*)$"

        with open(self.chat_file) as f:
            for line in f:
                date_search = re.search(date_regex, line)
                user_search = re.search(user_regex, line)
                msg_search = re.search(msg_regex, line)

                if date_search:
                    date = date_search.group(1)
                if user_search:
                    user = user_search.group(1)
                if msg_search:
                    msg = msg_search.group(1)

                post = (date, user, msg)
                print(post)
                self.messages.append(post)
