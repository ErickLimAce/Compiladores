# ast_builder.py

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
