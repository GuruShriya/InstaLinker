"""Terminal UI entry point for Insta Linker."""

from textual.app import App, ComposeResult
from textual.widgets import Static


class InstaLinkerApp(App):
    """Minimal welcome screen for the first TUI ticket."""

    CSS_PATH = "insta_linker.tcss"

    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Static("Welcome to InstaLinker\n\nHello World", id="welcome")


if __name__ == "__main__":
    InstaLinkerApp().run()
