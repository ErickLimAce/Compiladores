# ast_builder.py
#Transformar el árbol de análisis sintáctico
# en una representación más abstracta y estructurada del comando de predicción. 
# Sirve para validación semántica.
#1 El analizador sintáctico (parser) genera un árbol de análisis completo a partir del texto de entrada
#2 Se llama al método visit() con el nodo raíz del árbol
#3 Cada método visit tiene el control total sobre si visita o no los nodos hijos y puede devolver cualquier valor
#4El analizador sintáctico (parser) genera un árbol de análisis concreto a partir del texto de entrada
#4.1El visitor recorre el árbol, transformándolo en una estructura de datos jerárquica (diccionarios y listas)
#5El resultado es un AST que representa de manera más abstracta el significado del comando
# Mandar a parse_jason

from ForecastVisitor import ForecastVisitor
from ForecastParser import ForecastParser

class ASTBuilder(ForecastVisitor):
    def visitStatement(self, ctx: ForecastParser.StatementContext):
        return {
            "type": "ForecastStatement",
            "pollutant": self.visit(ctx.pollutant()),
            "location": ctx.location().getText(),
            "duration_hours": int(ctx.NUMBER().getText()),
            "conditions": self.visit(ctx.condition())
        }

    def visitPollutant(self, ctx: ForecastParser.PollutantContext):
        return ctx.getText()

    def visitCondition(self, ctx: ForecastParser.ConditionContext):
        return [self.visit(expr) for expr in ctx.expr()]

    def visitExpr(self, ctx: ForecastParser.ExprContext):
        return {
            "metric": ctx.metric().getText(),
            "comparator": ctx.comparator().getText(),
            "value": int(ctx.NUMBER().getText())
        }
#