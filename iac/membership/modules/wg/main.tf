resource "github_team" "maintainers" {
  name        = var.name
  description = "Team ${var.name}"
  privacy     = var.privacy  // or "secret"
}

resource "github_team_membership" "sig_maintainer" {
  for_each = toset(var.maintainers)
  team_id  = github_team.maintainers.id
  username = each.value

  role = "maintainer"
}
