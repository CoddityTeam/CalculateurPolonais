import pytest
from rpn.services.exceptions import StackNotFoundException, StackValuesException
from rpn.services.stack import StackService

from rpn.storage.inmemory import InMemoryStorage
import uuid
@pytest.fixture(scope="session")
def storage()-> InMemoryStorage:
    storage = InMemoryStorage()
    return storage

@pytest.fixture(scope="session")
def service(storage) ->StackService:
    service = StackService(storage)
    return service

def test_stack_service_exists(service: StackService):
    assert service is not None

def test_get_all_stacks_should_return_empty_list(service: StackService):
    assert service.get_all_stacks() == []

def test_create_stack_should_return_newly_created_stack(service: StackService, monkeypatch):
    monkeypatch.setattr(uuid, "uuid4", lambda : "id")
    created_stack = service.create_stack()
    assert created_stack.values == []
    assert created_stack.id == "id"    

def test_get_all_stacks_should_return_list_with_created_stack(service: StackService):
    stack_list = service.get_all_stacks()
    assert isinstance(stack_list, list)
    assert len(stack_list) != 0
    assert stack_list[0].id == "id"
    assert stack_list[0].values == []

def test_get_stack_with_id_equals_id_should_return_stack(service: StackService):
    stack = service.get_stack(stack_id="id")
    assert stack is not None
    assert stack.id == "id"
    assert stack.values == []

def test_get_stack_with_unexistant_id_should_raise_stack_not_found_exception(service: StackService):
    with pytest.raises(StackNotFoundException):
        service.get_stack(stack_id="unexistant_id")

def test_update_stack_with_id_should_return_updated_stack(service: StackService):
    updated_stack = service.update_stack(stack_id='id', stack_update=[122, 5435,544.2])
    assert updated_stack.id == "id"
    assert updated_stack.values == [122, 5435,544.2]

def test_update_stack_with_unexistant_id_should_raise_stack_not_found_exception(service: StackService):
    with pytest.raises(StackNotFoundException):
        updated_stack = service.update_stack(stack_id='unexistant_id', stack_update=[122, 5435.32,5442])

def test_update_stack_with_values_not_number_should_raise_stack_values_exception(service:StackService):
    with pytest.raises(StackValuesException):
        updated_stack = service.update_stack(stack_id='id', stack_update=["dlkflk", 5435,5442])

def test_delete_stack_with_id_should_return_deleted_stack(service: StackService):
    deleted_stack = service.delete_stack(stack_id="id")
    assert deleted_stack.id == "id"
    assert deleted_stack.values == [122, 5435,544.2]

def test_delete_stack_with_id_should_should_raise_stack_not_found_exception(service: StackService):
    with pytest.raises(StackNotFoundException):
        deleted_stack = service.delete_stack(stack_id="id")

    
def test_delete_stack_with_unexistant_id_should_raise_stack_not_found_exception(service: StackService):
    with pytest.raises(StackNotFoundException):
        deleted_stack = service.delete_stack(stack_id="unexistant_id")

def test_get_all_stacks_should_return_empty_list_after_delete(service: StackService):
    assert service.get_all_stacks() == []
