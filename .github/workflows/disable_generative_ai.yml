name: Update Notebooks with Colab Metadata

on:
  push:
    branches:
      - main  # Trigger on pushes to main

jobs:
  update-notebooks:
    runs-on: ubuntu-latest
    steps:
      # 1️⃣ Checkout the repo with full history
      - name: Checkout
        uses: actions/checkout@v3
        with:
          fetch-depth: 0  # Full history to allow force-push

      # 2️⃣ Set up Python
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      # 3️⃣ Run the notebook metadata script
      - name: Add Colab metadata
        run: python .github/scripts/add_colab_metadata.py

      # 4️⃣ Commit changes if there are any
      - name: Commit changes
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git add "*.ipynb"
          git diff --cached --quiet || git commit -m "Add Colab metadata to notebooks"

      # 5️⃣ Force push to automation branch
      - name: Push to automation branch
        run: |
          git branch -M update-notebooks
          git push -f origin update-notebooks

      # 6️⃣ Create or update Pull Request to main
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "Add Colab metadata to notebooks"
          branch: update-notebooks
          title: "Add Colab metadata to notebooks"
          body: "This PR updates all notebooks to include the Colab metadata block."
          base: main
          delete-branch: false
