workflow "Check code" {
  on = "push"
  resolves = [ "Run Bandit", "Run Black", "Run Mypy"]
}

action "Run Bandit" {
  uses = "nymous/actions/python-tools@master"
  args = "bandit -r ."
}

action "Run Black" {
  uses = "nymous/actions/python-tools@master"
  args = "black . --check"
}

action "Run Mypy" {
  uses = "nymous/actions/python-tools@master"
  args = "mypy bookmarks_collection"
}
