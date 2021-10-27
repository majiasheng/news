from news.news import fetch_and_save_all_headlines
from dotenv import load_dotenv

load_dotenv()


def main():
    fetch_and_save_all_headlines()


if __name__ == '__main__':
    main()
