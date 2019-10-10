""" Dummy Python Script """
import os
import time
import argparse


def main():
    """ Main """
    parser = argparse.ArgumentParser()
    parser.add_argument("--host",
                        type=str,
                        default=os.environ.get("TEST_HOST", "localhost"),
                        help="Test server host.")
    parser.add_argument("--port",
                        type=int,
                        default=os.environ.get("TEST_PORT", 7777),
                        help="Test server port.")
    parser.add_argument("--username",
                        type=str,
                        default=os.environ.get("TEST_USER", "admin"),
                        help="Test server username.")
    parser.add_argument("--password",
                        type=str,
                        default=os.environ.get("TEST_PASS", "admin#PASS"),
                        help="Test server password.")
    parser.add_argument("--cert",
                        type=str,
                        default=os.environ.get("TEST_CERT", ""),
                        help="Path to certfile.")
    parser.add_argument("--certkey",
                        type=str,
                        default=os.environ.get("TEST_CERTKEY", ""),
                        help="Path to cert key.")
    args = parser.parse_args()
    print("ARGS:", args)
    print("Waiting forever...")
    while True:
        time.sleep(100)


if __name__ == "__main__":
    main()
    exit(0)
