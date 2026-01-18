import click
from pathlib import Path

@click.group()
def main():
    pass

@click.command()
@click.option('-r', '--repo-path', 
              default='.', help='relative path to repository', 
              type = click.Path(exists=True, file_okay=False, dir_okay=True, readable=True, resolve_path=True, path_type=Path))
@click.option('-v', '--verbose', 'verbose', count=True, default=0, help='returns verbose output')
def analyse(repo_path,verbose):
    click.echo(f'Analysing repo at {repo_path}')


main.add_command(analyse)
