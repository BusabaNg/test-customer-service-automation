import os
from dotenv import load_dotenv

# read environment variables from .env
package_path = os.path.dirname(os.path.realpath(__file__))
path_to_env = os.path.join(package_path, "../.env")
load_dotenv(path_to_env)

# OpenAI API key
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")