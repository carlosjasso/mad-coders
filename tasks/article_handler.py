import subprocess
from argparse import Namespace
from datetime import datetime
from os import path

import conf
from tasks import helpers
from tasks.types import Article, CreateArticleProps


def createArticle(namespace: Namespace) -> None:
    props = helpers.getProps(namespace, CreateArticleProps)
    article = __initArticle(props.title, props.status)
    __writeFrontMatter(article)
    subprocess.run(f"code {article.path} --reuse-window", shell=True)


def __initArticle(title: str, status: str) -> Article:
    utcTime = datetime.utcnow()
    timestamp = utcTime.isoformat(timespec="seconds")
    slug = title.replace(' ', '-')
    basename = f"{utcTime.strftime('%Y-%m-%d')}_{slug}.md"

    return Article(
        title=title,
        status=status,
        date=timestamp,
        modified=timestamp,
        tags=None,
        slug=slug,
        author=conf.SITENAME,
        summary=title,
        basename=basename,
        path=path.join(conf.WORKSPACE_PATH, conf.PATH, basename)
    )


def __getFrontMatter(article: Article) -> str:
    return "\n".join([
        "---",
        f"title: {article.title}",
        f"date: {article.date}",
        f"modified: {article.modified}",
        f"tags: {article.tags or 'None'}",
        f"slug: {article.slug}",
        f"author: {article.author}",
        f"summary: {article.summary}",
        f"status: {article.status}",
        "---"
    ]) + ("\n" * 2)


def __writeFrontMatter(article: Article) -> None:
    with open(article.path, mode="x") as file:
        frontmatter = __getFrontMatter(article)
        file.write(frontmatter)
