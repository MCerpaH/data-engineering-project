import logging
from pyspark.sql.functions import col

logger = logging.getLogger(__name__)

def transform_data(df):
    logger.info("Starting transformations")

    df_clean = df.dropna()
    logger.info(f"Rows after dropna: {df_clean.count()}")

    df_transformed = df_clean \
        .withColumn("amount", col("amount").cast("double")) \
        .withColumn("amount_with_tax", col("amount") * 1.19)

    logger.info("Transformations completed")

    return df_transformed