from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class Multiplicate(BaseOperator):
    @apply_defaults
    def __init__(self, num1, num2, *args, **kwargs):
        super(Multiplicate, self).__init__(*args, **kwargs)
        self.num1 = num1
        self.num2 = num2

    def execute(self, context):
        result = self.num1 * self.num2
        self.log.info(f"Multiplication result: {result}")
        return result
