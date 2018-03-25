# passbook

> A Vue.js project

## Running API / Installing Virtualenv

`virtualenv -p python3.6 .env && source .env/bin/activate && pip install -r requirements.txt`
Then just `python lib/main.py`

## UI Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).


docker run --name passbook_db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -d mysql:latest

### UI TODO
- [x] Businesses comp
- [ ] Business comp
- [ ] Hours comp
- [ ] Coupons
- [ ] Locations
- [ ] Add new data types
- [ ] Opentable
