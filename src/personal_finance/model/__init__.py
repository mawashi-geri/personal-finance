import polars as pl

schema = {
    "id": pl.Int32,
    "date": pl.Date,
    "category": pl.String,
    "description": pl.String,
    "amount": pl.Float64,
    "transaction_type": pl.Categorical,  # "income" or "expense"
}