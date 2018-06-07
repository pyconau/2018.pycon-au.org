---
layout: page
title: Talks
permalink: /talks/
---

{% for talk in site.talks %}
    {% if talk.type == "talk" %}
* [{{ talk.title }}]({{talk.url}}) {{ talk.speaker}}
    {% endif %}
{% endfor %}

