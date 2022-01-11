import subprocess

import yaml

with open("config.yml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)
    activeFolder = cfg["production"]["activeFolder"]


def splitter(repeat: int = 80):
    print("-" * repeat)


def cleanpy():
    subprocess.run(["cleanpy", "./"])
    print("cleanpy: Done.")
    splitter()


def autoflake():
    subprocess.run(
        [
            "autoflake",
            "--in-place",
            "--remove-all-unused-imports",
            "--remove-duplicate-keys",
            "--remove-unused-variables",
            activeFolder,
            "--recursive",
        ]
    )
    print("autoflake: Done.")
    splitter()


def requirement():
    subprocess.run(["pipreqs", activeFolder, "--force"])
    splitter()


def mypy():
    subprocess.run(["mypy", activeFolder])
    splitter()


def isort():
    subprocess.run(
        ["isort", activeFolder], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
    )
    print("isort: Done.")
    splitter()


def black():
    subprocess.run(
        ["black", activeFolder], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
    )
    print("black: Done.")
    splitter()


def main():
    black()
    autoflake()
    isort()
    mypy()
    requirement()
    cleanpy()


if __name__ == "__main__":
    main()
