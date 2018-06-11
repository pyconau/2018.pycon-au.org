import requests
import json
import sys
import os
import re
import pdb
import shutil
import hashlib

if len(sys.argv) < 2:
    sys.exit("Usage: talk_id")

talk_id = sys.argv[1]

PAPERCALL_API = os.environ.get("PAPERCALL_API")
if not PAPERCALL_API:
    sys.exit("PAPERCALL_API environment variable not found")


def _get(uri):
    return requests.get(uri, headers={"Authorization": PAPERCALL_API})


def _pag(resp):
    return json.loads(resp.headers["x-pagination"])


def get_submission_by_id(talk_id):
    URI = "https://www.papercall.io/api/v1/submissions/%s" % talk_id

    resp = _get(URI)

    return resp.json()


talk = get_submission_by_id(talk_id)


def safecase(string):
    return re.sub(r"[^\w\s]", "", string).lower().replace(" ", "-")


fp = "%s-%s.md" % (talk_id, safecase(talk["talk"]["title"]))
talk_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '_talks', fp))

g_hash = hashlib.md5(bytes(talk["profile"]["email"], "utf-8")).hexdigest()

gravatar = "https://s.gravatar.com/avatar/%s?s=200" % g_hash

print(gravatar)

image_name = safecase(talk["profile"]["name"]) + ".png"
image_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'static','img','people', image_name))

r = requests.get(gravatar, stream=True)
if r.status_code == 200:
    with open(image_path, "wb") as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)

print(image_path)

entry = []

entry.append("---")
entry.append("layout: talk")
entry.append("type: talk")
entry.append("talk_id: %s" % talk_id)
entry.append('title: "%s"' % talk["talk"]["title"])
entry.append("speakers: ")
entry.append('  - name: "%s"' % talk["profile"]["name"])
entry.append('    thumbnailUrl: "%s"' % image_name)
for x in ["company", "twitter", "url", "bio"]:
    if talk["profile"][x]:
        entry.append('    %s: "%s"' % (x, talk["profile"][x]))
entry.append(" ")
entry.append('abstract: "%s"' % talk["talk"]["abstract"])
entry.append("---")
entry.append("  ")
entry.append(talk["talk"]["description"])

with open(talk_path, "w") as f:
    f.write("\n".join(entry))

print(talk_path)
