import marvin


@marvin.fn
def list_fruits(n: int, color: str) -> list[str]:
    """Generates a list of `n` fruits that are `color`"""


fruits = list_fruits(3, color='red')