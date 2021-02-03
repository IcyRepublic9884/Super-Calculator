from PyQt5.QtWidgets import QLabel
import ast
import operator

_OP_MAP = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.itruediv,
    ast.Invert: operator.neg,
}


class Calc(ast.NodeVisitor):

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return _OP_MAP[type(node.op)](left, right)

    def visit_Num(self, node):
        return node.n

    def visit_Expr(self, node):
        return self.visit(node.value)

    @classmethod
    def evaluate(cls, expression):
        tree = ast.parse(expression)
        calc = cls()
        return calc.visit(tree.body[0])


def update_display(display: QLabel, text):
    """Updates the display"""
    display.setText(display.text() + str(text))


def empty_display(display: QLabel):
    """Truncates the display"""


def set_display_text(display: QLabel, text):
    """Sets the text of display"""
    display.setText(text)
