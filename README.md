# Presto Design Skill

This repository is packaged for Vercel `skills` CLI discovery.

## Install

Install directly from GitHub:

```powershell
npx skills add MapleCity1314/presto-design-skill --skill presto-design
```

Or install the skill folder URL:

```powershell
npx skills add https://github.com/MapleCity1314/presto-design-skill/tree/main/skills/presto-design
```

## Repo Layout

```text
skills/
  presto-design/
    SKILL.md
    agents/openai.yaml
    clusters/
    context/
    presets/
    evals/
    contract.md
    gsap-integration.md
```

The publishable skill lives under `skills/presto-design/`. Local fixtures, test workspaces, and planning docs are intentionally excluded from this repository layout.
