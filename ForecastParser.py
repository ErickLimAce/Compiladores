# Generated from Forecast.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,45,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,
        3,1,3,5,3,32,8,3,10,3,12,3,35,9,3,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,
        6,1,6,0,0,7,0,2,4,6,8,10,12,0,3,1,0,7,8,1,0,9,11,1,0,12,16,38,0,
        14,1,0,0,0,2,24,1,0,0,0,4,26,1,0,0,0,6,28,1,0,0,0,8,36,1,0,0,0,10,
        40,1,0,0,0,12,42,1,0,0,0,14,15,5,1,0,0,15,16,3,2,1,0,16,17,5,2,0,
        0,17,18,3,4,2,0,18,19,5,3,0,0,19,20,5,18,0,0,20,21,5,5,0,0,21,22,
        5,4,0,0,22,23,3,6,3,0,23,1,1,0,0,0,24,25,7,0,0,0,25,3,1,0,0,0,26,
        27,5,17,0,0,27,5,1,0,0,0,28,33,3,8,4,0,29,30,5,6,0,0,30,32,3,8,4,
        0,31,29,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,7,1,
        0,0,0,35,33,1,0,0,0,36,37,3,10,5,0,37,38,3,12,6,0,38,39,5,18,0,0,
        39,9,1,0,0,0,40,41,7,1,0,0,41,11,1,0,0,0,42,43,7,2,0,0,43,13,1,0,
        0,0,1,33
    ]

class ForecastParser ( Parser ):

    grammarFileName = "Forecast.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'FORECAST'", "'AT'", "'IN'", "'IF'", 
                     "'HOURS'", "'AND'", "'PM25'", "'PM10'", "'WIND'", "'HUMIDITY'", 
                     "'TEMPERATURE'", "'>'", "'<'", "'>='", "'<='", "'='" ]

    symbolicNames = [ "<INVALID>", "FORECAST", "AT", "IN", "IF", "HOURS", 
                      "AND", "PM25", "PM10", "WIND", "HUMIDITY", "TEMPERATURE", 
                      "GT", "LT", "GE", "LE", "EQ", "ID", "NUMBER", "WS" ]

    RULE_statement = 0
    RULE_pollutant = 1
    RULE_location = 2
    RULE_condition = 3
    RULE_expr = 4
    RULE_metric = 5
    RULE_comparator = 6

    ruleNames =  [ "statement", "pollutant", "location", "condition", "expr", 
                   "metric", "comparator" ]

    EOF = Token.EOF
    FORECAST=1
    AT=2
    IN=3
    IF=4
    HOURS=5
    AND=6
    PM25=7
    PM10=8
    WIND=9
    HUMIDITY=10
    TEMPERATURE=11
    GT=12
    LT=13
    GE=14
    LE=15
    EQ=16
    ID=17
    NUMBER=18
    WS=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FORECAST(self):
            return self.getToken(ForecastParser.FORECAST, 0)

        def pollutant(self):
            return self.getTypedRuleContext(ForecastParser.PollutantContext,0)


        def AT(self):
            return self.getToken(ForecastParser.AT, 0)

        def location(self):
            return self.getTypedRuleContext(ForecastParser.LocationContext,0)


        def IN(self):
            return self.getToken(ForecastParser.IN, 0)

        def NUMBER(self):
            return self.getToken(ForecastParser.NUMBER, 0)

        def HOURS(self):
            return self.getToken(ForecastParser.HOURS, 0)

        def IF(self):
            return self.getToken(ForecastParser.IF, 0)

        def condition(self):
            return self.getTypedRuleContext(ForecastParser.ConditionContext,0)


        def getRuleIndex(self):
            return ForecastParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ForecastParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(ForecastParser.FORECAST)
            self.state = 15
            self.pollutant()
            self.state = 16
            self.match(ForecastParser.AT)
            self.state = 17
            self.location()
            self.state = 18
            self.match(ForecastParser.IN)
            self.state = 19
            self.match(ForecastParser.NUMBER)
            self.state = 20
            self.match(ForecastParser.HOURS)
            self.state = 21
            self.match(ForecastParser.IF)
            self.state = 22
            self.condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PollutantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PM25(self):
            return self.getToken(ForecastParser.PM25, 0)

        def PM10(self):
            return self.getToken(ForecastParser.PM10, 0)

        def getRuleIndex(self):
            return ForecastParser.RULE_pollutant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPollutant" ):
                listener.enterPollutant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPollutant" ):
                listener.exitPollutant(self)




    def pollutant(self):

        localctx = ForecastParser.PollutantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pollutant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ForecastParser.ID, 0)

        def getRuleIndex(self):
            return ForecastParser.RULE_location

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocation" ):
                listener.enterLocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocation" ):
                listener.exitLocation(self)




    def location(self):

        localctx = ForecastParser.LocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_location)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(ForecastParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ForecastParser.ExprContext)
            else:
                return self.getTypedRuleContext(ForecastParser.ExprContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(ForecastParser.AND)
            else:
                return self.getToken(ForecastParser.AND, i)

        def getRuleIndex(self):
            return ForecastParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = ForecastParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.expr()
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 29
                self.match(ForecastParser.AND)
                self.state = 30
                self.expr()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def metric(self):
            return self.getTypedRuleContext(ForecastParser.MetricContext,0)


        def comparator(self):
            return self.getTypedRuleContext(ForecastParser.ComparatorContext,0)


        def NUMBER(self):
            return self.getToken(ForecastParser.NUMBER, 0)

        def getRuleIndex(self):
            return ForecastParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = ForecastParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.metric()
            self.state = 37
            self.comparator()
            self.state = 38
            self.match(ForecastParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetricContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WIND(self):
            return self.getToken(ForecastParser.WIND, 0)

        def HUMIDITY(self):
            return self.getToken(ForecastParser.HUMIDITY, 0)

        def TEMPERATURE(self):
            return self.getToken(ForecastParser.TEMPERATURE, 0)

        def getRuleIndex(self):
            return ForecastParser.RULE_metric

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetric" ):
                listener.enterMetric(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetric" ):
                listener.exitMetric(self)




    def metric(self):

        localctx = ForecastParser.MetricContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_metric)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(ForecastParser.GT, 0)

        def LT(self):
            return self.getToken(ForecastParser.LT, 0)

        def GE(self):
            return self.getToken(ForecastParser.GE, 0)

        def LE(self):
            return self.getToken(ForecastParser.LE, 0)

        def EQ(self):
            return self.getToken(ForecastParser.EQ, 0)

        def getRuleIndex(self):
            return ForecastParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)




    def comparator(self):

        localctx = ForecastParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126976) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





