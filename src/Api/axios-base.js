import axios from 'axios'
import store from '../store'

const APIUrl = 'http://hitecmx.ddns.net:8082/'
// Make Axios play nice with Django CSRF

const axiosBase = axios.create({
  baseURL: APIUrl,

})

axiosBase.defaults.xsrfCookieName = 'csrftoken'
axiosBase.defaults.xsrfHeaderName = 'X-CSRFToken'
const getAPI = axios.create({
  baseURL: APIUrl
})



getAPI.defaults.xsrfCookieName = 'csrftoken'
getAPI.defaults.xsrfHeaderName = 'X-CSRFToken'
getAPI.interceptors.response.use(undefined,

  function (err) {
  // if error response status is 401, it means the request was invalid due to expired access token
  if (err.config && err.response && err.response.status === 401) {
    return store.dispatch('refreshToken') // attempt to obtain new access token by running 'refreshToken' action
      .then(access => {

        console.log(store.state.accessToken)

        err.config.headers['Authorization'] = 'Bearer ' + store.state.accessToken;
        return getAPI.request(err.config);

      })
      .catch(err => {
        return Promise.reject(err)
      })
  }
}
)

getAPI.interceptors.request.use(function(config) {
    const auth_token = localStorage.getItem('access_token');
    if(auth_token) {
      config.headers.Authorization = `Bearer ${auth_token}`;
    }
    return config;
}, function(err) {
    return Promise.reject(err);
});
export {axiosBase, getAPI}
