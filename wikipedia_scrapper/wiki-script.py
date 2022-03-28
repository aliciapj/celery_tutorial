

import wikipediaapi
from tqdm import tqdm
import os
import django


def setup_script():
    # django config
    parent_dir = \
        os.path.dirname(  # celery_tutorial
            os.path.dirname(  # wikipedia_scrapper
                    os.path.abspath(__file__)
                ))
    os.sys.path.insert(0, parent_dir)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
    django.setup()

if __name__ == '__main__':

    setup_script()

    from wikipedia_scrapper.scrap_manager import scrap_article
    from wikipedia_scrapper.models import Article

    wiki_wiki = wikipediaapi.Wikipedia('en')
    category_page = wiki_wiki.page('Category:Women_computer_scientists')

    page_titles = []
    for c in tqdm(category_page.categorymembers.values(), desc='Extracting urls'):
        # skipping sub-categories
        if not c.title.startswith('Category:'):
            scrap_article(c.title)

    print(Article.objects.count())
    print(', '.join([a.title for a in Article.objects.all()]))