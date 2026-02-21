import sys
from us_visa.exception import CustomException
from us_visa.logger import logging
from us_visa.components.data_ingestion import DataIngestion
from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact


class TrainPipeline:
    def __init__(self):
        try:
            self.data_ingestion_config = DataIngestionConfig()
        except Exception as e:
            raise CustomException(e, sys) from e
        

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info(f"Starting data ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
            logging.info(f"Completed data ingestion")
            return data_ingestion_artifact
        except Exception as e:
            raise CustomException(e, sys) from e
        

    def run_pipeline(self,) -> None:
            try:
                data_ingestion_artifact = self.start_data_ingestion()
                logging.info(f"Data ingestion completed and data ingestion artifact: {data_ingestion_artifact}")
            except Exception as e:
                raise CustomException(e, sys) from e