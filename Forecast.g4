// Archivo: Forecast.g4
//Define la gramática formal lenguaje.
//Especifica reglas léxicas (tokens) y sintácticas (parser rules) 

grammar Forecast;

// -------------------
// Parser rules.Define la estructura de un comando completo en tu lenguaje.
// -------------------
statement: FORECAST pollutant AT location IN NUMBER HOURS IF condition;

pollutant: PM25 | PM10;

location: ID;

condition: expr (AND expr)*;

expr: metric comparator NUMBER;

metric: WIND | HUMIDITY | TEMPERATURE;

comparator: GT | LT | GE | LE | EQ;

// -------------------
// Lexer rules Tokenizacion
// -------------------

FORECAST: 'FORECAST';
AT: 'AT';
IN: 'IN';
IF: 'IF';
HOURS: 'HOURS';
AND: 'AND';

PM25: 'PM25';
PM10: 'PM10';

WIND: 'WIND';
HUMIDITY: 'HUMIDITY';
TEMPERATURE: 'TEMPERATURE';

GT: '>';
LT: '<';
GE: '>=';
LE: '<=';
EQ: '=';

ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;

WS: [ \t\r\n]+ -> skip;
