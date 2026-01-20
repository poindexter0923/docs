#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADD_ONE = ROOT / 'scripts' / 'add-doc.py'


def die(msg: str) -> None:
    print(f'error: {msg}', file=sys.stderr)
    sys.exit(1)


def main() -> None:
    if len(sys.argv) != 2:
        die('usage: scripts/add-docs-batch.py path/to/dir')

    target = Path(sys.argv[1])
    if not target.is_absolute():
        target = (ROOT / target).resolve()

    if not target.exists() or not target.is_dir():
        die('please provide an existing directory')

    # Process markdown files recursively
    md_files = sorted(target.rglob('*.md'))
    if not md_files:
        print('no markdown files found')
        return

    # Invoke add-doc.py for each file
    for md in md_files:
        rc = __import__('subprocess').run([sys.executable, str(ADD_ONE), str(md)], check=False)
        if rc.returncode != 0:
            die(f'failed processing {md}')

    print(f'processed {len(md_files)} file(s)')


if __name__ == '__main__':
    main()
