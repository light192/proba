ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)

def convert_config_to_dict(config_filename):
    '''
    Функция преобразует файл конфигурации в словарь
    '''
    f = open(config_filename,'r')
    commands = f.read().split('\n')
    commands_dict = {}
    for command in commands:
        #print (command[:1])
        if command != "" and command[:1] != "!" and  not ignore_command(command,ignore):
            print(command)
            if command[:1] != " ":
                cmd_key = command
                commands_dict[cmd_key] = []
            else:
                commands_dict[cmd_key].append(command[1:])
    return commands_dict

print(convert_config_to_dict("config_sw1.txt"))
