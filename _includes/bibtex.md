{% assign publication=include.publication %}
{% assign key=publication.author[0] %}
{% assign keys = "volume,number,doi,pages" | split: "," %}
```
@{{ publication.type }}{
    {{site.data.collaborators[key].last}}{{publication.date | date: "%Y"}},
    title = "{{publication.title}}",
    author = "{% for key in publication.author %}{% assign author=site.data.collaborators[key]%}{{author.last}}, {{author.first}}{% if forloop.last == false%} and {%endif%}{%endfor%}",
    journal = "{{publication.venue}}",
    year = "{{publication.date | date: "%Y"}}",
{%for key in keys %}{% if publication[key]%}    {{key}} = "{{publication[key]}}",
{%endif%}{%endfor%}}
```
