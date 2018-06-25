---
layout: talk
snake: rainbow
type: track

talkid: 1004
abstract: placeholder
title: Internet of Things
track: iot

permalink: /internet-of-things-track/


speakers: 
    - name: Lachlan Blackhall
      thumbnailUrl: lachlan-blackhall.png
      twiter: lblackhall
    - name: Mike Leonard
      thumbnailUrl: mike-leonard.png
      twitter: mikerleonard
    - name: Matt Trentini
      thumbnailUrl: matt-trentini.png
      twitter: matt_trentini


abstract: | 
    The Internet of Things (IoT) mini-conf is a day devoted to presentations and demonstrations of how Python powers IoT devices, applications and services. 
---

Talks in this track:

{%- for talk in site.talks -%}
    {% if talk.type == "talk" and talk.track == page.track %}
* [{{ talk.title }}]({{talk.url}}) {% for speaker in talk.speakers %}{{ speaker.name }}{%- endfor -%}{%- endif -%}
{% endfor %}

<hr>

<p align="center">The Internet of Things Specialist Track cannot be run without the generous support of <a href="https://www.espressif.com/">espressif</a><br><br><a href="https://www.espressif.com/"><img src="/static/img/sponsors/Espressif.png" style="width: 300px"/></a></p>
