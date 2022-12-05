from rpn.models.stack import Stack
from rpn.storage.exceptions import StorageException


class InMemoryStorage: 
    def __init__(self) -> None:
        self.__db: dict[str, Stack] = dict()
    
    def add_stack(self, stack: Stack) -> Stack:
        if self.stack_exists(stack_id=stack.id):
            raise StorageException()
        self.__db[stack.id] = stack
        return stack
    
    def stack_exists(self, stack_id: str) -> bool:
        if self.__db.get(stack_id, None) is not None:
            return True
        return False
    
    def get_stack(self, stack_id: str) -> Stack | None:
        return self.__db.get(stack_id, None)
    
    def get_all_stacks(self)-> list[Stack]:
        return list(self.__db.values())
    
    def update_stack(self, stack_id: str, updated_stack: Stack) -> Stack:
        if not self.stack_exists(stack_id=stack_id) or stack_id != updated_stack.id:
            raise StorageException()
        self.__db[stack_id] = updated_stack
        return updated_stack
    
    def delete_stack(self, stack_id: str)-> Stack:
        if not self.stack_exists(stack_id=stack_id):
            raise StorageException()
        deleted_stack = self.__db.pop(stack_id)
        return deleted_stack