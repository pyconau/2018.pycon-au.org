import yaml

with open("sessions.yml") as f:
    data = yaml.safe_load(f)

for d in data:

    talk_id = '%03d' % d["id"]

    fp = talk_id + "-" + d["title"].lower().replace(" ","-") + ".md"

    fc = ["---", "layout: talk"]
    fc.append("talk-id: %s" % talk_id)

    for i in ["description", "abstract",  "subtype", "title", "place", "speakers", "complexity"]:
        if i in d.keys():
            fc.append("%s: %s" % (i, d[i]))

    fc.extend(["---","\n"])

    with open(fp, "w") as f:
        f.write("\n".join(fc))


