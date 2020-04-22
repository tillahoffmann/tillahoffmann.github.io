---
layout: default
title: Publications
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
  {% for publication in site.posts %}
  {% if publication.layout == 'publication' %}
  <li class="clearfix">
  <span class="post-meta">{{ publication.date | date: date_format }}</span>
  <h3 style="margin-bottom: 0;">
    <a class="post-link" href="{{ publication.url | relative_url }}">
    {{ publication.title | escape }}
    </a>
  </h3>
  {% include publication_metadata.html citation=publication.citation %}
  {% if publication.thumbnail %}
  <img src="{{publication.thumbnail}}" style="float: left; max-width: 25%; margin-right: 1em;"/>
  {% endif %}
  {{ publication.excerpt }}
</li>
{%endif%}
{%- endfor -%}
</ul>
