from rpn.api import storage_provider
from rpn.services.operand import OperandService
from rpn.services.stack import StackService



stack_service = StackService(storage=storage_provider.storage)
operand_service = OperandService()