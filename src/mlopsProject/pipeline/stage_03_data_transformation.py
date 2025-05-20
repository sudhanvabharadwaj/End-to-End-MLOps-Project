from mlopsProject.config.configuration import ConfigurationManager
from mlopsProject.components.data_transformation import DataTransformation
from mlopsProject import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path('artifacts/data_validation/status.txt'), 'r') as file:
                status = file.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Your data schema is not valid. Please check the data validation stage.")
        
        except Exception as e:
            raise e

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e