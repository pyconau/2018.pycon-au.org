import requests
import json
import sys
import os
import re
import pdb
import shutil
import hashlib
import yaml

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

def track_info(tags):
    TRACKS = {"gen_accepted": "general",
              "iot_accepted": "iot",
              "sec_accepted": "security",
              "DCAU_accepted": "django",
              "EduSeminarAccepted": "education"}

    for t in tags: 
        if t in TRACKS.keys():
            return TRACKS[t]

    return None

def record_consent(info):
    if len(sys.argv) > 2:
        if sys.argv[2] == "-f":
            return True

    print("\n" + info + "\n")
    resp = input("Is this consent? (y/n): ")
    if resp.lower() == "y":
        print("\nMarking talk as 'Yes, record my talk'")
        return True
    else:
        print("\nMarking talk as 'No, do not record my talk'")
        return False


def safecase(string):
    return re.sub(r"[^\w\s]", "", string).lower().replace(" ", "-")


fp = "%s-%s.md" % (talk_id, safecase(talk["talk"]["title"]))
talk_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '_talks', fp))

g_hash = hashlib.md5(bytes(talk["profile"]["email"], "utf-8")).hexdigest()

gravatar = f"https://s.gravatar.com/avatar/{g_hash}?s=200&default=https%3A%2F%2Fpyconau-test.glasnt.com%2Fstatic%2Fimg%2Fpeople%2Fcurlyboi.png"

print(gravatar)

image_name = safecase(talk["profile"]["name"]) + ".png"
image_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'static','img','people', image_name))

r = requests.get(gravatar, stream=True)
if r.status_code == 200:
    with open(image_path, "wb") as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)

e = {}

e["layout"] = "talk"
e["type"] = "talk"
e["talkid"] = int(talk_id)
e["title"] = talk["talk"]["title"]
e["track"] = track_info(talk["tags"])
e["recordingconsent"] = record_consent(talk["additional_info"])

s = [{}]
for x in ["name", "company", "twitter", "url", "bio"]:
    s[0][x] = talk["profile"][x]
s[0]["thumbnailUrl"] = image_name
s = {"speakers": s}

a = {}
a["abstract"] = talk["talk"]["abstract"]

d = talk["talk"]["description"]

with open(talk_path, "w") as f:
    f.write("---\n")
    yaml.dump(e, f, default_flow_style=False)
    f.write("\n")
    yaml.dump(s, f, default_flow_style=False)
    f.write("\n")
    yaml.dump(a, f, default_flow_style=False)
    f.write("---\n")
    f.write(d)
    f.write("\n")


print(talk_path)
