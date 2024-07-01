variable "username" {
  type = string
  description = "The github username for this member"
}

variable "role" {
  type = string
  description = "The role for the member"
  default = "member"
}