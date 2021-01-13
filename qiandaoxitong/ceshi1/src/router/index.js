import Vue from 'vue'
import VueRouter from 'vue-router'
import khgl from '@/components/khgl'
import home from '@/components/home'
import zjmd from '@/components/zjmd'
Vue.use(VueRouter);

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
     redirect: 'khgl',  //重定向：当路由为 / 界面时 跳转 到 Home 界面
    },
    {
      path: '/khgl',
      name: 'khgl',
      component: khgl
    },
    {
      path: '/home',
      name: 'home',
      component: home
    },
    {
      path: '/zjmd',
      name: 'zjmd',
      component: zjmd
    }
    ]
});


export default router