# TODO
- [ ] Add docstring to api
  - > I did not have the time to write the documentations during the tests.
- [x] Create git project
  - [x] Add `.gitignore` for python
  - [x] Add venv and create `requirements.txt`
  - [x] Add `flask` and `pytest` dependency
- [x] Create `OpService`
  - [x] Create a method to create a stack using TDD
    - [x] Create a stack model (`id [uuid.v4], values [list[number]]`)
    - [x] Create an `InMemoryStorage` to store the operand 
      - Database Schema : `dict[uuid.v4,Stack]`
  - [x] Create operand Enum -> `+ - / *`
  - [x] Create operand Service using TDD
    - [x] Create method to apply operand to a stack -> return the new stack
      - [x] Verify that we can apply operand
        - [x] Check if stack length > 2
        - [x] If operand == "/" -> second element must not be 0
  - [x] Create a method to update a stack (`def add(self, id:str, values: list[int])`) using TDD
    - [x] Find the stack to update in the `InMemoryStorage`
    - [x] Update the stack in the `InMemoryStorage`
    - [x] Return the updated stack
  - [x] Create FlaskApp
    - [ ] Create rpn Router
    - [x] Add routes to rpn Router
      - [x] `GET /op` -> Return the list of Operand enum values
      - [x] `POST /op/{op}/stack/{stack_id}` -> Apply operand on stack and returns the updated stack (404 if stack or op not found, 409 if stack is op is not valid on stack)
      - [x] `GET /stack` -> Return the stack list
      - [x] `GET /stack/{stack_id}` -> Return the stack with id stack_id (404 if not found)
      - [x] `POST /stack` -> Create and return a stack (Empty body)
      - [x] `PUT /stack/{stack_id}` `body:{"num": int}` -> Add num to stack and return the updated stack (404 if stack not found)
      - [x] `DELETE /stack/{stack_id}` -> Delete the stack (404 if rpn not found)
  - [ ] Create OpenApi doc
    - >Initially, I wanted to use flask restplus or something similar, but when I looked into github repositories, I didn't find something updated recently. So, an analysis of existing frameworks can be preformed to choose one which can generate open api specs automatically. Or a migration to fastapi for automatic open api doc. Or I can write manually the specs but i did not have the time now 
  - [ ] Add Errors handlers
    - > I Created some exceptions on the service package and on the storage package. Flask can handle those errors to avoid returning 500 status (INTERNAL_SERVER_ERROR) and return 404 when resources is not found or 409 when trying to apply an operand on invalid values (Operand on nothing or divide by zero )