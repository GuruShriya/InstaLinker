"""Terminal UI entry point for Insta Linker."""

from textual import work
from textual.app import App, ComposeResult
from textual.widgets import DataTable, Static

from fetch_one_link import fetch_video_link


class InstaLinkerApp(App):
    """Minimal welcome screen for the first TUI ticket."""

    CSS_PATH = "insta_linker.tcss"

    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Static("Welcome to InstaLinker", id="welcome") #TODO yeild what exactly here?
        yield Static("Loading one #gym video...", id="status")
        yield DataTable(id="video_table")

    def on_mount(self) -> None:
        table = self.query_one("#video_table", DataTable) #TODO what is #vdeio_table
        table.add_columns("Instagram link")
        self.load_video_link()

    @work(thread=True) #TODO why thread?
    def load_video_link(self) -> None:
        try:
            link = fetch_video_link()
        except Exception as error:
            self.call_from_thread(self.show_error, str(error))
        else:
            self.call_from_thread(self.show_video_link, link)

    def show_video_link(self, link: str) -> None:
        table = self.query_one("#video_table", DataTable)
        table.clear()
        table.add_row(link)
        self.query_one("#status", Static).update("One #gym video found")

    def show_error(self, message: str) -> None:
        table = self.query_one("#video_table", DataTable)
        table.clear()
        table.add_row(message)
        self.query_one("#status", Static).update("Could not fetch a #gym video")


if __name__ == "__main__":
    InstaLinkerApp().run()
