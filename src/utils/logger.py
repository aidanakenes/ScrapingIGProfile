import logging


def get_logger(name: str):
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s: %(name)s %(message)s %(asctime)s',
        datefmt='%Y-%m-%dT%H:%M'
    )

    return logging.getLogger(name)
