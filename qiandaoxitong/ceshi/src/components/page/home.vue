<template>
  <el-container>
    <el-header>
      <el-row>
        <el-col :span="12">
          <div class="grid-content bg-purple" style="text-align: left;">
            <span style="font-size: 30px;color: #ffffff;">发票管理系统V1.0</span>
          </div>
        </el-col>
        <el-col :span="12">
          <div class="grid-content bg-purple-light">
            <div>
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
          </div>
        </el-col>
      </el-row>
    </el-header>
    <el-container>
      <el-aside style="background-color: #545c64">
        <el-menu
          default-active="2"
          class="el-menu-vertical-demo"
          @select="handleSelect"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
          style="height: 800px;"
          :unique-opened="true"
        >
          <!-- style="height: 800px;width: 200px;" -->
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
              <el-menu-item index="4-5">客户管理</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main>
        <div style="height: 600px">
          <router-view></router-view>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
// @ is an alias to /src
import home from "@/components/page/home.vue";
import Axios from "axios";
let Base64 = require("js-base64").Base64;
export default {
  name: "home",
  data() {
    return {
      name: "",
    };
  },
  components: {
    home,
  },
  created: function () {
    let user = decodeURIComponent(
      escape(window.atob(localStorage.getItem("Authorization").split(".")[1]))
    );
    let res = JSON.parse(user).identity;
    this.name = res;
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
          this.$router.push("/read").catch(err => {err});
          // this.breadcrumbItems = ["单据读入"];
          break;
        case "1-2":
          this.$router.push("/lead").catch(err => {err});
          // this.breadcrumbItems = ["单据导入"];
          break;
        case "1-3":
          this.$router.push("/write").catch(err => {err});
          // this.breadcrumbItems = ["单据录入"];
          break;
        case "4-3":
          this.$router.push("/spgl").catch(err => {err});
          // this.breadcrumbItems = ["客户管理"];
          break;
        case "4-5":
          this.$router.push("/khgl").catch(err => {err});
          // this.breadcrumbItems = ["客户管理"];
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
.el-header,
.el-footer {
  background-color: #5eabd9;
  color: #333;
  text-align: center;
  line-height: 60px;
}
</style>