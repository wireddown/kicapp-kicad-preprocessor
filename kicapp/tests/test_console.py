from click.testing import CliRunner
from kicapp import console

def test_console():
  runner = CliRunner()
  result = runner.invoke(console.cli)
  assert result.exit_code == 0
  assert "Show this message and exit." in result.output
