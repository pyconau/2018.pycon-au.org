---
layout: page
title: Talks
permalink: /talks/
---

<ul>
{% for talk in site.talks %}
    <li> {{ talk.talk-id }} {{ talk.title }} {{ talk.url }}
{% endfor %}

</ul>

