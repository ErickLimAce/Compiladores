from antlr4 import *
from ForecastLexer import ForecastLexer
from ForecastParser import ForecastParser

input_text = "FORECAST PM25 AT zona_norte IN 2 HOURS IF WIND > 10 AND HUMIDITY < 40"
input_stream = InputStream(input_text)

# Lexer
lexer = ForecastLexer(input_stream)
token_stream = CommonTokenStream(lexer)

# Parser
parser = ForecastParser(token_stream)
tree = parser.statement()

print(tree.toStringTree(recog=parser))
