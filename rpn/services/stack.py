from rpn.models.stack import Stack
from rpn.services.exceptions import StackNotFoundException, StackValuesException
from rpn.storage.exceptions import StorageException
from rpn.storage.inmemory import InMemoryStorage
import uuid

class StackService: 
    def __init__(self, storage: InMemoryStorage) -> None:
        self.__storage = storage
    
    def get_all_stacks(self) -> list[Stack]:
        return self.__storage.get_all_stacks()

    def create_stack(self) -> Stack:
        created_stack = Stack(id=str(uuid.uuid4()), values=[])
        self.__storage.add_stack(stack=created_stack)
        return created_stack

    def get_stack(self, stack_id: str) -> Stack:
        stack = self.__storage.get_stack(stack_id=stack_id)
        if stack is None: 
            raise StackNotFoundException()
        return stack

    def update_stack(self,stack_id: str, stack_update: list[int]) -> Stack:
        try:
            self._verify_values(stack_update)
            stack_updated = self.__storage.update_stack(stack_id=stack_id, updated_stack=Stack(id=stack_id, values=stack_update))
            return stack_updated    
        except StorageException:
            raise StackNotFoundException()
    
    def delete_stack(self, stack_id: str) -> Stack:
        self.get_stack(stack_id=stack_id)
        stack = self.__storage.delete_stack(stack_id=stack_id)
        return stack

    
    def _verify_values(self,values: list[int]):
        for v in values:
            if not (isinstance(v, int) or isinstance(v, float)) :

                raise StackValuesException()