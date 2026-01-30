import polars as pl

from personal_finance.schemas.transformed import deposit_account_transactions_schema


def transform_barclays_deposit_account_transactions(df: pl.DataFrame) -> pl.DataFrame:
    transformed = df.with_columns(
        [
            pl.col("Subcategory").alias("TransactionType").cast(pl.Categorical),
            pl.col("Memo").alias("Description").cast(pl.Categorical),
        ]
    ).select(deposit_account_transactions_schema.keys())

    return transformed


def transform_skipton_deposit_account_transactions(df: pl.DataFrame) -> pl.DataFrame:
    transformed = df.with_columns(
        [
            (pl.col("Money In") - pl.col("Money Out")).alias("Amount").cast(pl.Float64),
            pl.col("Category").alias("TransactionType").cast(pl.Categorical),
        ]
    ).select(deposit_account_transactions_schema.keys())

    return transformed


transform_functions = {
    "Barclays": transform_barclays_deposit_account_transactions,
    "Skipton": transform_skipton_deposit_account_transactions,
}
