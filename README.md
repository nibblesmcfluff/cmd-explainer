# cmd-explainer 🔍

An interactive shell-based utility that deconstructs complex Linux/Unix command-line strings to explain exactly what each part does.

## Features

- **Command Parsing**: Uses `bashlex` to break command strings into an Abstract Syntax Tree (AST)
- **Man Page Mapping**: References a database of ~30,000 parsed man pages (primarily from Ubuntu)
- **Heuristic Extraction**: Uses Python NLP (NLTK) to isolate relevant documentation paragraphs
- **Interactive Visualization**: Renders Markdown with connecting lines between command parts and their explanations
- **REPL Interface**: Interactive shell for continuous command analysis
- **Colored Output**: Easy-to-read terminal output with syntax highlighting
- **Export Capability**: Save explanations to file for documentation

## Installation

### Requirements
- Python 3.8+
- pip

### Setup

```bash
git clone https://github.com/nibblesmcfluff/cmd-explainer.git
cd cmd-explainer
pip install -r requirements.txt
```

### Download Man Pages Database (Optional)

For the full 30,000 man pages experience:

```bash
python scripts/download_man_pages.py
```

This will download and parse man pages from Ubuntu man-pages archives.

## Usage

### Interactive Shell

```bash
python cmd_explainer/main.py
```

Then type commands to analyze:

```
> ls -lah /tmp
> grep -r "pattern" --include="*.py" .
> find . -name "*.txt" -exec cat {} \;
> ps aux | grep python | awk '{print $2}'
```

### Command Line

```bash
python cmd_explainer/main.py "ls -lah /tmp"
```

### Programmatic Usage

```python
from cmd_explainer import CommandExplainer

explainer = CommandExplainer()
result = explainer.explain("grep -r 'pattern' --include='*.py' .")
print(result)
```

## Project Structure

```
cmd-explainer/
├── cmd_explainer/
│   ├── __init__.py
│   ├── main.py                 # Interactive shell entry point
│   ├── parser.py              # AST parsing with bashlex
│   ├── analyzer.py            # Command component analysis
│   ├── man_page_db.py         # Man page database interface
│   ├── nlp_processor.py       # NLTK-based text processing
│   ├── visualizer.py          # Markdown visualization
│   └── utils.py               # Utility functions
├── scripts/
│   ├── download_man_pages.py  # Man page database downloader
│   └── parse_man_pages.py     # Man page parser and indexer
├── data/
│   ├── man_pages.db           # SQLite database (generated)
│   └── man_pages_index.json   # Man pages index (generated)
├── tests/
│   ├── test_parser.py
│   ├── test_analyzer.py
│   └── test_visualizer.py
├── requirements.txt
├── setup.py
└── README.md
```

## Example Output

```
Command: ls -lah /tmp

┌─────────────────────────────────────────────────────────────┐
│ COMMAND BREAKDOWN                                           │
└─────────────────────────────────────────────────────────────┘

  ls ──────┬─────────────────────────────────────────────────
           │
           └─→ List directory contents
                 From: man ls (1)
                 "List information about the FILEs (the current
                  directory by default)."

  -l ──────┬─────────────────────────────────────────────────
           │
           └─→ use a long listing format
                 "use a long listing format"

  -a ──────┬─────────────────────────────────────────────────
           │
           └─→ do not ignore entries starting with .
                 "do not ignore entries starting with ."

  -h ──────┬─────────────────────────────────────────────────
           │
           └─→ print sizes in human readable format
                 "print sizes in human readable format (e.g., 1K
                  234M 2G)"

  /tmp ────┬─────────────────────────────────────────────────
           │
           └─→ Directory argument
                 Path to list contents of
```

## Development

### Running Tests

```bash
pytest tests/
```

### Building Documentation

```bash
python scripts/generate_docs.py
```

## Architecture

### 1. Command Parsing (`parser.py`)
- Uses `bashlex` to generate AST from command strings
- Extracts command, subcommands, flags, arguments, pipes, redirections
- Handles complex shell syntax (globbing, quoting, variable expansion context)

### 2. Analysis (`analyzer.py`)
- Maps AST nodes to semantic components
- Categorizes: command, options/flags, arguments, redirections, pipes
- Tracks flag values and their arguments

### 3. Man Page Database (`man_page_db.py`)
- SQLite backend for efficient querying
- Indexed by command name and flag
- Caches frequently accessed pages

### 4. NLP Processing (`nlp_processor.py`)
- Uses NLTK for text tokenization and processing
- Extracts relevant paragraphs for flags/options
- Implements TF-IDF scoring for relevance ranking

### 5. Visualization (`visualizer.py`)
- Renders Markdown with ASCII art connections
- Syntax highlighting with color codes
- Responsive terminal formatting

## Data Sources

- **Ubuntu Man Pages**: https://manpages.ubuntu.com/
- **Linux Man-Pages Project**: https://www.kernel.org/doc/man-pages/
- **GNU Coreutils**: https://www.gnu.org/software/coreutils/

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

MIT License - see LICENSE file for details

## Roadmap

- [ ] Full 30,000 man page database integration
- [ ] Machine learning for better flag detection
- [ ] Shell integration (bash/zsh completion)
- [ ] Web-based interface
- [ ] Multi-language man page support
- [ ] Real-time command validation
- [ ] Integration with Stack Overflow for examples
- [ ] Docker containerization

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Made with ❤️ by nibblesmcfluff**
