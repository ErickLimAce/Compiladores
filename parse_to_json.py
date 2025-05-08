# parse_to_json.py

from antlr4 import InputStream, CommonTokenStream
from ForecastLexer import ForecastLexer
from ForecastParser import ForecastParser
from ast_builder import ASTBuilder

def parse_forecast(text):
    input_stream = InputStream(text)
    lexer = ForecastLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ForecastParser(stream)
    
    tree = parser.statement()
    visitor = ASTBuilder()
    return visitor.visit(tree)
