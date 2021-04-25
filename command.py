class Command:
    commandList = []

    def toInt(self, str):
        return int(str)

    def toFloat(self, str):
        return float(str)

    def toBoolean(self, str):
        if str == 'true':
            return True
        elif str == 'false':
            return False
        return 100

    def register(self, name, sub, func):
        self.commandList.append({'name':name, 'sub':sub, 'function':func})

    def handleCommands(self):
        receivedCommand = input('> ').split()
        for i in self.commandList:
            if receivedCommand[0] == '/' + i['name']:
                parsedSubs = []
                largeCount = 0
                for j in receivedCommand[1:]:
                    smallCount = 0
                    for k in i['sub'].items():
                        if largeCount == smallCount:
                            if k[1] == 'integer':
                                parsedSubs.append(self.toInt(j))
                            elif k[1] == 'float':
                                parsedSubs.append(self.toFloat(j))
                            elif k[1] == 'boolean':
                                parsedSubs.append(self.toBoolean(j))
                            elif k[1] == 'string':
                                parsedSubs.append(j)
                            smallCount+=1
                        else:
                            smallCount+=1
                            continue
                    largeCount+=1
                i['function'](parsedSubs)



if __name__ == '__main__':
    def cHelp(args):
        global command
        for i in command.commandList:
            if i['name'] == args[0]:
                print('/{}'.format(i['name']), end=' ')
                for j in i['sub'].items():
                    print('<{}:{}>'.format(j[0], j[1]), end=' ')
            print(' ')

    def test_function(args):
        for i in range(args[0]):
            print(args[1])

        if args[2] == True:
            print('pooof')

    def add(args):
        sum = args[0] + args[1]
        print('sum: {}'.format(sum))

    command = Command()

    command.register('help', {'command':'string'}, cHelp)
    command.register('test', {'num':'integer', 'float':'float', 'bool':'boolean'}, test_function)
    command.register('add', {'num1':'integer', 'num2':'integer'}, add)

    command.handleCommands()
