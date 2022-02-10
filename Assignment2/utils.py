from server import db
from model import Build
import time


def save_json_to_build(data):
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
    record_found = Build.query.filter_by(
        pusher=build.pusher, timestamp=build.timestamp
    ).first()
    record_found.syntax_result = syntax_result
    db.session.commit()


def get_all_builds():
    return Build.query.all()
