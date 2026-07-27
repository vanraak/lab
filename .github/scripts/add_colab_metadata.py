import json
import os
import glob

COLAB_BLOCK = {"generative_ai_disabled": True, "provenance": []}


def update_ipynb(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    metadata = data.setdefault("metadata", {})
    colab = metadata.setdefault("colab", {})

    changed = False

    if "generative_ai_disabled" not in colab:
        colab["generative_ai_disabled"] = True
        changed = True

    if "provenance" not in colab:
        colab["provenance"] = []
        changed = True

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            f.write("\n")

        print(f"Updated Colab metadata: {path}")
    else:
        print(f"Skipped (already complete): {path}")


if __name__ == "__main__":
    notebooks = glob.glob("**/*.ipynb", recursive=True)

    print(f"Found {len(notebooks)} notebooks")

    for notebook in notebooks:
        update_ipynb(notebook)
