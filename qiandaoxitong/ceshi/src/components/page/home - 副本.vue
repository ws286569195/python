<template>
  <div style="background-color: #EBEBEB;min-height:900px">
    <div style="width:100%;background-color: #636363; overflow: hidden;height: 50px;">
      <span
        class="demonstration"
        style="float:left;padding-top:10px;color:white;margin-left:1%"
      >发票管理系统V1.0</span>
      <!-- <span
        class="demonstration"
        style="float:left;padding:5px;color:white;margin-left:2%;width:15%"
      >
        <el-input
          placeholder="请输入"
          icon="search"
          v-model="searchCriteria"
          :on-icon-click="handleIconClick"
        ></el-input>
      </span>-->
      <span class="demonstration" style="float:right;padding-top:10px;margin-right:1%">
        <el-dropdown trigger="click">
          <span class="el-dropdown-link" style="color:white">
            当前登录用户：{{name}}
            <i class="el-icon-caret-bottom el-icon--right"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>个人信息</el-dropdown-item>
            <el-dropdown-item @click.native="exit">退出登录</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </span>
    </div>

    <div style="margin-top:5px">
      <el-row :gutter="10">
        <el-col :xs="4" :sm="4" :md="4" :lg="4">
          <div>
            <el-menu
              default-active="2"
              class="el-menu-vertical-demo"
              @select="handleSelect"
              background-color="#545c64"
              text-color="#fff"
              active-text-color="#ffd04b"
              style="height: 800px;width: 200px;"
              :unique-opened="true"
            >
              <el-submenu index="1">
                <template slot="title">
                  <i class="el-icon-location"></i>
                  <span>单据管理</span>
                </template>
                <el-menu-item-group>
                  <el-menu-item index="1-1">单据读入</el-menu-item>
                  <el-menu-item index="1-2">单据导入</el-menu-item>
                  <el-menu-item index="1-3">单据录入</el-menu-item>
                </el-menu-item-group>
              </el-submenu>
              <el-submenu index="2">
                <template slot="title">
                  <i class="el-icon-location"></i>
                  <span>开具发票</span>
                </template>
                <el-menu-item-group>
                  <el-menu-item index="2-1">单张开具</el-menu-item>
                  <el-menu-item index="2-2">批量开具</el-menu-item>
                  <el-menu-item index="2-3">冲红开具</el-menu-item>
                  <el-menu-item index="2-4">虚拟开具</el-menu-item>
                </el-menu-item-group>
              </el-submenu>
                            <el-submenu index="3">
                <template slot="title">
                  <i class="el-icon-location"></i>
                  <span>发票管理</span>
                </template>
                <el-menu-item-group>
                  <el-menu-item index="3-1">发票查询</el-menu-item>
                  <el-menu-item index="3-2">查询统计</el-menu-item>
                  <el-menu-item index="3-3">————</el-menu-item>
                  <el-menu-item index="3-4">————</el-menu-item>
                </el-menu-item-group>
              </el-submenu>              
              <el-submenu index="4">
                <template slot="title">
                  <i class="el-icon-location"></i>
                  <span>系统管理</span>
                </template>
                <el-menu-item-group>
                  <el-menu-item index="4-1">组织机构</el-menu-item>
                  <el-menu-item index="4-2">人员管理</el-menu-item>
                  <el-menu-item index="4-3">商品管理</el-menu-item>
                  <el-menu-item index="4-4">角色管理</el-menu-item>
                </el-menu-item-group>
              </el-submenu>
            </el-menu>
          </div>
        </el-col>
        <el-col :xs="20" :sm="20" :md="20" :lg="20">
          <div>
            <div
              style="border: 1px solid #A6A6A6; border-radius:6px; padding:5px; margin:2px; background-color: white"
            >
              <el-breadcrumb separator="/">
                <el-breadcrumb-item v-for="item in breadcrumbItems" key="item">{{item}}</el-breadcrumb-item>
              </el-breadcrumb>
            </div>
          </div>

          <div style="margin-top:10px;width:1300px;float: left;">
            <router-view></router-view>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
  <!-- <div>
  <div class="home">
   <div class="zhuangtai">
      <el-container>
        <el-button @click="exit">退出登录</el-button>
        <el-button @click="test">测试</el-button>
      </el-container>
    </div> 
  </div>
  
  </div>-->
</template>

<script>
// @ is an alias to /src
import home from "@/components/page/home.vue";

import Axios from "axios";
let Base64 = require('js-base64').Base64
export default {
  name: "home",
  data(){
    return{
      name:""
    }
  },
  components: {
    home,
  },
  created:function () {

      let user = decodeURIComponent(escape(window.atob(localStorage.getItem('Authorization').split('.')[1])))
      let res = JSON.parse(user).identity 
      this.name=res
  },
  methods: {
    
    exit() {
      //退出登录，清空token
      localStorage.removeItem("Authorization");
      this.$router.push("/login");
      alert("您已成功退出系统！");
    },
    test() {
      Axios({
        method: "post",
        url: "/protected",
        data: { firstName: "Fred", lastName: "Flintstone" },
      })
        .then(function (res) {
          // alert(localStorage.getItem('Authorization'));
          console.log("res", res);
        })
        .catch(function (err) {
      localStorage.removeItem("Authorization");
      this.$router.push("/login");
      alert("您已成功退出系统！");
          // alert(localStorage.getItem("Authorization"));
          console.log("err", err);
        });
    },
    handleIconClick(ev) {
      console.log(ev);
    },

    handleSelect(key, keyPath) {
      switch (key) {
        case "1-1":
          this.$router.push("/read");
          this.breadcrumbItems = ["单据读入"];
          break;
        case "1-2":
          this.$router.push("/lead");
          this.breadcrumbItems = ["单据导入"];
          break;
        case "1-3":
          this.$router.push("/write");
          this.breadcrumbItems = ["单据录入"];
          break;
      }
    },
  },
};
</script>
<style>
.zhuangtai {
  float: right;
}
</style>