---
layout: post
published: true
---

[Simplenote](http://simplenote.com) is a note-taking application that syncs your notes across devices. They recently added [Markdown](http://daringfireball.net/projects/markdown/) capabilities but do not support [MathJax](http://www.mathjax.org), which is essential for many scientists. The following JavaScript injects MathJax into the Simplenote application such that equations are typeset when you click the "Preview" button in Simplenote. I use Safari and have written a small extension which adds MathJax support to Simplenote. You can get it here (Google Drive link): [simplenote_mathjax.safariextz](https://drive.google.com/file/d/0BwG2uZkT-BMOV3pSUERlZXFqRkk/view?usp=sharing) The script should also work with [Greasemonkey](http://www.greasespot.net).

{% gist e03a7a9cf4059e92774b %}
