import json,logging
from assistant.jorel import Jorel

def read_config():
    with open('config/config.json') as file:
        return json.load(file)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s : %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    Jorel(logger = logging , config = read_config())
