import pytest
from rpn.models.operand import Operand
from rpn.models.stack import Stack
from rpn.services.exceptions import OperandException
from rpn.services.operand import OperandService


@pytest.fixture(scope="session")
def service() -> OperandService:
    service = OperandService()
    return service

@pytest.fixture
def valid_stack_for_op():
    return Stack(id="id", values=[230,10,5])

@pytest.fixture
def invalid_stack_for_op():
    return Stack(id="id", values=[230])

@pytest.fixture
def invalid_stack_for_divide_op():
    return Stack(id="id", values=[230, 10, 0])

def test_get_all_operand(service: OperandService):
    operand_list = service.list_operand()
    assert operand_list == ["+","-","*","/"]

def test_apply_operand_plus_should_return_updated_stack(service: OperandService, valid_stack_for_op):
    res = service.apply(valid_stack_for_op, Operand.ADD.value)
    assert isinstance(res, Stack)
    assert res.id == "id"
    assert res.values == [230, 15]
    
def test_apply_operand_minus_should_return_updated_stack(service: OperandService, valid_stack_for_op):
    res = service.apply(valid_stack_for_op, Operand.SUBSTRACT.value)
    assert isinstance(res, Stack)
    assert res.id == "id"
    assert res.values == [230, 5]

    
def test_apply_operand_multiply_should_return_updated_stack(service: OperandService, valid_stack_for_op):
    res = service.apply(valid_stack_for_op, Operand.MULTIPLY.value)
    assert isinstance(res, Stack)
    assert res.id == "id"
    assert res.values == [230, 50]

def test_apply_operand_divide_should_return_updated_stack(service: OperandService, valid_stack_for_op):
    res = service.apply(valid_stack_for_op, Operand.DIVIDE.value)
    assert isinstance(res, Stack)
    assert res.id == "id"
    assert res.values == [230, 2]
    
def test_apply_operand_on_invalid_stack(service: OperandService, invalid_stack_for_op: Stack, invalid_stack_for_divide_op:Stack):
    with pytest.raises(OperandException):
        service.apply(invalid_stack_for_op, Operand.ADD)
    with pytest.raises(OperandException):
        service.apply(invalid_stack_for_op, Operand.SUBSTRACT)
    with pytest.raises(OperandException):
        service.apply(invalid_stack_for_op, Operand.MULTIPLY)
    with pytest.raises(OperandException):
        service.apply(invalid_stack_for_op, Operand.DIVIDE)
    with pytest.raises(OperandException):
        service.apply(invalid_stack_for_divide_op, Operand.DIVIDE)