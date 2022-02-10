from server import db
from model import Build
import time


def save_json_to_build(data):
    """
    Takes in JSON data for a push github request and saves data regarding the
    repository name, owner, url, timestamp, pusher and branch to the
    SQLite database.
    """
    try:
        repository = data["repository"]
        repo_name = repository["name"]
        owner = repository["owner"]["name"]
        url = repository["owner"]["url"]
        timestamp = int(time.time())
        pusher = data["pusher"]["name"]
        branch = data["ref"].split("/")[-1]
        new_build = Build(
            owner=owner,
            timestamp=timestamp,
            pusher=pusher,
            branch=branch,
            repo_name=repo_name,
            repo_url=url,
        )
        db.session.add(new_build)
        db.session.commit()
        return new_build
    except:
        raise Exception("JSON data could not be parsed")


def update_build_with_syntax_check(build, syntax_result):
    """
    Takes in a previous build saved to the database and edits the
    the "syntax result" to indicate whether a build was successful or not
    """
    record_found = Build.query.filter_by(
        pusher=build.pusher, timestamp=build.timestamp
    ).first()
    record_found.syntax_result = syntax_result
    db.session.commit()


def get_all_builds():
    "Queries all builds in the database"
    return Build.query.all()
