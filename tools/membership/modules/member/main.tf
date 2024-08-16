resource "github_membership" "member" {
  username = var.username
  role     = var.role
}
