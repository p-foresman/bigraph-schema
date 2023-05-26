from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor


parameter_examples = {
    # 'no-parameters': 'simple',
    'typed': 'a:field[yellow,tree,snake]|b.(x:length|y:cloud)',
    'typed_parameters': 'edge[a:int|b.(x:length|y:float),v[zz:float|xx:what]]|okay',
    # 'one-parameter': 'parameterized[A]',
    # 'three-parameters': 'parameterized[A,B,C]',
    # 'nested-parameters': 'nested[outer[inner]]',
    # 'multiple-nested-parameters': 'nested[outer[inner],other,later[on,there[is],more]]',
}


parameter_grammar = Grammar(
    """
    expression = merge / tree
    merge = bigraph (bar bigraph)+
    tree = bigraph / type_name
    bigraph = group / nest / control
    group = paren_left expression paren_right
    nest = symbol dot bigraph
    control = symbol colon type_name
    type_name = symbol parameter_list?
    parameter_list = square_left expression (comma expression)* square_right
    symbol = ~r"[\w\d-_/*&^%$#@!~`+]+"
    dot = "."
    colon = ":"
    bar = "|"
    paren_left = "("
    paren_right = ")"
    square_left = "["
    square_right = "]"
    comma = ","
    not_newline = ~r"[^\\n\\r]"*
    newline = ~"[\\n\\r]+"
    ws = ~"\s*"
    """)


class ParameterVisitor(NodeVisitor):
    # def visit_qualified_type(self, node, visit):
    #     outer_type = visit[0]
    #     parameters = []
    #     if len(visit[1]['visit']) > 0:
    #         parameters = visit[1]['visit'][0]

    #     return [outer_type, parameters]

    def visit_expression(self, node, visit):
        import ipdb; ipdb.set_trace()
        return {
            'node': node,
            'visit': visit,
        }

    def visit_merge(self, node, visit):
        import ipdb; ipdb.set_trace()
        return {
            'node': node,
            'visit': visit,
        }

    def visit_tree(self, node, visit):
        import ipdb; ipdb.set_trace()
        return {
            'node': node,
            'visit': visit,
        }

    def visit_bigraph(self, node, visit):
        import ipdb; ipdb.set_trace()
        return {
            'node': node,
            'visit': visit,
        }

    def visit_group(self, node, visit):
        import ipdb; ipdb.set_trace()
        return {
            'node': node,
            'visit': visit,
        }

    def visit_nest(self, node, visit):
        import ipdb; ipdb.set_trace()
        return {
            'node': node,
            'visit': visit,
        }

    def visit_control(self, node, visit):
        import ipdb; ipdb.set_trace()
        return {
            'node': node,
            'visit': visit,
        }

    def visit_type_name(self, node, visit):
        import ipdb; ipdb.set_trace()

        type_name = visit[0]
        type_parameters = visit[1]['visit']

        return [type_name, type_parameters]

    def visit_parameter_list(self, node, visit):
        import ipdb; ipdb.set_trace()

        first_type = [visit[1]['visit'][0]['visit'][0]]
        rest_types = [
            inner['visit'][1]['visit'][0]['visit'][0]
            for inner in visit[2]['visit']]

        parameters = first_type + rest_types

        return parameters

    def visit_symbol(self, node, visit):
        return node.text

    def generic_visit(self, node, visit):
        return {
            'node': node,
            'visit': visit,
        }


def parse_type_parameters(expression):
    parse = parameter_grammar.parse(expression)
    visitor = ParameterVisitor()
    type_parameters = visitor.visit(parse)

    return type_parameters


def render_type_parameters(type_parameters):
    # inverse of parse_type_parameters
    type_name, parameters = type_parameters
    parameters_render = ','.join([
        render_type_parameters(parameter)
        for parameter in parameters
    ])

    render = type_name
    if len(parameters) > 0:
        render = f'{render}[{parameters_render}]'

    return render


def test_parse_parameters():
    for key, example in parameter_examples.items():
        types = parse_type_parameters(example)

        print(f'{key}: {example}')
        if types:
            print(types)
            print(render_type_parameters(types))


if __name__ == '__main__':
    test_parse_parameters()

