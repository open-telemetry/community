output "triagers_id" {
  value = try(github_team.triagers[0].id, null)
}
output "approvers_id" {
  value = try(github_team.approvers[0].id, null)
}
output "maintainers_id" {
  value = github_team.maintainers.id
}