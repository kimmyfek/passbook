import axios from 'axios'

var Base = axios.create({
  baseURL: 'http://localhost:7777/api' // TODO - make this some sort of config var
})

export const BusAPI = {
  getBusinesses () {
    return Base
      .get('/business')
      .catch(e => {
        console.log(e) // TODO handle this error
        this.errors = e
      })
  }
}
