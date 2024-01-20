# General
variable "project" {
  description = "Project"
  default     = "gifted-antonym-411815"
}

variable "credentials" {
  default = "./.keys/gcp.json"
}

variable "location" {
  description = "Project location"
  default = {
    location = "EU"
    region   = "europe-west4-a"
  }
}

# Storage
variable "gcs_bucket_name" {
  description = "Bucket Storage name"
  default     = "bucket-ny-taxi"
}
variable "gcs_class" {
  description = "Bucket storage class"
  default     = "STANDART"
}

# Big Querry
variable "bq_dataset_name" {
  description = "My BigQuerry dataset name"
  default     = "bq_dataset_ny_taxi"
}
