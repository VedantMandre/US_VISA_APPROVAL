import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import and run the pipeline
from us_visa.pipline.training_pipeline import TrainPipeline

pipeline = TrainPipeline()
pipeline.run_pipeline()
