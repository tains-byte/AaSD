
from __future__ import annotations

from beartype import beartype

_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~"

_DECODE_MAP = {ord(c): i for i, c in enumerate(_ALPHABET)}


@beartype
def encode(b: bytes) -> bytes:
    if not b:
        return b""

    result = []

    for i in range(0, len(b), 4):
        # из 4 байт в 5 блоков Base
        chunk = b[i:i + 4]
        ours_len = len(chunk)

        # выравнивание до 4 байт (\x00 = 0)
        padded = chunk + b'\x00' * (4 - ours_len)

        # последовательность байтов в число
        num = int.from_bytes(padded, 'big')

        digits = []
        for _ in range(5):
            digits.append(num % 85)
            num //= 85
        digits.reverse()

        # на N байт N+1 символ Base85
        chars_to_keep = ours_len + 1

        for d in digits[:chars_to_keep]:
            result.append(_ALPHABET[d])

    # обратно в байты из строчки
    return ''.join(result).encode('ascii')


@beartype
def decode(b: bytes) -> bytes:
    if not b:
        return b""

    # изменяемая последовательность чисел 0 до 255
    result = bytearray()
    # хотим строку обратно
    text = b.decode('ascii')

    for i in range(0, len(text), 5):
        chunk = text[i:i + 5]
        chunk_len = len(chunk)

        partial = 0
        for char in chunk:
            partial = partial * 85 + _DECODE_MAP[ord(char)]

        missing_chars = 5 - chunk_len  # Сколько символов не хватает до 5

        # костыль для работы с остатком от системы счисления 85
        shifted = partial * (85 ** missing_chars)
        missing_value = (-shifted) % (256 ** missing_chars)
        full_num = shifted + missing_value


        decoded_bytes = full_num.to_bytes(4, 'big')
        result.extend(decoded_bytes[:chunk_len - 1])

    return bytes(result)


