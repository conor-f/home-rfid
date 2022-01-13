import argparse
from ..rfid.listener import RFIDListener


def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    listener = RFIDListener()
    listener.listen()


if __name__ == '__main__':
    main()
