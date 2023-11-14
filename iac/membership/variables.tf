variable "members" {
    type = list(string)
    description = "A list of organization members"
}

variable "teams" {
    type = list(object({
        name    = string
        members = list(string)
    }))
    description = "A list of organization teams and their members"
}