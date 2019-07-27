workflow "Check code" {
  on = "push"
  resolves = [ "Run Bandit", "Run Black", "Run Mypy"]
}

action "Install dependencies" {
  uses = "nymous/actions/python-tools@master"
  args = "poetry install"
}

action "Run Bandit" {
  uses = "nymous/actions/python-tools@master"
  needs = [ "Install dependencies" ]
  args = "bandit -r ."
}

action "Run Black" {
  uses = "nymous/actions/python-tools@master"
  needs = [ "Install dependencies" ]
  args = "black . --check"
}

action "Run Mypy" {
  uses = "nymous/actions/python-tools@master"
  needs = [ "Install dependencies" ]
  args = "mypy bookmarks_collection"
}
