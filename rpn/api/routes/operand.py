from flask import Blueprint, jsonify, make_response
from rpn.api.services_provider import operand_service, stack_service
operand_bp = Blueprint("op", __name__, url_prefix="/op")

@operand_bp.get("/")
def get_op_list():
    return jsonify(operand_service.list_operand())

@operand_bp.post("/<op>/stack/<stack_id>")
def apply_op(op: str, stack_id: str):
    if op not in operand_service.list_operand():
        return make_response({"details": "Unavailable operand"}, 400)
    stack_to_update = stack_service.get_stack(stack_id=stack_id)
    print(stack_to_update)
    stack_update = operand_service.apply(stack_to_update, op)
    print(stack_update)
    updated_stack = stack_service.update_stack(stack_id=stack_id, stack_update=stack_update.values)
    return jsonify(updated_stack)
