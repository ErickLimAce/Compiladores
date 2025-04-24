from antlr4 import *
from ForecastLexer import ForecastLexer

input_text = "FORECAST PM25 AT zona_norte IN 2 HOURS IF WIND > 10 AND HUMIDITY < 40"
lexer = ForecastLexer(InputStream(input_text))

for token in lexer.getAllTokens():
    token_name = lexer.symbolicNames[token.type]
    print(f"{token.text:<15} --> {token_name}")
