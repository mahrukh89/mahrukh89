#!/usr/bin/env python3
"""Fetch basic public GitHub profile statistics for the profile automation."""

import json
import os
import urllib.request

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", "mahrukh89")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")


def github_api(path: str):
    headers = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    request = urllib.request.Request(
        f"https://api.github.com{path}",
        headers=headers,
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def get_profile():
    """Return the public profile object."""
    return github_api(f"/users/{GITHUB_USERNAME}")


def get_repositories():
    """Return all public repositories owned by the profile."""
    repositories = []
    page = 1

    while True:
        batch = github_api(
            f"/users/{GITHUB_USERNAME}/repos"
            f"?per_page=100&page={page}&type=owner"
        )
        repositories.extend(batch)

        if len(batch) < 100:
            break

        page += 1

    return repositories


if __name__ == "__main__":
    profile = get_profile()
    repositories = get_repositories()

    print(f"GitHub profile: {profile.get('login', GITHUB_USERNAME)}")
    print(f"Public repositories: {profile.get('public_repos', len(repositories))}")
    print(f"Repositories fetched: {len(repositories)}")
