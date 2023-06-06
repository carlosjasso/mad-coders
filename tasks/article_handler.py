import subprocess
from argparse import Namespace
from datetime import datetime, timezone
from os import path

import conf
from tasks import helpers
from tasks.types import Article, ArticleUtilsProps, CreateArticleProps


def createArticle(namespace: Namespace) -> None:
    props = helpers.getProps(namespace, CreateArticleProps)
    article = __initArticle(props.title, props.status)
    __writeFrontMatter(article)
    subprocess.run(f"code {article.path} --reuse-window", shell=True)


def processUtils(namespace: Namespace) -> None:
    props = helpers.getProps(namespace, ArticleUtilsProps)

    if props.isTimestamp:
        __printTimestamp()


def __initArticle(title: str, status: str) -> Article:
    utcTime = __getUtcTime()
    timestamp = __getIsoTimestamp(utcTime)
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


def __printTimestamp() -> None:
    utcTime = __getUtcTime()
    timestamp = __getIsoTimestamp(utcTime)
    print(f"\t{timestamp}\n")


def __getUtcTime() -> datetime:
    return datetime.now(tz=timezone.utc)


def __getIsoTimestamp(time: datetime) -> str:
    return time.isoformat(timespec="seconds")


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
