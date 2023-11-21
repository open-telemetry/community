variable "name" {
  type = string
  description = "The name of the SIG"
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

variable "triagers" {
  type = list
  description = "The list of triagers for this SIG"
}

variable "approvers" {
  type = list
  description = "The list of approvers for this SIG"
}

variable "maintainers" {
  type = list
  description = "The list of maintainers for this SIG"
}
