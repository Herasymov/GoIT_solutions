news = []

def add_news():
    global news
    title = input("title: ")
    body = input("body: ")
    news.append({'title': title, 'body': body})

def read_news():
    global news
    print(news)


def work():
    for i in range(3):
        add_news()
    read_news()

work()