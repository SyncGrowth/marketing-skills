# Security policy

Skills are instructions that an AI agent follows, and some of them ship small scripts and code snippets. A vulnerability here means something that could make an agent act against the user: a hidden or misleading instruction, a script that does more than it says, a leaked secret, or a link that sends people somewhere unsafe.

## Reporting

Please report privately and do not open a public issue.

1. Use GitHub's private vulnerability reporting: **Security** tab, then **Report a vulnerability**.
2. If that is not available to you, write to kontakt@syncgrowth.pl with "marketing-skills security" in the subject.

Include the skill and file, what you observed, and how an agent or a user could be affected. We acknowledge reports as soon as a maintainer reads them and keep you informed until the fix is released. We credit reporters in the changelog unless you prefer otherwise.

## What is in scope

- Instructions in any `SKILL.md` or reference that cause an agent to exfiltrate data, run unexpected commands, or hide behavior from the user.
- Scripts in `skills/*/scripts/` and snippets in `skills/*/assets/`.
- Hidden content: zero-width or bidirectional characters, long blank runs, HTML comments in prose.
- Secrets or private data committed by mistake.
- Supply chain issues in the CI workflow.

## What is not in scope

- Marketing advice you disagree with. Open a normal issue for that.
- Behavior of third-party tools that a skill mentions.

## What we already check

`scripts/validate_skills.py` runs on every pull request. Besides the Agent Skills format, it rejects hidden characters, long blank runs, HTML comments in prose, secret-shaped strings, and private paths. Skills do not contain instructions to append footers, links, or calls to action to the agent's output, and a pull request that adds one will be declined.

## Supported versions

Only the latest release receives fixes.
