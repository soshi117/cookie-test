"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Cookie Test."""


def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    main(prog_name="cookie-test")  # pragma: no cover
