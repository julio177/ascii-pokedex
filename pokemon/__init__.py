'''Base class and pokemon imports'''
class Pokemon():
    '''Base class for pokemon'''

    def __init__(self, filename):
        with open(filename) as f:
            content = f.readlines()
        found_description = False
        found_display = False
        self.name = ''
        self.number = -1
        self.description = ''
        self.draw = ''
        for line in content:
            #print(line, '')
            if 'number' in line:
                data = line.split(':')
                self.number = int(data[1])
            elif 'name' in line:
                data = line.split(':')
                self.name = str(data[1])

            elif 'description' in line:
                data = line.split(':')
                self.description = str(data[1]).replace(' ', '')
                found_description = True

            elif 'display' in line:
                found_description = False
                data = line.split(':')
                self.draw = str(data[1]).replace(' ', '')
                found_display = True

            elif found_description:
                self.description += str(line)

            elif found_display:
                self.draw += str(line)

    def __str__(self):
        return self.draw + "\n\n" + str(self.number) + " " + self.name + "\n" + self.description

    def set_name(self, name):
        '''Change pokemon name'''
        self.name = name

    def set_number(self, number):
        '''Change pokemon number'''
        self.number = number

    def set_description(self, description):
        '''Change pokemon description'''
        self.description = description

    def get_name(self):
        '''Get pokemon name'''
        return self.name

    def get_number(self):
        '''Get pokemon number'''
        return self.number

    def get_description(self):
        '''Get pokemon description'''
        return self.description
