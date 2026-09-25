#!/usr/bin/env python3
"""Rewrite the upstream list in README.md between the PRS markers.

Reads https://dhairyashilrg.dev/cv.json, which the site builds from its own PR data, so the profile
and the site always show the same list and counts. No token needed.
"""
import json
import re
import sys
import urllib.request

SRC = sys.argv[1] if len(sys.argv) > 1 else "https://dhairyashilrg.dev/cv.json"


def load(src):
    if src.startswith("http"):
        # Cloudflare answers 403 to Python's default user agent; name ourselves instead.
        req = urllib.request.Request(src, headers={"User-Agent": "dhairyashilRG-profile-readme/1.0 (+https://github.com/dhairyashilRG)"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    with open(src, encoding="utf-8") as f:
        return json.load(f)


def main():
    pr = load(SRC)["pull_requests"]
    lines = [f"{pr['merged']} merged, {pr['open']} under review. The list updates itself from "
             f"[the site](https://dhairyashilrg.dev/work).", ""]
    for p in pr["items"]:
        state = p["state"]
        if p.get("superseded_by"):
            n = p["superseded_by"].split("#")[1]
            state = f"closed, superseded by [#{n}](https://github.com/{p['superseded_by'].replace('#', '/pull/')})"
        title = p["title"].replace("|", "\\|")
        lines.append(f"- [{p['repo']}#{p['number']}]({p['url']}) {title} ({state})")
    block = "<!-- PRS:START -->\n" + "\n".join(lines) + "\n<!-- PRS:END -->"
    readme = open("README.md", encoding="utf-8").read()
    new = re.sub(r"<!-- PRS:START -->.*?<!-- PRS:END -->", lambda _: block, readme, flags=re.S)
    if new != readme:
        open("README.md", "w", encoding="utf-8").write(new)
        print("README.md updated")
    else:
        print("no change")


if __name__ == "__main__":
    main()
