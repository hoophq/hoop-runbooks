: '
{{ .engine 
    | description "the RDS database engine"
    | type "select"
    | options "mysql" "postgres" 
    | asenv "RDS_ENGINE" }}
{{ .environment
    | description "the name of the environment"
    | type "select"
    | options "prod" "dev"
    | asenv "ENVIRONMENT" }}
{{ .team
    | description "squad name"
    | type "text"
    | asenv "TEAM" }}
{{ .subject
    | description "subject"
    | type "text"
    | asenv "SUBJECT" }}
'

./create-rds.sh
    -e $RDS_ENGINE
    -a $ENVIRONMENT
    -b $SQUAD
    -s $SUBJECT
    -t security_experience
    -n mfa-message-token
    -p secplataform-prod 
    -d mfa_message_token