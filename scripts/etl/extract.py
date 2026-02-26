import logging


logger = logging.getLogger(__name__)

def extract_data(spark, input_path):
    logger.info(f"Reading data from {input_path}")

    df = spark.read \
        .option("header", True) \
        .option("inferSchema", True) \
        .csv(input_path)

    logger.info(f"Data extracted with {df.count()} rows")

    return df