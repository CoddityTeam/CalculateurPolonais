from rpn.models.operand import Operand
from rpn.models.stack import Stack
from rpn.services.exceptions import OperandException


class OperandService:
    def list_operand(self):
        return [op.value for op in Operand]
    
    def apply(self, stack: Stack, op: Operand):
        self._check_op_validity(stack.values, op)
        if op == Operand.ADD.value:
            new_values = stack.values[:-2] + [stack.values[-1] + stack.values[-2]]
            return Stack(id=stack.id, values= new_values)
        if op == Operand.SUBSTRACT.value:
            new_values = stack.values[:-2] + [stack.values[-2] - stack.values[-1]]
            return Stack(id=stack.id, values= new_values)
        if op == Operand.MULTIPLY.value:
            new_values = stack.values[:-2] + [stack.values[-2] * stack.values[-1]]
            return Stack(id=stack.id, values= new_values)
        if op == Operand.DIVIDE.value:
            new_values = stack.values[:-2] + [stack.values[-2] / stack.values[-1]]
            return Stack(id=stack.id, values= new_values)
        print(op)
    
    def _check_op_validity(self, values: list[int], op: Operand):
        if len(values)< 2:
            raise OperandException()
        if op == Operand.DIVIDE and values[-1] == 0:
            raise OperandException()
        