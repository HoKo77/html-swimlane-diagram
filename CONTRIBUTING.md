# Contributing

Thanks for improving this skill.

## Guidelines

- Keep `SKILL.md` concise and procedural.
- Move detailed domain guidance into `references/`.
- Add deterministic validation logic to `scripts/` when possible.
- Do not commit generated screenshots, local previews, `.DS_Store`, or private workspace paths.
- Validate connector paths before submitting changes.

## Checks

Run:

```bash
python3 scripts/validate_repo.py
```

The validation checks required files and runs the bundled SVG connector linter against the example HTML.
