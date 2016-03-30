from subprocess import call
from argparse import ArgumentParser
from datetime import datetime
from os import path

# Get arguments
ap = ArgumentParser('convert')
ap.add_argument("--date", type=lambda x: datetime.strptime(x, "%Y-%m-%d"))
ap.add_argument("--layout", default="post")
ap.add_argument("--title")
ap.add_argument("--published", default=True, type=bool)
ap.add_argument("--mathjax", default=True, type=bool)
ap.add_argument("notebook")
args = ap.parse_args()

# Call the converter in the local directory (nbconvert seems to struggle with a specified output directory)
call(['jupyter', 'nbconvert', '--to', 'markdown', args.notebook])

# Get the name of the notebook
notebook_name, ext = path.splitext(args.notebook)

# Get the date for the post (use the creation date by default)
date = args.date or datetime.fromtimestamp(path.getctime(args.notebook))

# Get the name of the newly created post
post_name = "{:%Y-%m-%d}-{}".format(date, notebook_name)

# Get the original markdown
with open(notebook_name + '.md') as fp:
    markdown = fp.read()

# Determine the name of the support file directory
support = notebook_name + '_files'

# Replace all references to the support files
markdown = markdown.replace(support + '/', '/media/' + post_name + '/')

front_matter = {
    'layout': args.layout,
    'published': args.published,
}
if args.title:
    front_matter['title'] = args.title

content = ['---']
content.extend(["{}: {}".format(*item) for item in front_matter.iteritems()])
content.extend(['---', ''])

content.append(markdown)

if args.mathjax:
    content.append('{% include mathjax.html %}')

# Save it to the output directory
output = "../_posts/{}.md".format(post_name)
with open(output, 'w') as fp:
    fp.write('\n'.join(content))

# Delete the original files
call(['rm', notebook_name + '.md'])

# Delete the support directory
media_dir = '../media/' + post_name
if path.exists(media_dir):
    call(['rm', '-r', media_dir])

if path.exists(support):
    # Move the support files to the media directory
    call(['mv', support, media_dir])