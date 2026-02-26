import os
from pyspark.sql import SparkSession

from scripts.etl.extract import extract_data
from scripts.etl.transform import transform_data
from scripts.etl.load import load_data

from config.logging_config import setup_logger

# =========================================
# CONFIGURACIÓN
# =========================================

logger = setup_logger()

INPUT_PATH = os.getenv("INPUT_PATH", "data/raw/data.csv")
OUTPUT_PATH = os.getenv("OUTPUT_PATH", "data/processed/")

EXPECTED_SCHEMA = {
    "id": "int",
    "name": "string",
    "amount": "double"
}

# =========================================
# SPARK SESSION
# =========================================

def create_spark_session():
    logger.info("Creating Spark session")

    spark = SparkSession.builder \
        .appName("ETL Pipeline") \
        .getOrCreate()

    logger.info("Spark session created")
    return spark

# =========================================
# VALIDACIÓN DE SCHEMA
# =========================================

def validate_schema(df):
    logger.info("Validating schema")

    df_dtypes = dict(df.dtypes)

    for col, dtype in EXPECTED_SCHEMA.items():
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

        if df_dtypes[col] != dtype:
            raise ValueError(
                f"Column {col} should be {dtype}, but got {df_dtypes[col]}"
            )

    logger.info("Schema validation passed")

# =========================================
# PIPELINE PRINCIPAL
# =========================================

def run_pipeline():
    logger.info("Pipeline started")

    spark = None

    try:
        # Crear sesión Spark
        spark = create_spark_session()

        # Validar existencia del archivo
        if not os.path.exists(INPUT_PATH):
            logger.warning(f"File not found: {INPUT_PATH}")
            return

        # EXTRACT
        logger.info("Starting extract phase")
        df = extract_data(spark, INPUT_PATH)

        # VALIDATE
        validate_schema(df)

        # TRANSFORM
        logger.info("Starting transform phase")
        df_transformed = transform_data(df)

        # LOAD
        logger.info("Starting load phase")
        load_data(df_transformed, OUTPUT_PATH)

        logger.info("Pipeline finished successfully")

    except Exception as e:
        logger.error(f"Pipeline failed: {str(e)}", exc_info=True)
        raise

    finally:
        if spark:
            logger.info("Stopping Spark session")
            spark.stop()

# =========================================
# ENTRYPOINT
# =========================================

if __name__ == "__main__":
    run_pipeline()