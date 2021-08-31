#! /bin/bash

gcloud pubsub topics create jobs
gcloud pubsub subscriptions create worker-tasks --topic jobs

gcloud functions deploy Jobs --runtime go111 --trigger-http