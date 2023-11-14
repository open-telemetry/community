resource "github_membership" "members" {
    for_each = toset(var.members)
    username = each.key
    role = "member"
}

resource "github_team" "team" {
  for_each = { for t in var.teams : t.name => t }

  name        = each.key
  description = "${each.key}"
}

resource "github_team_membership" "team_member" {
  for_each = { for team in var.teams : team.name => team.members }

  team_id  = github_team.team[each.key].id
  username = each.value

  role = contains(each.key, "maintainers") || each.key == "technical-committee" || each.key == "governance-committee" ? "maintainer" : "member"
}


