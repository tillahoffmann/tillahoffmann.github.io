---
layout: default
title: Blog
---

<style>
.clearfix::after {
  content: "";
  clear: both;
  display: table;
}
</style>

{%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
<ul class="post-list">
  {% for post in site.posts %}
  <li class="clearfix">
    <span class="post-meta">{{ post.date | date: date_format }}</span>
    <h3 style="margin-bottom: 0;">
      <a class="post-link" href="{{ post.url | relative_url }}">
      {{ post.title | escape }}
      </a>
    </h3>
    {% if post.layout == 'publication' %}
      {% include publication_metadata.html publication=post %}
    {%endif%}
    {% if post.thumbnail %}
      <img src="{{post.thumbnail}}" style="float: left; max-width: 25%; margin-right: 1em;"/>
    {% endif %}
    {{ post.excerpt }}
  </li>
{%- endfor -%}
</ul>

{% include mathjax.html %}
