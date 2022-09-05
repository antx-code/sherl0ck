import asyncio
from loguru import logger
from maigret.maigret import main
import json
import os
import sys
import typer


app = typer.Typer(help='Social Network Account Hunter')


@logger.catch(level='ERROR')
def json_result(username: str):
    report_path = f'{os.path.dirname(__file__)}/reports'
    filename = f'{report_path}/report_{username}_simple.json'
    with open(filename, 'r', encoding='utf-8') as f:
        result = json.loads(f.read())
        logger.success(json.dumps(result, indent=4))
    return result


@logger.catch(level='ERROR')
@app.command()
def run(targets):
    logger.success('Using Maigret mode to hunter accounts')
    usernames = [targets] if isinstance(targets, str) else targets
    try:
        if sys.version_info.minor >= 10:
            asyncio.run(main(usernames))
        else:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main(usernames))
    except KeyboardInterrupt:
        print('Sherl0ck is interrupted.')
        sys.exit(1)


@logger.catch(level='ERROR')
@app.command()
def dia(targets):
    logger.success('Using Sherl0ck mode to hunter accounts')
    results = []
    usernames = [targets] if isinstance(targets, str) else targets
    asyncio.run(main(usernames))
    for username in usernames:
        results.append(json_result(username))
    return results


if __name__ == '__main__':
    app()
