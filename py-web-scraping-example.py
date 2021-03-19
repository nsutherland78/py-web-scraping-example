from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
from urllib.request import urlopen


def get_website_data():
    try:
        html = urlopen("https://www.python.org/")
    except HTTPError as e:
        print(e)
    except URLError:
        print("Server down or incorrect domain")
    else:
        webdata = BeautifulSoup(html.read(),"html5lib");
        return webdata


def get_website_title(webdata):

        if webdata.title is None:
            print("Tag not found")
        else:
            # getText() removes the tags from the output
            print(f"Title: {webdata.title.getText()}")


def get_all_h2_class(webdata):
    tags = webdata.findAll("h2", {"class": "widget-title"})
    print("Printing Tags: ")
    for tag in tags:
        # getText() removes the tags from the output
        print(tag.getText())


def get_tags_examples(webdata):
    # This code gets all span, anchor, and image tags from the scraped HTML
    tags = webdata.findAll("span", "a" "img")
    for tag in tags:
        # getText() removes the tags from the output
        print(tag.getText())

    # This code extracts all anchor tags that have "readmorebtn" and "url" class.
    tags = webdata.findAll("a", {"class": ["url", "readmorebtn"]})
    for tag in tags:
        # getText() removes the tags from the output
        print(tag.getText())

    # You can filter the content based on the inner text itself using the text argument like this:
    tags = webdata.findAll(text="Python Programming Basics with Examples")
    for tag in tags:
        # getText() removes the tags from the output
        print(tag.getText())


def main():
    webdata = get_website_data()
    get_website_title(webdata)
    get_all_h2_class(webdata)
    get_tags_examples(webdata)


if __name__ == '__main__':
    main()