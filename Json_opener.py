import click
import json
import logging


def get_value(path, key):
    path = rf'{path}'
    with open(path, "r") as json_file:
        data = json.load(json_file)
    if key == '*':
        return data
    else:
        return data[key]


logging.basicConfig(filename="errors.log", filemode="w",
                    format=u'# %(levelname)s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


@click.command()
@click.argument('path')
@click.argument('key')
def main(path, key):
    try:
        print(get_value(path, key))
    except KeyError:
        print("incorrect input")
        logging.info(f"user's incorrect input: {path} {key}")
    except Exception:
        logging.error(f"very strange behaviour with input: {path} {key}")


if __name__ == "__main__":
    main()
