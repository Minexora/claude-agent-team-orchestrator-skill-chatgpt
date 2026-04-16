from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    root / 'SKILL.md',
    root / 'agents' / 'openai.yaml',
    root / 'references' / 'workflow.md',
    root / 'references' / 'role-rules.md',
    root / 'references' / 'panel-setup.md',
    root / 'references' / 'repo-onboarding.md',
    root / 'references' / 'docs-templates.md',
    root / 'references' / 'output-format.md',
    root / 'references' / 'sample-prompts.md',
    root / 'README.md',
]
missing = [str(p.relative_to(root)) for p in required if not p.exists()]
if missing:
    print('Missing files:')
    for m in missing:
        print('-', m)
    sys.exit(1)
skill = (root / 'SKILL.md').read_text(encoding='utf-8')
if not skill.startswith('---\nname: claude-agent-team-orchestrator\ndescription:'):
    print('Frontmatter check failed')
    sys.exit(1)
print('Local validation OK')
