from worker_scrapper.celery_worker import worker_scrapper
import wikipediaapi
from wikipedia_scrapper.models import Article

@worker_scrapper.task()
def scrap_article(article_title: str):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    wiki_page = wiki_wiki.page(article_title)

    if wiki_page.exists():
        Article.objects.create(
            fullurl=wiki_page.fullurl,
            title=wiki_page.title,
            summary=wiki_page.summary,
            full_text=wiki_page.text,
        )
        print(f'Downloaded {article_title}')
    else:
        print(f'Page {article_title} does not exist')
