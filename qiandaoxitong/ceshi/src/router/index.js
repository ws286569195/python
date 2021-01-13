import Vue from 'vue'
import VueRouter from 'vue-router'
import login from '@/components/page/home'
Vue.use(VueRouter);

const router = new VueRouter({
  routes: [
    {
      path: '/',
      redirect: 'home',
      component: home
    },
    ]
});


export default router