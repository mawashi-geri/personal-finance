
import polars as pl


barclays_transactions_schema = {
    "Number": pl.String,
    "Date": pl.Date,
    "Account": pl.String,
    "Amount": pl.Float32,
    "Subcategory": pl.Categorical,
    "Memo": pl.String,
}

skipton_transactions_schema = {
    "Account": pl.String,
    "Date": pl.Date,
    "Description": pl.String,
    "Money In": pl.Float32,
    "Money Out": pl.Float32,
    "Balance": pl.Float32,  # "income" or "expense"
}

source_deposit_account_schemas = {
    "Barclays": barclays_transactions_schema,
    "Skipton": skipton_transactions_schema,
}
