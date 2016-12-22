import vk_api
import operator

class VKMSGStat:

    def __init__(self, login, password):
        """
        Allows to get simple statistics of messages in VK
        :param login: VK login
        :type login: str
        :param password: VK password
        :type password: str
        """

        # Create session
        self.__vk_session = vk_api.VkApi(login, password)

        #Problems flag
        self.noProblem = True

        self.__toPrint = ""

        try:
            #Try to authorize
            self.__vk_session.authorization()
            self.__tools = vk_api.VkTools(self.__vk_session)
            self.__vk = self.__vk_session.get_api()

        except vk_api.AuthorizationError as error_msg:
            self.noProblem = False

    def getUserStats(self, userID):
        """
        Return stats for current user
        :param userID: VK userID
        :type userID: int
        :return: Dict with stats
        :rtype: dict
        """
        return self.__getStats(userID)

    def getChatStats(self, chatID):
        """
        Return stats for current chat
        :param chatID: VK chat ID
        :type chatID: int
        :return: Dict with stats
        :rtype: dict
        """
        return self.__getStats(2000000000+chatID)

    #Send the request and creates result array
    def __getStats(self, profileNum):

        #Get the result from API
        messages = self.__tools.get_all('messages.getHistory', 100, {'count': 200, 'peer_id': profileNum})

        self.stats = {}
        self.stats['count'] = messages['count']
        self.stats['people'] = {}

        #Calculate the messages
        for num in range(0, messages['count']):
            from_id = messages['items'][num]['from_id']
            if from_id in self.stats['people']:
                self.stats['people'][from_id]['count'] += 1
            else:
                self.stats['people'][from_id] = {}
                self.stats['people'][from_id]['count'] = 1

        #Create stats array
        for key, value in self.stats['people'].items():
            human = self.__vk.users.get(user_ids=key)[0]
            self.stats['people'][key]['user'] = human['first_name'] + " " + human['last_name']

        #Create system array just for printing
        self.__result = {}

        for key, value in self.stats['people'].items():
            self.__result[value['count']] = "%s - %s (%.1f%%)" % (
            value['user'], '{:,}'.format(value['count']).replace(',', ' '), 100.0 * float(value['count']) / float(self.stats['count']))

        #Formate the string to print
        self.__toPrint = "Total - %s" % '{:,}'.format(self.stats['count']).replace(',', ' ') + "\n"

        for key, value in reversed(sorted(self.__result.items(), key=operator.itemgetter(0))):
            self.__toPrint += "%s\n" % value

        #Return the dict
        return self.stats

    #Prints the result
    def printStats(self):
        print(self.__toPrint)