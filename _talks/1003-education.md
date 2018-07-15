---
layout: talk
talkid: 1003
snake: rainbow

type: track
track: education
title: Education Track
permalink: /education-track/
card: education.png

speakers: 
  - name: Nicky Ringland
    thumbnailUrl: nicky-ringland.png
  - name: Nick Coghlan
    thumbnailUrl: nick-coghlan.png
  - name: Amanda Hogan
    thumbnailUrl: amanda-hogan.png

abstract: | 
    Teaching the basics of software development is hard, so it's best to get them while they're young. Not just development in Python, but also visual programming languages. The Education Specialist Track brings together both educators and creators of educational tools to discuss ideas to help the next generation of programmers. This track also includes the <a href="http://localhost:4000/speak/showcase">Education Showcase</a>.
---

Talks in this track:

{%- for talk in site.talks -%}
    {% if talk.type == "talk" and talk.track == page.track %}
* [{{ talk.title }}]({{talk.url}}) {% for speaker in talk.speakers %}{% if forloop.index0 > 0 %} and {%endif%}{{ speaker.name }}{%- endfor -%}{%- endif -%}
{% endfor %}

<hr>
<p align="center">The Education Specialist Track is seeking a Track Sponsor to help make their event happen.<br>Is that you? <a href="/news/call-for-sponsorship/">Get in touch!</a></p>
