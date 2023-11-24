# Exceptions
class BillTitleLengthError(BaseException):
    def __init__(self, bill_id, title):
        super().__init__(
            f"Title of {bill_id} exceeds 300 characters:"
            f"\n title -> '{title}'"
            f"\n character length -> {len(title)}"
        )


class SelectorError(ValueError):
    """
    Error raised when a selector's constraint (min_items/max_items, etc.) is not met.
    """
    pass
