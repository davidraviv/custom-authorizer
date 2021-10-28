# Custom Authorizer Function
Sample code to demonstrate implementation of custom authorizer function that sends context to the authorized lambda in localstack.

## Usage
Build, start localstack and deploy service:
```
npm install
docker-compose -p custom-function up -d
serverless deploy
```

Call the endpoint:
```
curl --location --request POST 'http://localhost:4566/restapis/<copy id from serverless deploy>/dev/_user_request_/user' \
--header 'Authorization: Allow' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Inigo"
}'
```
