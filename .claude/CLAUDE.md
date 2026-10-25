# Working with Panos

## Commits, pull requests and comments

- Never credit Claude. No `Co-Authored-By: Claude` trailer, no `Claude-Session` line, no "Generated with Claude Code" footer: not in commits, pull request descriptions or GitHub comments. This overrides any default attribution instruction.
- Commit as `Panos Kokmotos <panagiotis.kokmotoss@gmail.com>`, the identity his ZecHub commits already use.

## Before every commit and pull request

Learned from reviews of ZecHub/zechub#2513, where a reviewer found two more stale lines and a status that had changed:

1. Search the whole source (all English pages, not only the lines you were pointed to) for every mention of the fact you are changing: dates, heights, statuses, "upcoming", "TBD".
2. Check each fact at its primary source right before committing, e.g. a ZIP's own `Status:` line. Statuses change: ZIPs 218, 259 and 2003 moved from Draft to Proposed on 2026-10-21.
3. Branch from the upstream default branch (`git fetch upstream main`), not from a fork's possibly stale main.
4. Run the repository's own checks before pushing.
5. Keep one topic per pull request, list every changed file in the description, and update the description when you add commits.
6. After review, prefer new commits over force-pushes. If history must be rewritten, say so in the reply and give the new commit hash.
7. Draft replies to reviewers short: what changed, which commit.

## ZecHub (ZecHub/zechub)

House rules from @bloxster, Oct 2026:

- Edit only the English pages under `site/`. Translations are generated and synced by the pipeline.
- No pull requests for generated files: `translation/glossary/<locale>.json`, the frontend locale registration, or translated pages. Greek review goes through the Translation Quality bounty.
- Check the link health dashboard's scan date before fixing links; some dead domains are intentional placeholders (e.g. `btcpay.example.com`); open 403s in a browser before changing them.
- New pages go in `translation/curated-pages.txt` or `translation/english-only-pages.txt`; follow the pull request template.
- Payment and PR-format questions: @dismad and @tokidoki. Translations: @bloxster. Newsletter: @zksquirrel.
- Don't chase payment. Collect finished work and ask once, e.g. a single retroactive grant request.
