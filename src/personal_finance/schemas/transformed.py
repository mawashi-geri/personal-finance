import polars as pl


deposit_account_transactions_schema = {
    "Entity": pl.String,
    "Account": pl.String,
    "Date": pl.Date,
    "Amount": pl.Float32,
    "TransactionType": pl.Categorical,
    "Description": pl.String,
}
