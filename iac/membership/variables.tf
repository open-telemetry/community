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
