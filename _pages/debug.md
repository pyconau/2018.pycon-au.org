---
layout: page
title: Debug
snake: grey
permalink: /debug/

---

### Talks

Count: {{ site.talks | size }}

{% for session in site.talks %}
    {{ session.title }} {{ session.url }}
{% endfor %}


### Sponsors

Count: 
{% for l in site.data.sponsors %}
    {{ l.title }}: {{ l.sponsors | size}}
{% endfor %}


{{ site.talks }}
