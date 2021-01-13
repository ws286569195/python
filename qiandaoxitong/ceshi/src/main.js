import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from "axios"
import store from './store'
import Vuex from 'vuex'
Vue.prototype.$axios = axios;
Vue.config.productionTip = false
/* eslint-disable no-new */
Vue.use(ElementUI)
Vue.use(Vuex);
axios.defaults.baseURL = 'http://127.0.0.1:5000'
axios.defaults.auth = {
  username: '',
  password: '',
}
axios.interceptors.request.use(
  config => {
    if (localStorage.getItem('Authorization')) {
      config.headers.authorization ="Bearer " +  localStorage.getItem('Authorization');
      // alert(localStorage.getItem('Authorization'));
    }

    return config;
  },
  error => {
    return Promise.reject(error);
  });
axios.interceptors.response.use(function (response) {
  // 对响应数据做点什么
  if(response.status === 200){ //成功状态码200
      return response;    //返回响应的数据
  }else{
      return  Promise.reject(response)  
  }
}, function (error) {
  // 对响应错误做点什么
  if(error.response.status){
    switch(error.response.status){
      //用户名密码错误
      case 400:
          router.replace({
            path:'/login',
            query:{redirect:router.currentRoute.fullPath}
          })
          console.log("账号密码错误！");
      //未登录,跳转到登录页并携带当前页路径，登录成功后跳转
      case 401:
          alert("登录过期！")
          router.replace({
            path:'/login',
            query:{redirect:router.currentRoute.fullPath}
          })
      //token过期，对用户提示然后清除本地token再跳转
      case 403:
          Toast({
            message:'登陆过期',
            duration:1000,
          })
          localStorage.removeItem('token')
          store.commit('token')
          setTimeout(() => {
              router.replace({
                path:'/login',
                query:{redirect:router.currentRoute.fullPath}
              })
          },1000)
      //请求不存在		
      case 404:
          Toast({
            message:'请求不存在',
            duration:1000,
          })
      case 422:
            router.replace({
              path:'/login',
              query:{redirect:router.currentRoute.fullPath}
            })
        //token过期，对用户提示然后清除本地token再跳转
      break
      
      //其他错误，提示错误
      default:
          Toast({
            message:error.response.data.message,
            duration:1000,
          })
    }
  }
  return Promise.reject(error);
});
new Vue({
  el: '#app',
  router,
  store: store,
  components: { App },
  template: '<App/>'
})
