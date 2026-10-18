#!/usr/bin/env python3
"""Open a GitHub issue in this repo for each new, claimable ZecHub bounty.

Reads ZecHub's public bounty API (no login needed). A bounty counts when it is
TO_DO, approved, public, unassigned, not past its deadline and not a test post.
Each alert carries the bounty id, so the same bounty is never alerted twice.
Run with --dry-run to print what would be opened.
"""
import datetime
import json
import re
import subprocess
import sys
import urllib.request

API = "https://zechub.zone/api/bounties"
BOUNTY_URL = "https://bounties.zechub.wiki/bounties/{id}"
LABEL = "zechub-bounty"
MATCH_LABEL = "matches-you"
MATCH_WORDS = re.compile(
    r"translat|greek|ελλην|nonprofit|non-profit|donat|charit|educat|explainer|"
    r"newsletter|digest|zecweekly|shielded news|wiki|next\.?js|react|tachyon",
    re.IGNORECASE,
)
TEST_TITLE = re.compile(r"^\W*(test|prueba)\b|tarea de prueba", re.IGNORECASE)


def fetch_all():
    bounties, page = [], 1
    while True:
        req = urllib.request.Request(f"{API}?limit=50&page={page}", headers={"User-Agent": "zechub-bounty-alerts"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.load(resp)
        bounties.extend(data["data"])
        if page * data["limit"] >= data["total"] or not data["data"]:
            return bounties
        page += 1


def is_claimable(b, today):
    deadline = (b.get("timeToComplete") or "")[:10]
    return (
        b.get("status") == "TO_DO"
        and b.get("isApproved")
        and not b.get("isPrivate")
        and not b.get("assignees")
        and not b.get("assignee")
        and not TEST_TITLE.search(b.get("title") or "")
        and (not deadline or deadline >= today)
    )


def quiet(text):
    # Bounty text is written by others: stop @mentions and #refs from pinging anyone.
    return text.replace("@", "@​").replace("#", "#​")


def gh(*args):
    return subprocess.run(["gh", *args], check=True, capture_output=True, text=True).stdout


def already_alerted():
    out = gh("issue", "list", "--label", LABEL, "--state", "all", "--limit", "1000", "--json", "body")
    return {m for issue in json.loads(out) for m in re.findall(r"bounty-id: (\S+)", issue["body"] or "")}


def issue_for(b):
    team = (b.get("team") or {}).get("name") if isinstance(b.get("team"), dict) else None
    desc = " ".join((b.get("description") or "").split())
    if len(desc) > 1200:
        desc = desc[:1200] + "…"
    matched = bool(MATCH_WORDS.search(f"{b.get('title', '')} {desc}"))
    title = f"ZecHub bounty: {b['title'].strip()[:90]} ({b.get('bountyAmount')} ZEC)"
    body = "\n".join([
        f"**[Open the bounty and apply]({BOUNTY_URL.format(id=b['id'])})**",
        "",
        f"- Reward: {b.get('bountyAmount')} ZEC",
        f"- Deadline: {(b.get('timeToComplete') or 'none')[:10]}",
        f"- Difficulty: {b.get('difficulty') or 'not set'}",
        f"- Posted by team: {team or 'ZecHub admins'}",
        f"- Fits your areas: {'yes' if matched else 'no'}",
        "",
        "> " + quiet(desc),
        "",
        "Apply with a short, specific note: your plan, timeline and one relevant link.",
        "",
        f"<!-- bounty-id: {b['id']} -->",
    ])
    labels = [LABEL] + ([MATCH_LABEL] if matched else [])
    return quiet(title), body, labels


def main():
    dry = "--dry-run" in sys.argv
    today = datetime.date.today().isoformat()
    claimable = [b for b in fetch_all() if is_claimable(b, today)]
    seen = set() if dry else already_alerted()
    new = [b for b in claimable if b["id"] not in seen]
    print(f"{len(claimable)} claimable, {len(new)} new")
    if not dry and new:
        gh("label", "create", LABEL, "--color", "F4B728", "--description", "New claimable ZecHub bounty", "--force")
        gh("label", "create", MATCH_LABEL, "--color", "2F6FDE", "--description", "Matches translation, nonprofit or education work", "--force")
    for b in new:
        title, body, labels = issue_for(b)
        if dry:
            print(f"--- {title} {labels}\n{body}\n")
            continue
        args = ["issue", "create", "--title", title, "--body", body]
        for label in labels:
            args += ["--label", label]
        print(gh(*args).strip())


if __name__ == "__main__":
    main()
