resource "github_membership" "member" {
  for_each = toset(var.members)

  username = each.value
  role     = "member"  // or "admin"
}

resource "github_team" "team" {
  for_each = { for t in var.teams : t.name => t }

  name        = each.key
  description = "Team ${each.key}"
  privacy     = "closed"  // or "secret"
}

resource "github_team_membership" "team_member" {
  for_each = { for team in var.teams : team.name => team.members }

  team_id  = github_team.team[each.key].id
  username = each.value

  role = contains(each.key, "maintainers") || contains(each.key, "technical-committee") || contains(each.key, "governance-committee") ? "maintainer" : "member"
}
