# Basic tests for the minimal parser

from src import parser


def test_parse_simple_command():
    out = parser.parse_command('ls -lah /home')
    assert isinstance(out, dict)
    assert 'pipeline' in out
    assert len(out['pipeline']) == 1
    p = out['pipeline'][0]
    assert p['name'] == 'ls'
    assert '-lah' in p['args'] or '-l' in p['args']
