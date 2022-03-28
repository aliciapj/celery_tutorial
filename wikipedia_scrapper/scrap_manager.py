import logging
import wikipediaapi
from wikipedia_scrapper.models import Article

logger = logging.getLogger(__name__)


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
    else:
        print(f'Page {article_title} does not exist')
