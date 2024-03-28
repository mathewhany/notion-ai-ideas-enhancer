import csv

import click
from .config import idea_processor


@click.command()
@click.argument("idea", required=False)
@click.option("--path", "-p", type=click.Path(exists=True))
@click.option("--starting-index", "-i", type=int, default=0)
def cli(idea, path, starting_index):
    if idea:
        process_idea(idea)

    elif path:
        ideas = []

        with open(path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                ideas.append(row[0])

        for i, idea in enumerate(ideas[starting_index:], starting_index):
            if not process_idea(idea, i):
                break
    else:
        print("No idea provided!")


def process_idea(idea, index: int | None = None):
    try:
        idea_processor.process(idea)
        print(f"{idea} added to the database!")
        return True

    except Exception as e:
        print(f"Failed to process idea: {e}")
        if index:
            print(f"Last executed index: {index}")
        return False


if __name__ == "__main__":
    cli()
