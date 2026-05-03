# cmd-explainer 🔍

An interactive shell-based utility that deconstructs complex Linux/Unix command-line strings to explain exactly what each part does.

## Overview

`cmd-explainer` breaks down intimidating command-line strings into digestible explanations. It uses:

- **bashlex**: Python-based parser to generate Abstract Syntax Trees (AST)
- **Man Page Database**: ~30,000 parsed man pages (primarily Ubuntu)
- **Natural Language Processing**: NLTK-based heuristic extraction for relevant documentation
- **Interactive Visualization**: Markdown-rendered explanations with connecting lines

## Features

✨ **Command Parsing**: Distinguishes commands, flags, arguments, pipes, redirections
📚 **Man Page Mapping**: References extensive documentation database
🔍 **Heuristic Extraction**: Isolates relevant paragraphs for specific flags/options
📊 **Interactive Visualization**: Visual Markdown representation of command structure
🎯 **Educational**: Perfect for learning complex command syntax
💾 **Export**: Save explanations to file for reference

## Installation

### Prerequisites

- Python 3.8+
- pip

### Quick Start

```bash
git clone https://github.com/nibblesmcfluff/cmd-explainer.git
cd cmd-explainer
pip install -r requirements.txt
python cmd_explainer.py
```

## Usage

### Interactive Mode

```bash
$ python cmd_explainer.py
cmd-explainer> grep -r "pattern" /path/to/files | head -20
```

### Single Command Mode

```bash
python cmd_explainer.py "ls -lah /home"
```

### Example Output

```
COMMAND STRUCTURE:
├── ls
│   ├── -l (long format listing)
│   ├── -a (show hidden files)
│   └── -h (human-readable sizes)
└── /home (target directory)

DETAILED EXPLANATION:
• ls: List directory contents
• -l: Display in long format (permissions, owner, size, date)
• -a: Include entries starting with . (hidden files)
• -h: Print human-readable file sizes (K, M, G)
• /home: Operate on /home directory
```

## Project Structure

```
cmd-explainer/
├── README.md
├── requirements.txt
├── cmd_explainer.py          # Main entry point
├── src/
│   ├── __init__.py
│   ├── parser.py             # bashlex integration
│   ├── man_db.py             # Man page database
│   ├── extractor.py          # NLP-based extraction
│   ├── visualizer.py         # Markdown visualization
│   └── shell.py              # Interactive shell
├── data/
│   ├── man_pages.db          # SQLite database (optional)
│   └── man_pages_index.json  # Man page index
├── tests/
│   ├── test_parser.py
│   ├── test_extractor.py
│   └── test_man_db.py
└── docs/
    ├── architecture.md
    ├── contributing.md
    └── examples.md
```

## Core Components

### 1. **Parser** (`src/parser.py`)
Uses bashlex to parse command strings into AST, extracting:
- Command name
- Flags and options
- Arguments
- Operators (pipes, redirections)

### 2. **Man Page Database** (`src/man_db.py`)
- Loads pre-parsed man pages
- Provides lookup for commands and flags
- Caches frequently used entries
- Falls back to online API if needed

### 3. **Extractor** (`src/extractor.py`)
- Uses NLTK for natural language processing
- Identifies relevant paragraphs
- Extracts option descriptions
- Ranks results by relevance

### 4. **Visualizer** (`src/visualizer.py`)
- Generates ASCII tree structure
- Creates Markdown explanations
- Links parsed components to documentation
- Supports colored output

### 5. **Interactive Shell** (`src/shell.py`)
- REPL-style interface
- Command history
- Autocomplete support
- Export functionality

## Examples

See `docs/examples.md` for detailed walkthroughs of:
- Basic commands (`ls`, `grep`, `find`)
- Complex pipelines (`grep | awk | sort`)
- Redirection and file operations
- Advanced options and flags

## Data Directory

The `data/` directory contains:
- Man page database (SQLite or JSON)
- Index files for quick lookups
- Scripts for building/updating the database

## Contributing

See `docs/contributing.md` for guidelines on:
- Adding new man pages
- Improving parsing logic
- Enhancing visualizations

## License

MIT License - See LICENSE file for details

## Roadmap

- [ ] Web interface for cmd-explainer
- [ ] Real-time man page synchronization
- [ ] Custom command aliases
- [ ] Integration with shell history
- [ ] Multi-language support
- [ ] Community man page contributions

## Support

Found a bug? Have a feature request? Open an issue or submit a pull request!

---

**Made with ❤️ for Linux/Unix learners**
