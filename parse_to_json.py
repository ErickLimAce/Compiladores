# parse_to_json.py
#ransformar texto de entrada a una estructura de datos JSON.
# encapsula todo el proceso de análisis léxico, sintáctico y construcción del AST. Y se usa en prueba_parser.py

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
