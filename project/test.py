""" Dummy Python Test """
import argparse


def main():
    """ Main """
    parser = argparse.ArgumentParser()
    parser.add_argument("--host",
                        type=str,
                        default="localhost",
                        help="Test server host.")
    parser.add_argument("--port",
                        type=int,
                        default=7077,
                        help="Test server port.")
    parser.add_argument("--username",
                        type=str,
                        default="admin",
                        help="Test server username.")
    parser.add_argument("--password",
                        type=str,
                        default="admin#SNET",
                        help="Test server password.")
    parser.add_argument("--cert",
                        type=str,
                        default="",
                        help="Path to certfile.")
    parser.add_argument("--certkey",
                        type=str,
                        default="",
                        help="Path to cert key.")
    args = parser.parse_args()
    print("ARGS:", args)


if __name__ == "__main__":
    main()
