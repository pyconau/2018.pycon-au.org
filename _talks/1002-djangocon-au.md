---
layout: talk
type: track
snake: rainbow

talkid: 1002
track: django
title: DjangoCon AU

permalink: /djangoconau/
card: django.png

speakers: 
    - name: Adam Brenecki
      company: CMV Group
      twitter: adambrenecki
      url: https://adam.brenecki.id.au
      thumbnailUrl: adam-brenecki.png
    - name: Markus Holtermann
      thumbnailUrl: markus-holtermann.png
      twitter: m_holtermann
      url: https://markusholtermann.eu
      company: LaterPay GmbH

abstract: <a href="https://2018.djangocon.com.au/">DjangoCon AU</a> has been running as a mini-conference inside PyCon AU since 2013. Now in it's 6th year, it is the younger sibling conference to <a href="https://2018.djangocontent.eu">DjangoCon Europe</a> and <a href="https://2018.djangocon.us/">DjangoCon US</a>
---
Talks in this track:

{%- for talk in site.talks -%}
    {% if talk.type == "talk" and talk.track == page.track %}
* [{{ talk.title }}]({{talk.url}}) {% for speaker in talk.speakers %}{{ speaker.name }}{%- endfor -%}{%- endif -%}
{% endfor %}


<hr>

<p align="center">DjangoCon AU cannot be run without the generous support of the <a href="https://www.djangoproject.com/foundation/">Django Software Foundation</a><br><br><a href="https://www.djangoproject.com/foundation/"><img src="/static/img/sponsors/django.png" style="width: 200px"/></a></p>
