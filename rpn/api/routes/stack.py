from flask import Blueprint, jsonify, make_response, request
from rpn.api.services_provider import stack_service
from rpn.services.exceptions import StackNotFoundException
stack_bp = Blueprint("stacks", __name__, url_prefix="/stacks")

@stack_bp.get("/")
def get_stacks_list():
    return jsonify(stack_service.get_all_stacks())

@stack_bp.post("/")
def create_stack():
    return jsonify(stack_service.create_stack())

@stack_bp.get("/<id>")
def get_stack(id:str):
    stack = stack_service.get_stack(stack_id=id)
    return jsonify(stack)

@stack_bp.put("/<id>")
def add_value_to_stack(id: str):
    jso = request.get_json()
    value_to_add = jso.get("value")
    if value_to_add is None:
        return make_response(jsonify("Incorred value"), 400)
    stack_to_update = stack_service.get_stack(stack_id=id)
    updated_stack = stack_service.update_stack(stack_id=id, stack_update=stack_to_update.values + [value_to_add])
    return jsonify(updated_stack)

@stack_bp.delete("/<id>")
def delete_stack(id: str):
    deleted_stack = stack_service.delete_stack(id)
    return make_response(jsonify(deleted_stack), 200)