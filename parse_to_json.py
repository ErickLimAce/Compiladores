from antlr4 import *
from ForecastLexer import ForecastLexer
from ForecastParser import ForecastParser
from ForecastVisitor import ForecastVisitor
import json

class MyVisitor(ForecastVisitor):
    def visitStatement(self, ctx):
        result = {
            "command": ctx.FORECAST().getText(),  
            "target": ctx.pollutant().getText(),
            "location": ctx.location().getText().replace("_", " "),
            "time": int(ctx.NUMBER().getText()),
            "conditions": []
        }

        conditions_ctx = ctx.condition()
        for expr in conditions_ctx.expr():
            condition = {
                "variable": expr.metric().getText(),
                "operator": expr.comparator().getText(),
                "value": int(expr.NUMBER().getText())
            }
            result["conditions"].append(condition)

        return result

def parse_forecast(input_text):
    input_stream = InputStream(input_text)
    lexer = ForecastLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ForecastParser(stream)
    tree = parser.statement()

    visitor = MyVisitor()
    return visitor.visit(tree)
