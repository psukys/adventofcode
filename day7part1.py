class Operations:
    AND = staticmethod(lambda var1, var2: var1 & var2)
    OR = staticmethod(lambda var1, var2: var1 | var2)
    NOT = staticmethod(lambda var: ~ var & 0xffff)
    LSHIFT = staticmethod(lambda var1, var2: var1 << var2)
    RSHIFT = staticmethod(lambda var1, var2: var1 >> var2)
    ASSIGN = staticmethod(lambda var: var)


class Wire:
    name = ''
    inputs = []
    operation = None

    def __init__(self, name):
        self.name = name

    def resolve(self):
        for i in xrange(len(self.inputs)):
            if type(self.inputs[i]) is not int:
                self.inputs[i] = self.inputs[i].resolve()
        return self.output()

    def output(self):
        if len(self.inputs) == 1:
            return self.operation(self.inputs[0])
        elif len(self.inputs) == 2:
            return self.operation(self.inputs[0], self.inputs[1])
        else:
            print('There are more than 2 input variables in {0}'.format(self.name))


class Wires:
    wires = {}  # 'wire variable name': Wire object

    def parse_input(self, input):
        if input.isdigit():
            return int(input)
        else:
            if input not in self.wires:
                self.wires[input] = Wire(input)  # Creates an empty Wire object
            return self.wires[input]

    def __init__(self, f):
        for line in f:
            items = line.replace('\n', '').split(' ')
            output = items[-1]
            inputs = []
            if len(items) == 3:  # ASSIGN operation
                operation = Operations.ASSIGN
                inputs.append(self.parse_input(items[0]))
            elif len(items) == 4:  # NOT operation
                operation = Operations.NOT
                inputs.append(self.parse_input(items[1]))
            elif len(items) == 5:  # any of AND/OR/LSHIFT/RSHIFT operations
                if items[1] == 'AND':
                    operation = Operations.AND
                elif items[1] == 'OR':
                    operation = Operations.OR
                elif items[1] == 'LSHIFT':
                    operation = Operations.LSHIFT
                elif items[1] == 'RSHIFT':
                    operation = Operations.RSHIFT
                else:
                    print('Unexpected operation: {0}'.format(items[1]))

                inputs.append(self.parse_input(items[0]))
                inputs.append(self.parse_input(items[2]))
            else:
                print('Unexpected amount of items: {0}'.format(line))

            if output not in self.wires:
                self.wires[output] = Wire(output)
            self.wires[output].operation = operation
            self.wires[output].inputs = inputs


with open('data/day7.txt') as f:
    w = Wires(f)

print w.wires['a'].resolve()
