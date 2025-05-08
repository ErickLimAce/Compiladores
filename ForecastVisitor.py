# Generated from Forecast.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ForecastParser import ForecastParser
else:
    from ForecastParser import ForecastParser

# This class defines a complete generic visitor for a parse tree produced by ForecastParser.

class ForecastVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ForecastParser#statement.
    def visitStatement(self, ctx:ForecastParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ForecastParser#pollutant.
    def visitPollutant(self, ctx:ForecastParser.PollutantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ForecastParser#location.
    def visitLocation(self, ctx:ForecastParser.LocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ForecastParser#condition.
    def visitCondition(self, ctx:ForecastParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ForecastParser#expr.
    def visitExpr(self, ctx:ForecastParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ForecastParser#metric.
    def visitMetric(self, ctx:ForecastParser.MetricContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ForecastParser#comparator.
    def visitComparator(self, ctx:ForecastParser.ComparatorContext):
        return self.visitChildren(ctx)



del ForecastParser