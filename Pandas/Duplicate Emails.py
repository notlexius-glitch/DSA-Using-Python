import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicate = (
        person.groupby("email")
        .size()
        .reset_index(name="count")
    )

    return duplicate[duplicate["count"] > 1][["email"]].rename(
        columns={"email": "Email"}
    )