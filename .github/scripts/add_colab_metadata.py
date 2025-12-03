import json
import os

COLAB_BLOCK = {"generative_ai_disabled": True, "provenance": []}


def update_ipynb(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    metadata = data.setdefault("metadata", {})

    if "colab" not in metadata:
        metadata["colab"] = COLAB_BLOCK
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"Added 'colab' block: {path}")
    else:
        print(f"Skipped (already has 'colab'): {path}")


def update_all_notebooks(root="."):
    for dirpath, _, files in os.walk(root):
        for file in files:
            if file.endswith(".ipynb"):
                update_ipynb(os.path.join(dirpath, file))


if __name__ == "__main__":
    update_all_notebooks(".")
