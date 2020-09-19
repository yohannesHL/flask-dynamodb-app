- The dynamo db table doesn't exist so had to test with my own dynamodb table to test the API response. Provided there is a dynamodb table, with name defined via `TABLE_NAME` env var (from `.env`), then the `/secret` will return the expected response.

- Had some minor issues when pushing to docker hub via the github actions but its now resolved. Documentation was not clear that why buildx was required so i didn't use it. I learnt the hard way.
