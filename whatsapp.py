class WhatsappAnalyzer():

    def __init__(self, chat_file):
        self.chat_file = chat_file
        self.users = {}
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
            user_count = 0
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
                    import string
                    user = ''.join(ch for ch in user if ch.isalnum()).lower()
                if msg_search:
                    msg = msg_search.group(1)
                    msg = re.sub(r'[^\w\s]', '', msg)

                # if validly constructed message, save to object
                if date and user and msg:
                    if user not in self.users.values():
                        self.users[user_count] = user
                        user_count += 1
                    post = {
                        'date': date,
                        'user': [k for k,v in self.users.items() if v==user][0],
                        'message': msg
                    }
                    self.messages.append(post)

    def edit_user(self, user, new_name):
        """
        Edit the name of an existing user
        """
        if user in self.users.values():
            user_key = [k for k,v in self.users.items() if v==user][0]
            self.users[user_key] = new_name

    def message_count(self):
        """
        Calculate number of messages sent by each user
        """
        for user in self.users:
            count = len([x for x in self.messages if x['user'] == user])
            print("%s: %d" % (self.users[user], count))

    def top_words(self, user, n):
        """
        Get top n most commonly used words for user
        """
        if user in self.users.values():
            user_key = [k for k,v in self.users.items() if v==user][0]
            # get list of words
            all_msgs = " ".join([x['message'].lower() for x in self.messages if x['user'] == user_key])
            tokens = all_msgs.split(' ')

            # filter stop words
            from nltk.corpus import stopwords
            tokens = [word for word in tokens if word not in stopwords.words('english') and word != '']
            
            # create term-frequency pairs
            from collections import Counter
            return Counter(tokens).most_common(n)
        else:
            return None