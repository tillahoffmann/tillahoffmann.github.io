---
layout: post
---

There are a range of approaches to versioning [Jupyter notebooks](http://jupyter.org/) using git (e.g. [here](https://gist.github.com/pbugnion/ea2797393033b54674af), [here](https://github.com/toobaz/ipynb_output_filter), and [here](http://timstaley.co.uk/posts/making-git-and-jupyter-notebooks-play-nice/)) by removing any output before adding the notebooks to git. But they typically rely on adding a script to your executable path that can be invoked by a [git filter](https://git-scm.com/book/en/v2/Customizing-Git-Git-Attributes#filters_a) to remove any output.

> **Update**: [`jupytext`](https://jupytext.readthedocs.io/en/latest/) can store notebooks as markdown and is recommended for versioning notebooks.

Fortunately, Jupyter's own [nbconvert](http://nbconvert.readthedocs.io/en/latest/) can achieve the same task, which

* avoids adding scripts to your exectuable path,
* ensures that removing the output is always compatible with the Jupyter and python versions you are using.

Here's how to set it up: First, open your `~/.gitconfig` and add the following lines.

```ini
[filter "jupyter_clear_output"]
    clean = "jupyter nbconvert --stdin --stdout --log-level=ERROR \
             --to notebook --ClearOutputPreprocessor.enabled=True"
    smudge = cat
    required = true
```

The lines define a git filter called `jupyter_clear_output` which applies the `clean` filter when changes are staged and the `smudge` filter when files are checked out. The `smudge` filter is trivial: it just reproduces the input. The `clean` filter invokes nbconvert, reading from `stdin`, writing to `stdout`, converting to the notebook file format, and clearing all output. The flag `required = true` ensures that the filter does not fail silently.

The final step is to register the `.ipynb` extension with the `jupyter_clear_output` filter. If you would like to enable the filter on a per-repository basis, simply add a `.gitattributes` with the following content to your repository.

```ini
*.ipynb    filter=jupyter_clear_output
```

If you want to enable the filter globally, add the line above to `~/.gitattributes` and let git know about the attributes file by adding the following line to your `~/.gitconfig`.

```ini
[core]
    attributesfile = ~/.gitattributes
```
