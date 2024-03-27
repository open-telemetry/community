variable "name" {
  type = string
  description = "The name of the WG"
}

variable "privacy" {
  type = string
  description = "The privacy of this team"
  default = "closed"
}

variable "repos" {
  type = list
  description = "The list of repos this SIG works on"
  default = []
}

variable "members" {
  type = list
  description = "The list of members for this working group"
}
