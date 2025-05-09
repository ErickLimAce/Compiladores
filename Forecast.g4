// Archivo: Forecast.g4
grammar Forecast;

// -------------------
// Parser rules
// -------------------
statement: FORECAST pollutant AT location IN NUMBER HOURS IF condition;

pollutant: PM25 | PM10 | O3 | CO | NO | NO2 | NOX | SO2;

location: ID;

condition: expr (AND expr)*;

expr: metric comparator NUMBER;

metric: TEMPERATURE | RAIN | PRESSURE | HUMIDITY | SOLAR_RADIATION | WIND;

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

PM10: 'PM10';
O3: 'O3';
CO: 'CO';
NO: 'NO';
NO2: 'NO2';
NOX: 'NOx';
SO2: 'SO2';

TEMPERATURE: 'TEMPERATURE';
RAIN: 'RAIN';
PRESSURE: 'PRESSURE';
HUMIDITY: 'HUMIDITY';
SOLAR_RADIATION: 'SOLAR_RADIATION';
WIND: 'WIND';

GT: '>';
LT: '<';
GE: '>=';
LE: '<=';
EQ: '=';

ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;

WS: [ \t\r\n]+ -> skip;
