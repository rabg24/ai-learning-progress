How to open the starter notebook in Google Colab

1. Open Google Colab at https://colab.research.google.com
2. Choose File -> Upload notebook and upload `examples/colab_starter.ipynb`, or select GitHub and paste the repo URL after you've pushed the files.
3. Install required packages (the notebook already installs transformers).
4. Run the cells sequentially. Use the `colab_starter.py` for quick inference demos or convert code cells into your own notebook cells.
5. To share: File -> Save a copy in Drive or share the Colab link.

Tips:
- Use GPU runtime in Colab for larger models: Runtime -> Change runtime type -> GPU.
- For reproducibility, pin package versions and note the runtime in the issue checklist.
