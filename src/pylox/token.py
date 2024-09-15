from typing import Any

from src.pylox.types import TokenType


class Token:
    def __init__(
        self,
        token_t: TokenType,
        lexeme: str,
        literal: Any,
        line: int,
    ) -> Any:
        self.token_t = token_t
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self) -> str:
        return f"{self.token_t.name} {self.lexeme} {self.literal} {self.line}"

    def __repr__(self) -> str:
        return self.__str__()


class Scanner:
    def __init__(self, source: str) -> None:
        self.source = source
        self.tokens: list[Token] = list()
        self._start: int = 0
        self._current: int = 0
        self._line: int = 0

    def has_next(self) -> bool:
        return self._current >= len(self.source)

    def scan_tokens(self) -> None:
        while self.has_next():
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self._line))
