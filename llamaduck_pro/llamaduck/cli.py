import click
import time
import os
import json
import sys
from typing import Optional, Dict, Any, List
from duckduckgo_search import DDGS
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

console = Console()

# Define the help_me function first so it can be called from the main function
def show_help():
    """Show help information about LlamaDuck commands."""
    console.print("\n[bold yellow]🦙 LlamaDuck Pro[/] - Your friendly terminal search assistant\n")
    
    table = Table(title="Available Commands")
    table.add_column("Command", style="cyan")
    table.add_column("Description", style="green")
    table.add_column("Example", style="yellow")
    
    table.add_row(
        "search",
        "Search the web using DuckDuckGo",
        "llamaduck search \"python best practices\""
    )
    
    table.add_row(
        "chat",
        "Have a conversation with LlamaDuck",
        "llamaduck chat \"Tell me about llamas\""
    )
    
    table.add_row(
        "--help",
        "Show help for a specific command",
        "llamaduck search --help"
    )
    
    table.add_row(
        "--version",
        "Show the installed version",
        "llamaduck --version"
    )
    
    console.print(table)
    
    console.print("\n[bold cyan]Installation Directory:[/]")
    console.print(f"  {os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}")
    
    console.print("\n[bold cyan]Features:[/]")
    features = [
        "🔍 Fast web search using DuckDuckGo's API",
        "💬 Interactive chat capabilities",
        "🌈 Rich terminal UI with beautiful formatting",
        "🚀 Optimized for macOS"
    ]
    
    for feature in features:
        console.print(f"  {feature}")

@click.group(invoke_without_command=True)
@click.version_option(version="0.1.0")
@click.pass_context
def cli(ctx):
    """LlamaDuck Pro: A powerful search and chat CLI tool."""
    if ctx.invoked_subcommand is None:
        show_help()

@cli.command()
@click.argument("query", type=str)
@click.option("--limit", "-l", default=5, help="Number of results to return")
@click.option("--region", "-r", default="wt-wt", help="Region for search results")
def search(query: str, limit: int, region: str):
    """Search the web using DuckDuckGo."""
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold cyan]Searching...[/]"),
        transient=True,
    ) as progress:
        progress.add_task("search", total=None)
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, region=region, max_results=limit))
        except Exception as e:
            console.print(f"[bold red]Error during search: {e}[/]")
            return

    console.print(f"\n[bold]🦙 LlamaDuck Search Results for:[/] [yellow]'{query}'[/]\n")
    
    for i, result in enumerate(results, 1):
        title = result.get("title", "No title")
        body = result.get("body", "No description available")
        href = result.get("href", "No URL available")
        
        console.print(Panel(
            f"[bold cyan]{i}. {title}[/]\n\n"
            f"{body}\n\n"
            f"[link={href}]{href}[/link]",
            expand=False,
            border_style="yellow"
        ))

@cli.command()
@click.argument("query", type=str)
def chat(query: str):
    """Chat with LlamaDuck using DuckDuckGo knowledge."""
    console.print(f"\n[bold yellow]🦙 [/][bold cyan]You:[/] {query}\n")
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold cyan]LlamaDuck is thinking...[/]"),
        transient=True,
    ) as progress:
        progress.add_task("thinking", total=None)
        time.sleep(1)  # Simulate thinking
        
        # Get some information to respond with
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=3))
                answer = f"Based on my search, I found: \n\n"
                
                for result in results:
                    answer += f"- {result.get('body', 'No information found')}\n\n"
                
                answer += f"Is there anything specific about this you'd like to know more about?"
        except Exception as e:
            answer = f"I'm having trouble searching for information about that right now. Can you try asking something else?"
    
    console.print(f"[bold yellow]🦙 [/][bold green]LlamaDuck:[/]\n")
    console.print(Markdown(answer))

@cli.command()
def help_me():
    """Show help information about LlamaDuck commands."""
    show_help()

if __name__ == "__main__":
    cli()
