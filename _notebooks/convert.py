from argparse import ArgumentParser
from pathlib import Path
import shutil
from subprocess import call


# Get arguments
ap = ArgumentParser("convert")
ap.add_argument("notebook", help="notebook to convert", type=Path)
args = ap.parse_args()

# Call the converter.
call(["jupyter", "nbconvert", "--to", "markdown", "--output-dir=_posts", args.notebook])

# Get the name of the notebook, markdown path, and markdown text.
name = args.notebook.with_suffix("").name
markdown_path = Path("_posts", f"{name}.md")
markdown = markdown_path.read_text()

# Move the assets.
file_prefix = f"{name}_files"
asset_directory = Path(f"assets/{name}")
if asset_directory.is_dir():
    shutil.rmtree(asset_directory)
Path("_posts", file_prefix).rename(asset_directory)

# Determine the name of the support file directory, replace all instances, and save.
markdown = markdown.replace(file_prefix, f"/assets/{name}")
markdown_path.write_text(markdown)
