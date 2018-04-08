# passbook

> A Vue.js && Python 3.6 project

## Init Virtualenv

`virtualenv -p python3.6 .env'

## Running API
`source .env/bin/activate && pip install -r requirements.txt`

Then just `python lib/main.py`

## Setting up MySQL with Docker
docker run --name passbook_db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -d mysql:latest

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

### UI TODO
- [x] Businesses comp
- [ ] Business comp
- [ ] Hours comp
- [ ] Coupons
- [ ] Locations
- [ ] Add new data types
- [ ] What to do when two locations are in the same neighborhood
- [ ] Add restaurant type to database + api
- [ ] Need to appropriately handle errors on the ajax calls
- [ ] Looks nice on mobile
- [ ] Size down coupon text if too long -- Coupons can get absurdly sized.
- [ ] If only one coupon, it needs to fill
- [ ] Put stars in rating
- [ ] Pull all query params from websites
- [ ] What to do about permanently closed
- [ ] Some tests
- [ ] Switch between locations
- [ ] Locations: Lodo are LJ'd weird

## Long Term ToDo
- [ ] Users
- [ ] Opentable
- [ ] Integrate eBates
