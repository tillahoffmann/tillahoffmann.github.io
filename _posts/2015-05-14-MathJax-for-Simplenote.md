[Simplenote](http://simplenote.com) is a note-taking application that syncs your notes across devices. They recently added [Markdown](http://daringfireball.net/projects/markdown/) capabilities but do not support [MathJax](http://www.mathjax.org), which is essential for many scientists. The following JavaScript injects MathJax into the Simplenote application such that equations are typeset when you click the "Preview" button in Simplenote. I use Safari and have written a small extension which adds MathJax support to Simplenote. You can get it here (Google Drive link): [simplenote_mathjax.safariextz](https://drive.google.com/file/d/0BwG2uZkT-BMOV3pSUERlZXFqRkk/view?usp=sharing) The script should also work with [Greasemonkey](http://www.greasespot.net).

{% highlight javascript linenos %}
if (window.MathJax === undefined) {
//Add the MathJax script
var script = document.createElement("script");
script.type = "text/javascript";
script.src = "//cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML";
var config = 'MathJax.Hub.Config({'
+ 'extensions: ["tex2jax.js"],'
+ 'tex2jax: { inlineMath: [["$","$"],["\\\\\\\\\\\\(","\\\\\\\\\\\\)"]], displayMath: [["$","$"],["\\\\[","\\\\]"]], processEscapes: true },'
+ 'jax: ["input/TeX","output/HTML-CSS"]' + '});';
if (window.opera) {
script.innerHTML = config
} else {
script.text = config
}
document.getElementsByTagName("head")[0].appendChild(script);

//Add the reload tag
script = document.createElement("script");
script.text = 'document.getElementById("view_mode_markdown").onclick = '
+ 'function() {MathJax.Hub.Queue(["Typeset", MathJax.Hub, "static_content"]);};';
document.getElementsByTagName("head")[0].appendChild(script);
} else {
//Render the content
MathJax.Hub.Queue(["Typeset", MathJax.Hub, "static_content"]);
}
{% endhighlight %}
