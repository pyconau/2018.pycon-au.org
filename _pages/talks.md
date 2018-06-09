---
layout: page
title: Talks
permalink: /talks/
sponsors: true
---

{% for talk in site.talks %}{% if talk.type == "talk" %}
* [{{ talk.title }}]({{talk.url}}) {% for speaker in talk.speakers %}{{ speaker.name }}{% endfor %}
{% endif %}{% endfor %}

