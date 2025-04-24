// Archivo: Forecast.g4
grammar Forecast;

// -------------------
// Parser rules
// -------------------
statement: FORECAST pollutant AT location IN number HOURS IF condition;

pollutant: PM25 | PM10;

location: ID;

condition: expr (AND expr)*;

expr: metric comparator number;

metric: WIND | HUMIDITY | TEMPERATURE;

comparator: GT | LT | GE | LE | EQ;

// -------------------
// Lexer rules
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
