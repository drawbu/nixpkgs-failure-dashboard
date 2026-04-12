import os
import json
import random
import string
import shutil
from datetime import datetime

from .config import RUNTIME_DIR, BUILD_LOGS_DIR


def generate_nix_hash():
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(32))


def create_dummy_commit():
    dummy_data = {
        "rev": "2766a4b44ee6eafae03a042801270c7f6b8ed32a",
        "name": f"You are using dummy data",
        "date": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    }

    with open(RUNTIME_DIR / "last-commit.json", "w") as f:
        json.dump(dummy_data, f, indent=2)


def main():
    os.makedirs(BUILD_LOGS_DIR, exist_ok=True)

    for file in os.listdir("samples"):
        shutil.copyfile(f"samples/{file}", BUILD_LOGS_DIR / file)

    create_dummy_commit()


if __name__ == "__main__":
    main()
