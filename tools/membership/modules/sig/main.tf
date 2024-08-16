// triagers is only created if there is a list of triagers for this SIG
resource "github_team" "triagers" {
  count       = length(var.triagers) > 0 ? 1 : 0
  name        = "${var.name}-triagers"
  description = "Team ${var.name} Triagers"
  privacy     = var.privacy  // or "secret"
}

resource "github_team_membership" "sig_triager" {
  for_each = toset(var.triagers)
  team_id  = github_team.triagers[0].id
  username = each.value

  role = "member"
}

resource "github_team" "approvers" {
  count       = length(var.approvers) > 0 ? 1 : 0
  name        = "${var.name}-approvers"
  description = "Team ${var.name} Approvers"
  privacy     = var.privacy  // or "secret"

  // set a parent team IFF it exists
  parent_team_id = length(var.triagers) > 0 ? github_team.triagers[0].id : null
}

resource "github_team_membership" "sig_approver" {
  for_each = toset(var.approvers)
  team_id  = github_team.approvers[0].id
  username = each.value

  role = "member"
}

resource "github_team" "maintainers" {
  name        = "${var.name}-maintainers"
  description = "Team ${var.name} Maintainers"
  privacy     = var.privacy  // or "secret"
  parent_team_id = length(var.approvers) > 0 ? github_team.approvers[0].id : null
}

resource "github_team_membership" "sig_maintainer" {
  for_each = toset(var.maintainers)
  team_id  = github_team.maintainers.id
  username = each.value

  role = "maintainer"
}
