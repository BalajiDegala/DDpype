from examples.example_calculator.calc_conf import register_node, OP_NODE_ADD, OP_NODE_SUB, OP_NODE_MUL, OP_NODE_DIV, OP_NODE_DEPT
from examples.example_calculator.calc_node_base import CalcNode, DeptNode


@register_node(OP_NODE_ADD)
class CalcNode_Add(CalcNode):
    icon = "icons/add.png"
    op_code = OP_NODE_ADD
    op_title = "SEQUENCE"
    content_label = ""
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1, input2):
        return input1 + input2


@register_node(OP_NODE_SUB)
class CalcNode_Sub(CalcNode):
    icon = "icons/sub.png"
    op_code = OP_NODE_SUB
    op_title = "ASSET"
    content_label = ""
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1, input2):
        return input1 - input2


@register_node(OP_NODE_MUL)
class CalcNode_Mul(CalcNode):
    icon = "icons/mul.png"
    op_code = OP_NODE_MUL
    op_title = "SHOT"
    content_label = ""
    content_label_objname = "calc_node_mul"

    def evalOperation(self, input1, input2):
        print('foo')
        return input1 * input2


@register_node(OP_NODE_DIV)
class CalcNode_Div(CalcNode):
    icon = "icons/divide.png"
    op_code = OP_NODE_DIV
    op_title = "TASK"
    content_label = ""
    content_label_objname = "calc_node_div"

    def evalOperation(self, input1, input2):
        return input1 / input2


@register_node(OP_NODE_DEPT)
class CalcNode_Dept(DeptNode):
    icon = "icons/divide.png"
    op_code = OP_NODE_DEPT
    op_title = "DEPT"
    content_label = ""
    content_label_objname = "calc_node_div"

    def evalOperation(self, input1, input2):
        return input1 / input2

# way how to register by function call
# register_node_now(OP_NODE_ADD, CalcNode_Add)
