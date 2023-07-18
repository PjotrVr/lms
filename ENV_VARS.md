# Environment Variables Guide

This guide provides descriptions of the environment variables used in this project.
These variables are loaded from `.env` files for different environments: .env.prod (production) and .env.dev (development and testing)

| Environment Variable | Description |
| ------------------- | ----------- |
| `LMS_DB_PATH` | The path to the database file. This is typically something like "library.db". |
| `LMS_SMTP_SERVER` | The SMTP server used to send emails. For example, "smtp.gmail.com". |
| `LMS_SMTP_PORT` | The port used by the SMTP server. For Gmail, this is typically 465. |
| `LMS_EMAIL` (prod) / `LMS_SENDER_EMAIL` (dev, test) | The email address used as the sender for outgoing emails. |
| `LMS_EMAIL_PASSWORD` (prod) / `LMS_SENDER_EMAIL_PASSWORD` (dev, test) | The password for the sender email address. |
| `LMS_RECEIVER_EMAIL` (only dev, test) | The email address used as the receiver for incoming emails during testing. |
| `LMS_RECEIVER_EMAIL_PASSWORD` (only dev, test) | The password for the receiver email address during testing. |
| `LMS_PEPPER` | A secret key used for additional security in password hashing. |