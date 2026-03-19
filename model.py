class Credential:
    """Entity class representing a single credential entry."""
    def __init__(self, amount, category, date, id=None):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date

    def to_dict(self):
        """Convert object to dictionary for JSON storage."""
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        """Create object from dictionary."""
        return cls(
            id=data.get("id"),
            amount=data.get("amount"),
            category=data.get("category"),
            date=data.get("date")
        )
