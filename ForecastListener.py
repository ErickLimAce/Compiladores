# Generated from Forecast.g4 by ANTLR 4.13.1
# Nousado instead ast-builder.py
from antlr4 import *
if "." in __name__:
    from .ForecastParser import ForecastParser
else:
    from ForecastParser import ForecastParser

# This class defines a complete listener for a parse tree produced by ForecastParser.
class ForecastListener(ParseTreeListener):

    # Enter a parse tree produced by ForecastParser#statement.
    def enterStatement(self, ctx:ForecastParser.StatementContext):
        pass

    # Exit a parse tree produced by ForecastParser#statement.
    def exitStatement(self, ctx:ForecastParser.StatementContext):
        pass


    # Enter a parse tree produced by ForecastParser#pollutant.
    def enterPollutant(self, ctx:ForecastParser.PollutantContext):
        pass

    # Exit a parse tree produced by ForecastParser#pollutant.
    def exitPollutant(self, ctx:ForecastParser.PollutantContext):
        pass


    # Enter a parse tree produced by ForecastParser#location.
    def enterLocation(self, ctx:ForecastParser.LocationContext):
        pass

    # Exit a parse tree produced by ForecastParser#location.
    def exitLocation(self, ctx:ForecastParser.LocationContext):
        pass


    # Enter a parse tree produced by ForecastParser#condition.
    def enterCondition(self, ctx:ForecastParser.ConditionContext):
        pass

    # Exit a parse tree produced by ForecastParser#condition.
    def exitCondition(self, ctx:ForecastParser.ConditionContext):
        pass


    # Enter a parse tree produced by ForecastParser#expr.
    def enterExpr(self, ctx:ForecastParser.ExprContext):
        pass

    # Exit a parse tree produced by ForecastParser#expr.
    def exitExpr(self, ctx:ForecastParser.ExprContext):
        pass


    # Enter a parse tree produced by ForecastParser#metric.
    def enterMetric(self, ctx:ForecastParser.MetricContext):
        pass

    # Exit a parse tree produced by ForecastParser#metric.
    def exitMetric(self, ctx:ForecastParser.MetricContext):
        pass


    # Enter a parse tree produced by ForecastParser#comparator.
    def enterComparator(self, ctx:ForecastParser.ComparatorContext):
        pass

    # Exit a parse tree produced by ForecastParser#comparator.
    def exitComparator(self, ctx:ForecastParser.ComparatorContext):
        pass



del ForecastParser