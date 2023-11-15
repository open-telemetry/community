variable "members" {
  description = "List of GitHub organization members"
  type        = list(string)
}

variable "teams" {
  description = "List of GitHub teams with members"
  type = list(object({
    name    = string
    members = list(string)
    parent  = string
  }))
}

locals {
  team_member_combinations = merge([
    for team in var.teams : {
      for member in team.members : "${team.name}-${member}" => {
        team_name   = team.name
        member_name = member
      }
    }
  ]...) 
}