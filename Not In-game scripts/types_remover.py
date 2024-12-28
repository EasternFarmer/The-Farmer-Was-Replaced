def remove_types(path: str, return_str: bool = False) -> None | str:
    with open(path) as f:
        file = [line.rstrip('\n') for line in f.readlines()]

    # in_string: bool = False
    dict_deep: int = 0

    new_file: list[str] = []
    dict_line = ''
    for line in file:
        if 'import' in line:
            new_file.append(line)
            continue

        if line.count('{') > line.count('}'):
            dict_deep += 1

        try:
            match line.split()[0]:
                case 'def':
                    spaces: int = len(line)-len(line.lstrip())
                    args: list[str] = [tuple(lst.split(':'))[0] for lst in ''.join(line[line.index('(')+1 : line.index(')')].split(' ')).split(',')]
                    function_name: str = line[4:line.index('(')]
                    new_file.append(f'{' '*spaces}def {function_name}({', '.join(args)}):')
                case 'if' | 'case':
                    new_file.append(line)
                case _ if line.count('=') == 1:
                    if line[line.index('=')-2:line.index('=')+1] in ['**=', '//=', '>>=', '<<=']:
                        operator = line[line.index('=')-2:line.index('=')+1]
                    elif line[line.index('=')-1:line.index('=')+1] in ['+=', '-=', '*=', '/=', '&=', '|=', '^=', '~=']:
                        operator = line[line.index('=')-1:line.index('=')+1]
                    else:
                        operator = '='
                    if dict_deep == 0:
                        variable_name = line[0:line.lstrip().index(' ')+ len(line) - len(line.lstrip())].rstrip(':')
                        lst = line.split('=')
                        value = lst[1] if len(lst) == 2 else None
                        if value != None:
                            new_file.append(f'{variable_name} {operator}{value}')
                    else:
                        dict_line += line
                case _:
                    if dict_deep == 0:
                        new_file.append(line)
                    else:
                        dict_line += line
        except IndexError:
            new_file.append(line)
        if line.count('{') < line.count('}'):
            dict_deep -= 1
            if dict_line != '' and dict_deep == 0:
                dict_line = ''.join(dict_line.split('\n'))
                variable_name = dict_line[0:dict_line.lstrip().index(' ')+ len(dict_line) - len(dict_line.lstrip())].rstrip(':')
                lst = ''.join(dict_line.split()).split('=')
                value = lst[1] if len(lst) == 2 else None
                if value != None:
                    new_file.append(f'{variable_name} = {value}')
                dict_line = ''
                continue
    if return_str:
        return '\n'.join(new_file)
    with open('output.py', 'w') as f:
        f.writelines('\n'.join(new_file))
    return None

remove_types(r'C:\Users\user\Desktop\Git\tfwr-logger\Not In-game scripts\input.txt')