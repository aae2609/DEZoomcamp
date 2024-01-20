terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.12.0"
    }
  }
}

provider "google" {
  project     = "gifted-antonym-411815"
  region      = "europe-west4-a"
  credentials = "./.keys/gcp.json"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "ny-taxi-demo-bucket"
  location      = "EU"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1 # in days
    }
    action {
      type = "Delete"
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}


resource "google_bigquery_dataset" "demo-dataset" {
  dataset_id = "ny-taxi-demo-dataset"
  location   = "EU"
}
