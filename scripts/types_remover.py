"""
Types that include "," in the declaration like Callable[[int, int], int] in function argument definitions don't work!

def a(A: Callable[[int, int], int]) -> None:
    pass
def b() -> Callable[[int, int], int]:
    pass 
def c(A: tuple[int,int]):
    Aa: Callable[[int, int], int] = ...

    |
    v

def a(A, int], int]):
    pass
def b():
    pass 
def c(A, int]):
    Aa = ...
"""

def parse_line(line: str) -> str | bool:
    if '\n' in line:
        line = ''.join(line.split('\n'))
    spaces = len(line)-len(line.lstrip())
    variable_name = line[0:line.lstrip().index(' ')+ len(line) - len(line.lstrip())].rstrip(':')
    lst = ''.join(line.split()).split('=')
    value = lst[1] if len(lst) == 2 else None
    if value != None:
        return f'{' '*spaces}{variable_name} = {value}' #type: ignore
    return False

def remove_types(path: str, *, return_str: bool = False, output_file: str = 'output.py') -> None | str:
    with open(path) as f:
        file = [line.rstrip('\n') for line in f.readlines()]

    # in_string: bool = False
    dict_deep: int = 0
    list_deep: int = 0
    tuple_deep: int = 0

    new_file: list[str] = []
    dict_line: str = ''
    list_line: str = ''
    tuple_line: str = ''
    tuple_is_func: bool = False

    for line in file:
        if 'import' in line:
            new_file.append(line)
            continue

        if (line.count('{') - line.count(repr('{'))) > (line.count('}') - line.count(repr('}'))):
            dict_deep += 1
        if (line.count('[') - line.count(repr('['))) > (line.count(']') - line.count(repr(']'))):
            list_deep += 1
        if (line.count('(') - line.count(repr('('))) > (line.count(')') - line.count(repr(')'))):
            tuple_deep += 1

        try:
            if line.split()[0][0] == '#':
                new_file.append(line)
                continue
            match line.split()[0]:
                case 'def':
                    if tuple_deep == 0:
                        args2 = []
                        spaces: int = len(line)-len(line.lstrip())
                        args: list[list[str]] = [lst.split(':') for lst in ''.join(line[line.index('(')+1 : line.index(')')].split(' ')).split(',')]
                        function_name: str = line[line.index('def')+4:line.index('(')]
                        for i in range(len(args)):
                            if args == [['']]:
                                args2 = ['']
                                break
                            if len(args[i]) == 1:
                                args[i].append('')
                            args[i][1] = args[i][1].split('=')[1] if '=' in args[i][1] else None #type: ignore
                            args2.append(' = '.join(args[i]) if args[i][1] is not None else args[i][0])
                        new_file.append(f'{' '*spaces}def {function_name}({', '.join(args2)}):')
                    else:
                        tuple_line += line
                        tuple_is_func = True
                case 'if' | 'case' | 'return':
                    new_file.append(line)
                case _ if line.count('=') == 1:
                    if (dict_deep + list_deep + tuple_deep) == 0:
                        if line[line.index('=')-2:line.index('=')+1] in ['**=', '//=', '>>=', '<<=']:
                            operator = line[line.index('=')-2:line.index('=')+1]
                        elif line[line.index('=')-1:line.index('=')+1] in ['+=', '-=', '*=', '/=', '&=', '|=', '^=', '~=']:
                            operator = line[line.index('=')-1:line.index('=')+1]
                        else:
                            operator = '='
                        variable_name = line[0:line.lstrip().index(' ')+ len(line) - len(line.lstrip())].rstrip(':')
                        lst = line.split('=')
                        value = lst[1] if len(lst) == 2 else None
                        if value != None:
                            new_file.append(f'{variable_name} {operator}{value}')
                    elif dict_deep > list_deep and dict_deep > tuple_deep:
                        dict_line += line
                    elif tuple_deep > list_deep and tuple_deep > dict_deep:
                        tuple_line += line
                    elif list_deep > dict_deep and list_deep > tuple_deep:
                        list_line += line
                case _:
                    if (dict_deep + list_deep + tuple_deep) == 0:
                        new_file.append(line)
                    elif dict_deep > list_deep and dict_deep > tuple_deep:
                        dict_line += line
                    elif tuple_deep > list_deep and tuple_deep > dict_deep:
                        tuple_line += line
                    elif list_deep > dict_deep and list_deep > tuple_deep:
                        list_line += line
        except IndexError:
            new_file.append(line)
        if line.count('{') < line.count('}'):
            dict_deep -= 1
            if dict_line != '' and dict_deep == 0:
                new_line = parse_line(dict_line)
                if new_line: new_file.append(new_line) #type: ignore
                else: new_file.append(' '*(len(dict_line) - len(dict_line.lstrip()))+''.join(dict_line.split()))
                dict_line = ''
        if line.count('[') < line.count(']'):
            list_deep -= 1
            if list_line != '' and list_deep == 0:
                new_line = parse_line(list_line)
                if new_line: new_file.append(new_line) #type: ignore
                else: new_file.append(' '*(len(list_line) - len(list_line.lstrip()))+''.join(list_line.split()))
                list_line = ''
        if line.count('(') < line.count(')'):
            tuple_deep -= 1
            if tuple_line != '' and tuple_deep == 0 and tuple_is_func:
                tuple_line = ''.join(tuple_line.split('\n'))
                args2 = []
                spaces = len(tuple_line)-len(tuple_line.lstrip())
                args = [lst.split(':') for lst in ''.join(tuple_line[tuple_line.index('(')+1 : tuple_line.index(')')].split(' ')).split(',')]
                function_name = tuple_line[tuple_line.index('def')+4:tuple_line.index('(')]
                for i in range(len(args)):
                    if args == [['']]:
                        args2 = ['']
                        break
                    if len(args[i]) == 1:
                        args[i].append('')
                    args[i][1] = args[i][1].split('=')[1] if '=' in args[i][1] else None #type: ignore
                    args2.append(' = '.join(args[i]) if args[i][1] is not None else args[i][0])
                new_file.append(f'{' '*spaces}def {function_name}({', '.join(args2)}):')
                tuple_line = ''
                tuple_is_func = False
            elif tuple_line != '' and tuple_deep == 0:
                new_line = parse_line(tuple_line)
                if new_line: new_file.append(new_line) #type: ignore
                else: new_file.append(' '*(len(tuple_line) - len(tuple_line.lstrip()))+''.join(tuple_line.split()))
                tuple_line = ''

    if return_str:
        return '\n'.join(new_file)
    with open(output_file, 'w') as f:
        f.writelines('\n'.join(new_file))
    return None

if __name__ == '__main__':
    remove_types(r'C:\Users\user\Desktop\Git\The-Farmer-Was-Replaced\scripts\input.py')