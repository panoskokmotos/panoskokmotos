# Substack drafts

Staging area for Substack posts. Substack has no public publishing API, so this
folder is the "upload" — version-controlled drafts that sync back to me via git,
ready to paste-and-publish.

## Workflow

1. Share raw thoughts, notes, or a voice-memo-style ramble with Claude — the
   `substack-drafter` skill (in `.claude/skills/`) turns it into a polished,
   Substack-ready essay.
2. The draft lands in `drafts/` as a Markdown file with title options, a subtitle,
   pull-quotes, and the paste-ready body.
3. Paste the body into Substack, publish.
4. Move the file to `published/` and set `status: published` in its frontmatter.

## Folders

- `drafts/` — work in progress
- `published/` — shipped pieces (for the record)
