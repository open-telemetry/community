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
  for_each = local.team_member_combinations

  team_id  = github_team.team[each.value.team_name].id
  username = each.value.member_name

  role = can(regex(".*(maintainers|technical-committee|governance-committee).*", each.value.team_name)) ? "maintainer" : "member"
}
