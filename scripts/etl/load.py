import logging

logger = logging.getLogger(__name__)

def load_data(df, output_path):
    logger.info(f"Writing data to {output_path}")

    df.write \
        .mode("overwrite") \
        .parquet(output_path)

    logger.info("Data successfully written")