import os
import ollama
import logging
import pandas as pd
from datetime import datetime

# Step 1: Create Logs folder if it doesn't exist
log_folder = "Logs"
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Step 2: Create log filename with date and time
log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")
log_filepath = os.path.join(log_folder, log_filename)

# Step 3: Set up logging configuration
logging.basicConfig(
    filename=log_filepath,
    level=logging.INFO,  # You can adjust the logging level
    format="%(asctime)s - %(levelname)s - %(message)s",
)

questions = [
    'Is this product edible? Please return "yes" or "no" only, here is an example of how to format your response: "yes", here is an another example of how to format your response: "no"',
    'Is this product a fruit? Please return "yes" or "no" only, here is an example of how to format your response: "yes", here is an another example of how to format your response: "no"',
    'Is this product a vegetable? Please return "yes" or "no" only, here is an example of how to format your response: "yes", here is an another example of how to format your response: "no"',
    'Is this product a meat? Please return "yes" or "no" only, here is an example of how to format your response: "yes", here is an another example of how to format your response: "no"',
    'Is this product a dairy product? Please return "yes" or "no" only, here is an example of how to format your response: "yes", here is an another example of how to format your response: "no"',
    'Is this product an alcoholic beverage? Please return "yes" or "no" only, here is an example of how to format your response: "yes", here is an another example of how to format your response: "no"',
    'Is this product healthy? Please return "yes" or "no" only, here is an example of how to format your response: "yes", here is an another example of how to format your response: "no"',
    'Is this product suitable for vegans? Please return "yes" or "no" only, here is an example of how to format your response: "yes", here is an another example of how to format your response: "no"',
]

# Log the start of processing
logging.info("Starting product analysis...")

for image in os.listdir("images"):
    logging.info(f"Processing image: {image}...")

    answers = []
    for question in questions:
        res = ollama.chat(
            model="llava:13b",
            messages=[
                {
                    "role": "user",
                    "content": question,
                    "images": [f"images/{image}"],
                }
            ],
        )

        answers.append(res["message"]["content"])

    logging.info(f"Answers for {image}: {', '.join(answers)}\n")

logging.info("Product analysis completed.")
