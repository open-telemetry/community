resource "github_team" "members" {
  name        = var.name
  description = "Team ${var.name}"
  privacy     = var.privacy  // or "secret"
}

resource "github_team_membership" "sig_member" {
  for_each = toset(var.members)
  team_id  = github_team.working_group.id
  username = each.value

  role = "maintainer"
}
