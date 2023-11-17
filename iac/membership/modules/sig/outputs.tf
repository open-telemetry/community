output "triagers_id" {
  value = length(var.triagers) > 0 ? github_team.triagers[0].id : null
}
output "approvers_id" {
  value = length(var.approvers) > 0 ? github_team.approvers[0].id : null
}
output "maintainers_id" {
  value = github_team.maintainers.id
}