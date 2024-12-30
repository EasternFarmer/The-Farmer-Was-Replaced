"""
My take 2 at this problem. But this time i'm using ast module/library . Check: https://docs.python.org/3/library/ast

Turns out this method is on average 3,28 (average from 100 calls) times slower than /scripts/types_remover.py and removes comments (not doc strings)
It for sure has less / None bugs tho
"""
import ast

class DowngradeAnnAssign(ast.NodeTransformer):
    """Converts AnnAssign nodes (annotated assignment) to simpler Assign nodes."""
    def visit_AnnAssign(self, node: ast.AnnAssign) -> ast.Assign | None:
        if node.value is not None: 
            return ast.Assign(targets=[node.target], value=node.value)
        return None # just so mypy can leave me alone

def remove_typesV2(path: str, *, return_str: bool = False, output_file: str = 'output.py') -> None | str:
    with open(path) as f:
        nodes = ast.parse(f.read())
    for node in ast.walk(nodes):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            # See: https://docs.python.org/3/library/ast.html#ast.arguments
            for arg in [*node.args.posonlyargs, *node.args.args, *node.args.kwonlyargs]:
                arg.annotation = None
            if node.args.vararg is not None:
                node.args.vararg.annotation = None
            if node.args.kwarg is not None:
                node.args.kwarg.annotation = None
            node.returns = None            
    nodes = ast.fix_missing_locations(DowngradeAnnAssign().visit(nodes))

    if return_str:
        return ast.unparse(nodes)
    with open(output_file, 'w') as f:
        f.writelines(ast.unparse(nodes))
    return None # just so mypy can leave me alone

if __name__ == '__main__':
    remove_typesV2(r'C:\Users\user\Desktop\Git\The-Farmer-Was-Replaced\scripts\input.py')