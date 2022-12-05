from flask import Flask
from rpn.api.routes.operand import operand_bp
from rpn.api.routes.stack import stack_bp

app = Flask(__name__)
app.register_blueprint(operand_bp)
app.register_blueprint(stack_bp)