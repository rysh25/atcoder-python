import io
import sys

_INPUT = """\
3
2 6 2

"""

sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

N = int(input())
a = tuple(map(lambda x: int(x) - 1, input().split()))
