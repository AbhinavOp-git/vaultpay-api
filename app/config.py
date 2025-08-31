import os
from dotenv import load_dotenv

load_dotenv()

# just fetch DATABASE_URL from environment, don't hardcode it here
DATABASE_URL = os.getenv("DATABASE_URL")
