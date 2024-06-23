from tools.grammar import GrammarToken
from tools.parser import Parser
from tools.parserResp import ParseResult
from tools.SRL1automaton import AutomatonSLR1
from tools.tableLR import TableLR
from typing import List
from .grammar import regex_grammar
from .core import RegexToken


def regex_build() -> bool:
    a = AutomatonSLR1('regex', regex_grammar)
    return a.ok


def regex_parser(l: List[GrammarToken]) -> ParseResult:
    t = TableLR(regex_grammar)
    t.load('regex')
    return Parser(regex_grammar, t).parse(l)

def regex_to_grammar(token: RegexToken) -> GrammarToken:
    if token.is_special:
        return [t for t in regex_grammar.terminals if t.value == token.value][0]

    return [t for t in regex_grammar.terminals if t.value == 'ch'][0]
