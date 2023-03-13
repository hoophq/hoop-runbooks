#!/bin/bash -e

: '
{{ .namespace | required "namespace is required" | type "select" | options "dev" "prod" | asenv "NAMESPACE" }}
{{ .deploy_name | required "deploy name is required" | type "text" | asenv "DEPLOYMENT" }}
'
exec kubectl --namespace $NAMESPACE rollout restart deploy/$DEPLOYMENT
